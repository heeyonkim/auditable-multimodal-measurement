from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ResearchObjectTests(unittest.TestCase):
    def test_summary_matches_checked_in_snapshot(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "summary.json"
            subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "scripts" / "summarize_pilot.py"),
                    "--data-dir",
                    str(ROOT / "data" / "derived"),
                    "--output",
                    str(output),
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            expected = json.loads((ROOT / "summary_check.json").read_text(encoding="utf-8"))
            actual = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(actual, expected)

    def test_manifest_verification_passes(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts" / "verify_research_object.py"),
                "--check",
            ],
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)

    def test_measure_specification_prototype_is_standalone(self) -> None:
        prototype = ROOT / "tools" / "measure-specification-prototype" / "index.html"
        html = prototype.read_text(encoding="utf-8")
        self.assertIn("<title>Measure-Specification Prototype</title>", html)
        self.assertNotIn("<script src=", html)
        self.assertNotIn("<link rel=\"stylesheet\"", html)


if __name__ == "__main__":
    unittest.main()
