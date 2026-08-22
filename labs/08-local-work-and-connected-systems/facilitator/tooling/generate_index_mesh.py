#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

IGNORED_DIRS = {'.git', '__pycache__'}
IGNORED_FILES = {'INDEX.md'}


def visible_children(directory: Path):
    directories = sorted(
        [
            path
            for path in directory.iterdir()
            if path.is_dir()
            and path.name not in IGNORED_DIRS
            and not path.name.startswith('.')
        ],
        key=lambda path: path.name.lower(),
    )
    files = sorted(
        [
            path
            for path in directory.iterdir()
            if path.is_file()
            and path.name not in IGNORED_FILES
            and not path.name.startswith('.')
        ],
        key=lambda path: path.name.lower(),
    )
    return directories, files


def render_index(directory: Path) -> str:
    directories, files = visible_children(directory)
    lines = [
        f'# Index: {directory.name or directory.resolve().name}',
        '',
        'Generated from the filesystem. Do not hand edit.',
        '',
    ]

    if directories:
        lines.extend(['## Directories', ''])
        lines.extend(
            f'- [{child.name}]({child.name}/INDEX.md)' for child in directories
        )
        lines.append('')

    if files:
        lines.extend(['## Files', ''])
        lines.extend(f'- [{child.name}]({child.name})' for child in files)
        lines.append('')

    if not directories and not files:
        lines.extend(['_No indexed children._', ''])

    return '\n'.join(lines)


def generate(directory: Path) -> list[Path]:
    directories, _ = visible_children(directory)
    generated: list[Path] = []

    for child in directories:
        generated.extend(generate(child))

    index_path = directory / 'INDEX.md'
    index_path.write_text(render_index(directory), encoding='utf-8', newline='\n')
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

    cwd = Path.cwd().resolve()
    for path in generate(root):
        try:
            print(path.relative_to(cwd))
        except ValueError:
            print(path)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
