import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name('generate_index_mesh.py')


class IndexMeshTests(unittest.TestCase):
    def init_repo(self, root: Path):
        subprocess.run(['git', 'init', '-q', str(root)], check=True)
        subprocess.run(
            ['git', '-C', str(root), 'config', 'user.email', 'lab@example.com'],
            check=True,
        )
        subprocess.run(
            ['git', '-C', str(root), 'config', 'user.name', 'Lab'],
            check=True,
        )

    def stage(self, root: Path, *paths: str):
        subprocess.run(['git', '-C', str(root), 'add', '--', *paths], check=True)

    def run_generator(self, root: Path):
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(root)],
            cwd=root,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_regeneration_discovers_tracked_unindexed_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.init_repo(root)
            (root / 'curriculum').mkdir()
            (root / 'curriculum' / 'overview.md').write_text(
                'overview', encoding='utf-8'
            )
            (root / 'forgotten').mkdir()
            (root / 'forgotten' / 'answer.md').write_text(
                'answer', encoding='utf-8'
            )
            self.stage(root, 'curriculum/overview.md', 'forgotten/answer.md')

            result = self.run_generator(root)

            self.assertEqual(result.returncode, 0, result.stderr)
            root_index = (root / 'INDEX.md').read_text(encoding='utf-8')
            self.assertIn('[curriculum](curriculum/INDEX.md)', root_index)
            self.assertIn('[forgotten](forgotten/INDEX.md)', root_index)
            forgotten_index = (root / 'forgotten' / 'INDEX.md').read_text(
                encoding='utf-8'
            )
            self.assertIn('[answer.md](answer.md)', forgotten_index)

    def test_regeneration_is_idempotent(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.init_repo(root)
            (root / 'references').mkdir()
            (root / 'references' / 'operations.md').write_text(
                'ops', encoding='utf-8'
            )
            self.stage(root, 'references/operations.md')

            first = self.run_generator(root)
            self.assertEqual(first.returncode, 0, first.stderr)
            first_root = (root / 'INDEX.md').read_bytes()
            first_child = (root / 'references' / 'INDEX.md').read_bytes()

            second = self.run_generator(root)
            self.assertEqual(second.returncode, 0, second.stderr)
            self.assertEqual(first_root, (root / 'INDEX.md').read_bytes())
            self.assertEqual(first_child, (root / 'references' / 'INDEX.md').read_bytes())

    def test_unstaged_file_does_not_enter_commit_mesh(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.init_repo(root)
            (root / 'tracked.md').write_text('tracked', encoding='utf-8')
            (root / 'draft.md').write_text('draft', encoding='utf-8')
            self.stage(root, 'tracked.md')

            result = self.run_generator(root)

            self.assertEqual(result.returncode, 0, result.stderr)
            root_index = (root / 'INDEX.md').read_text(encoding='utf-8')
            self.assertIn('[tracked.md](tracked.md)', root_index)
            self.assertNotIn('draft.md', root_index)


if __name__ == '__main__':
    unittest.main()
