import unittest
import subprocess

class TestHelloWorld(unittest.TestCase):

    def test_print_hello_world(self):
        result = subprocess.run(["python3", "01.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout = result.stdout.strip()
        self.assertIn("Hello world", stdout)

class TestLinting(unittest.TestCase):

    def test_linting(self):
        result = subprocess.run(["flake8", "--verbose", "01.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        linting_output = result.stdout.strip()
        print(f"Linting output:\n{linting_output}")

        self.assertEqual(result.returncode, 0, f"Linting failed:\n{linting_output}")

if __name__ == '__main__':
    unittest.main()
