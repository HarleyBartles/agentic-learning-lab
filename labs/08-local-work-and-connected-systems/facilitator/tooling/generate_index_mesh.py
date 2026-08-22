#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from collections import defaultdict
from pathlib import Path

INDEX_NAME = 'INDEX.md'


def git_root(path: Path) -> Path:
    result = subprocess.run(
        ['git', '-C', str(path), 'rev-parse', '--show-toplevel'],
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError('target must be inside a Git working tree')
    return Path(result.stdout.strip()).resolve()


def tracked_files(root: Path) -> list[Path]:
    repo = git_root(root)
    relative_root = root.relative_to(repo)
    pathspec = '.' if relative_root == Path('.') else relative_root.as_posix()
    result = subprocess.run(
        ['git', '-C', str(repo), 'ls-files', '--cached', '-z', '--', pathspec],
        capture_output=True,
        check=True,
    )

    files: list[Path] = []
    for raw in result.stdout.split(b'\0'):
        if not raw:
            continue
        repo_relative = Path(raw.decode('utf-8'))
        relative = (repo / repo_relative).relative_to(root)
        if relative.name == INDEX_NAME:
            continue
        if any(part.startswith('.') for part in relative.parts):
            continue
        files.append(relative)

    return sorted(files, key=lambda path: path.as_posix().lower())


def build_mesh(files: list[Path]):
    child_dirs: dict[Path, set[str]] = defaultdict(set)
    child_files: dict[Path, set[str]] = defaultdict(set)
    directories = {Path('.')}

    for file_path in files:
        parent = file_path.parent
        directories.add(parent)
        child_files[parent].add(file_path.name)

        cursor = parent
        while cursor != Path('.'):
            ancestor = cursor.parent
            child_dirs[ancestor].add(cursor.name)
            directories.add(ancestor)
            cursor = ancestor

    return directories, child_dirs, child_files


def render_index(directory: Path, child_dirs: set[str], child_files: set[str]) -> str:
    label = directory.name if directory != Path('.') else 'root'
    lines = [
        f'# Index: {label}',
        '',
        'Generated from the Git index. Do not hand edit.',
        '',
    ]

    if child_dirs:
        lines.extend(['## Directories', ''])
        lines.extend(
            f'- [{name}]({name}/INDEX.md)' for name in sorted(child_dirs, key=str.lower)
        )
        lines.append('')

    if child_files:
        lines.extend(['## Files', ''])
        lines.extend(f'- [{name}]({name})' for name in sorted(child_files, key=str.lower))
        lines.append('')

    if not child_dirs and not child_files:
        lines.extend(['_No indexed children._', ''])

    return '\n'.join(lines)


def generate(root: Path) -> list[Path]:
    files = tracked_files(root)
    directories, child_dirs, child_files = build_mesh(files)
    generated: list[Path] = []

    for relative_dir in sorted(
        directories,
        key=lambda path: (len(path.parts), path.as_posix().lower()),
    ):
        directory = root if relative_dir == Path('.') else root / relative_dir
        directory.mkdir(parents=True, exist_ok=True)
        index_path = directory / INDEX_NAME
        index_path.write_text(
            render_index(
                relative_dir,
                child_dirs[relative_dir],
                child_files[relative_dir],
            ),
            encoding='utf-8',
            newline='\n',
        )
        generated.append(index_path)

    return generated


def main() -> int:
    if len(sys.argv) != 2:
        print('usage: generate_index_mesh.py <root>', file=sys.stderr)
        return 2

    root = Path(sys.argv[1]).resolve()
    if not root.is_dir():
        print(f'not a directory: {root}', file=sys.stderr)
        return 2

    try:
        generated = generate(root)
    except (RuntimeError, subprocess.CalledProcessError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 2

    cwd = Path.cwd().resolve()
    for path in generated:
        try:
            print(path.relative_to(cwd))
        except ValueError:
            print(path)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
