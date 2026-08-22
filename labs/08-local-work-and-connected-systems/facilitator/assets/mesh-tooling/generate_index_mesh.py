#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check or regenerate an INDEX.md navigation mesh from tracked Git state.")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Report whether generated INDEX.md files are current without mutating the worktree.")
    mode.add_argument("--apply", action="store_true", help="Write the expected INDEX.md files explicitly.")
    parser.add_argument("--scope", default=".", help="Repository-relative directory whose tracked tree should be indexed.")
    return parser.parse_args()


def git_lines(repo: Path, *args: str) -> list[str]:
    result = subprocess.run(["git", *args], cwd=repo, text=True, capture_output=True, check=True)
    return [line for line in result.stdout.splitlines() if line]


def repo_root() -> Path:
    return Path(git_lines(Path.cwd(), "rev-parse", "--show-toplevel")[0]).resolve()


def tracked_paths(repo: Path, scope: str) -> list[Path]:
    lines = git_lines(repo, "ls-files", "--cached", "--", scope)
    return [Path(line) for line in lines if Path(line).name != "INDEX.md"]


def tracked_indexes(repo: Path, scope: str) -> set[Path]:
    lines = git_lines(repo, "ls-files", "--cached", "--", scope)
    return {repo / Path(line) for line in lines if Path(line).name == "INDEX.md"}


def expected_directories(paths: list[Path], scope: Path) -> set[Path]:
    directories: set[Path] = {scope}
    for path in paths:
        parent = path.parent
        while parent == scope or scope in parent.parents:
            directories.add(parent)
            if parent == scope:
                break
            parent = parent.parent
    return directories


def render_index(directory: Path, paths: list[Path], directories: set[Path]) -> str:
    child_dirs = sorted(
        [candidate for candidate in directories if candidate.parent == directory and candidate != directory],
        key=lambda p: p.name.lower(),
    )
    child_files = sorted(
        [path for path in paths if path.parent == directory],
        key=lambda p: p.name.lower(),
    )

    title = directory.name or "."
    lines = [
        f"# Index: {title}",
        "",
        "Generated from tracked/staged Git state. Do not hand edit.",
        "",
    ]

    if child_dirs:
        lines.extend(["## Directories", ""])
        lines.extend(f"- [{child.name}]({child.name}/INDEX.md)" for child in child_dirs)
        lines.append("")

    if child_files:
        lines.extend(["## Files", ""])
        lines.extend(f"- [{child.name}]({child.name})" for child in child_files)
        lines.append("")

    if not child_dirs and not child_files:
        lines.extend(["_No indexed children._", ""])

    return "\n".join(lines)


def expected_mesh(repo: Path, scope_arg: str) -> dict[Path, str]:
    scope = Path(scope_arg)
    if scope.is_absolute():
        raise SystemExit("--scope must be repository-relative")

    paths = tracked_paths(repo, scope_arg)
    directories = expected_directories(paths, scope)
    return {
        repo / directory / "INDEX.md": render_index(directory, paths, directories)
        for directory in sorted(directories, key=lambda p: p.as_posix())
    }


def stale_paths(expected: dict[Path, str], obsolete: set[Path]) -> list[Path]:
    stale: list[Path] = []
    for path, content in expected.items():
        actual = path.read_text(encoding="utf-8") if path.exists() else None
        if actual != content:
            stale.append(path)
    stale.extend(sorted(obsolete))
    return stale


def main() -> int:
    args = parse_args()
    repo = repo_root()
    expected = expected_mesh(repo, args.scope)
    obsolete = tracked_indexes(repo, args.scope) - set(expected)
    stale = stale_paths(expected, obsolete)

    if args.check:
        if stale:
            print("Index mesh is stale:")
            for path in stale:
                print(path.relative_to(repo).as_posix())
            print("Run again with --apply to regenerate it.")
            return 1
        print("Index mesh is current.")
        return 0

    for path in sorted(obsolete):
        if path.exists():
            path.unlink()
        print(path.relative_to(repo).as_posix())

    for path, content in expected.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")
        print(path.relative_to(repo).as_posix())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
