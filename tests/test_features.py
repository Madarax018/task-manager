import subprocess
import sys
import tempfile
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class TaskTests(unittest.TestCase):
    def test_add_and_complete(self):
        with tempfile.TemporaryDirectory() as temp:
            result = subprocess.run(
                [sys.executable, str(ROOT / "main.py")],
                input="1\nLearn Python\n3\n1\n5\n",
                text=True, capture_output=True,
                cwd=temp, timeout=10
            )
            self.assertEqual(result.returncode, 0)
            tasks = json.loads(
                (Path(temp) / "tasks.json").read_text()
            )
            self.assertEqual(tasks[0]["title"], "Learn Python")
            self.assertTrue(tasks[0]["done"])
