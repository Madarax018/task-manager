import ast
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class ProjectTests(unittest.TestCase):

    def test_readme_exists(self):
        self.assertTrue((ROOT / "README.md").is_file())

    def test_application_exists(self):
        self.assertTrue(
            (ROOT / "main.py").is_file()
            or (ROOT / "index.html").is_file()
        )

    def test_python_syntax(self):
        script = ROOT / "main.py"
        if script.exists():
            ast.parse(script.read_text())

if __name__ == "__main__":
    unittest.main()
