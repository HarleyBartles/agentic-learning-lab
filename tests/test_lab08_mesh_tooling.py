# SPDX-License-Identifier: MIT

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


class Lab08MeshToolingTests(unittest.TestCase):
    def test_facilitator_mesh_tooling_contract(self) -> None:
        repo = Path(__file__).resolve().parents[1]
        test_script = repo / "labs" / "08-local-work-and-connected-systems" / "facilitator" / "assets" / "mesh-tooling" / "test_generate_index_mesh.py"
        result = subprocess.run(
            [sys.executable, str(test_script)],
            cwd=repo,
            text=True,
            capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
