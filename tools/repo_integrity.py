#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
LAB_RE = re.compile(r"^(\d{2})-.+")
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")


def display(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def extract_link_target(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<") and ">" in target:
        return target[1 : target.index(">")]
    if " \"" in target:
        target = target.split(" \"", 1)[0]
    elif " '" in target:
        target = target.split(" '", 1)[0]
    return target.strip()


def check_markdown_links(root: Path) -> list[str]:
    errors: list[str] = []
    for path in sorted(root.rglob("*.md")):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            target = extract_link_target(match.group(1))
            if not target or target.startswith("#"):
                continue
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith("//"):
                continue
            link_path = unquote(parsed.path)
            if not link_path:
                continue
            resolved = (root / link_path.lstrip("/")) if link_path.startswith("/") else (path.parent / link_path)
            if not resolved.exists():
                errors.append(f"{display(path, root)}: missing relative link target {target}")
    return errors


def check_markdown_fences(root: Path) -> list[str]:
    errors: list[str] = []
    for path in sorted(root.rglob("*.md")):
        if ".git" in path.parts:
            continue
        opening_char: str | None = None
        opening_len = 0
        opening_line = 0
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            match = FENCE_RE.match(line)
            if not match:
                continue
            fence = match.group(1)
            char = fence[0]
            if opening_char is None:
                opening_char = char
                opening_len = len(fence)
                opening_line = line_no
            elif char == opening_char and len(fence) >= opening_len:
                opening_char = None
                opening_len = 0
                opening_line = 0
        if opening_char is not None:
            errors.append(f"{display(path, root)}:{opening_line}: unclosed markdown fence")
    return errors


def check_labs(root: Path) -> list[str]:
    errors: list[str] = []
    labs = root / "labs"
    if not labs.is_dir():
        return errors

    by_number: dict[str, list[Path]] = {}
    for path in sorted(labs.iterdir()):
        if not path.is_dir():
            continue
        match = LAB_RE.match(path.name)
        if not match:
            continue
        number = match.group(1)
        by_number.setdefault(number, []).append(path)
        readme = path / "README.md"
        if not readme.is_file():
            errors.append(f"missing mature lab README: {display(readme, root)}")

    for number, paths in sorted(by_number.items()):
        if len(paths) > 1:
            names = ", ".join(display(path, root) for path in paths)
            errors.append(f"duplicate lab number {number}: {names}")
    return errors


def run(root: Path) -> list[str]:
    return [
        *check_markdown_links(root),
        *check_markdown_fences(root),
        *check_labs(root),
    ]


def main(argv: list[str]) -> int:
    root = Path(argv[1] if len(argv) > 1 else ".").resolve()
    errors = run(root)
    if errors:
        print("Repository integrity check failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Repository integrity check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
