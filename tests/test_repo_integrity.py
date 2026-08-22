# SPDX-License-Identifier: MIT
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

CHECKER = Path(__file__).resolve().parents[1] / "tools" / "repo_integrity.py"


def run_checker(root: Path):
    return subprocess.run(
        [sys.executable, str(CHECKER), str(root)],
        text=True,
        capture_output=True,
        check=False,
    )


class RepoIntegrityTests(unittest.TestCase):
    def test_valid_repository_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs").mkdir()
            (root / "labs" / "01-first-lab").mkdir(parents=True)
            (root / "README.md").write_text("See [docs](docs/guide.md).\n", encoding="utf-8")
            (root / "docs" / "guide.md").write_text("```text\nhello\n```\n", encoding="utf-8")
            (root / "labs" / "01-first-lab" / "README.md").write_text("# Lab 1\n", encoding="utf-8")

            result = run_checker(root)

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_missing_relative_markdown_link_fails_with_source_and_target(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("See [missing](docs/missing.md).\n", encoding="utf-8")

            result = run_checker(root)

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("README.md", result.stdout)
            self.assertIn("docs/missing.md", result.stdout)

    def test_unclosed_markdown_fence_fails_with_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("```text\nnever closed\n", encoding="utf-8")

            result = run_checker(root)

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("README.md", result.stdout)
            self.assertIn("unclosed", result.stdout.lower())

    def test_duplicate_lab_number_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in ("01-first", "01-other"):
                lab = root / "labs" / name
                lab.mkdir(parents=True)
                (lab / "README.md").write_text("# Lab\n", encoding="utf-8")

            result = run_checker(root)

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("duplicate lab number 01", result.stdout.lower())

    def test_numbered_lab_without_readme_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "labs" / "02-no-readme").mkdir(parents=True)

            result = run_checker(root)

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("labs/02-no-readme/README.md", result.stdout)


if __name__ == "__main__":
    unittest.main()
