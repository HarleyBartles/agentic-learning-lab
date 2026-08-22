#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("generate_index_mesh.py").resolve()


class MeshToolingTests(unittest.TestCase):
    def make_repo(self) -> Path:
        root = Path(tempfile.mkdtemp()).resolve()
        subprocess.run(["git", "init", "-q"], cwd=root, check=True)
        subprocess.run(["git", "config", "user.email", "lab@example.invalid"], cwd=root, check=True)
        subprocess.run(["git", "config", "user.name", "Lab"], cwd=root, check=True)
        (root / "environment" / "curriculum").mkdir(parents=True)
        (root / "environment" / "forgotten").mkdir(parents=True)
        (root / "environment" / "curriculum" / "overview.md").write_text("overview\n", encoding="utf-8")
        (root / "environment" / "forgotten" / "answer.md").write_text("keyword: lantern\n", encoding="utf-8")
        subprocess.run(["git", "add", "."], cwd=root, check=True)
        subprocess.run(["git", "commit", "-qm", "fixture"], cwd=root, check=True)
        return root

    def run_tool(self, root: Path, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["python", str(SCRIPT), *args],
            cwd=root,
            text=True,
            capture_output=True,
        )

    def test_check_fails_until_apply_generates_complete_mesh(self) -> None:
        root = self.make_repo()
        check_before = self.run_tool(root, "--check", "--scope", "environment")
        self.assertNotEqual(check_before.returncode, 0)
        self.assertIn("Index mesh is stale", check_before.stdout)

        apply_result = self.run_tool(root, "--apply", "--scope", "environment")
        self.assertEqual(apply_result.returncode, 0, apply_result.stderr)
        root_index = (root / "environment" / "INDEX.md").read_text(encoding="utf-8")
        self.assertIn("forgotten/", root_index)
        self.assertTrue((root / "environment" / "forgotten" / "INDEX.md").exists())

        check_after = self.run_tool(root, "--check", "--scope", "environment")
        self.assertEqual(check_after.returncode, 0, check_after.stdout + check_after.stderr)
        self.assertIn("Index mesh is current", check_after.stdout)

    def test_apply_is_byte_idempotent(self) -> None:
        root = self.make_repo()
        first = self.run_tool(root, "--apply", "--scope", "environment")
        self.assertEqual(first.returncode, 0, first.stderr)
        first_bytes = {
            p.relative_to(root).as_posix(): p.read_bytes()
            for p in sorted((root / "environment").rglob("INDEX.md"))
        }

        second = self.run_tool(root, "--apply", "--scope", "environment")
        self.assertEqual(second.returncode, 0, second.stderr)
        second_bytes = {
            p.relative_to(root).as_posix(): p.read_bytes()
            for p in sorted((root / "environment").rglob("INDEX.md"))
        }
        self.assertEqual(first_bytes, second_bytes)

    def test_untracked_files_do_not_enter_mesh(self) -> None:
        root = self.make_repo()
        (root / "environment" / "local-draft.txt").write_text("draft\n", encoding="utf-8")
        result = self.run_tool(root, "--apply", "--scope", "environment")
        self.assertEqual(result.returncode, 0, result.stderr)
        root_index = (root / "environment" / "INDEX.md").read_text(encoding="utf-8")
        self.assertNotIn("local-draft.txt", root_index)


if __name__ == "__main__":
    unittest.main()
