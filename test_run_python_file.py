import unittest
from functions.run_python_file import run_python_file

class TestRunPythonFile(unittest.TestCase):
    def test_run_main_py(self):
        result = run_python_file("calculator", "main.py")
        list_expected_strings = [
          "Calculator App", 
          'Usage: python main.py "<expression>"',
          'Example: python main.py "3 + 5"']
        
        print(result)

        for expected in list_expected_strings:
            self.assertIn(expected, result)
            
    def test_run_main_py_with_args(self):
        result = run_python_file("calculator", "main.py", ["3 + 5"])
        list_expected_strings = [
          '"expression": "3 + 5",', 
          '"result": 8']
        
        print(result)

        for expected in list_expected_strings:
            self.assertIn(expected, result)
            
    def test_run_test_py(self):
        result = run_python_file("calculator", "tests.py")
        
        print(result)

        self.assertIn("OK", result)
        
    def test_run_parent_main_py(self):
        result = run_python_file("calculator", "../main.py")
        
        print(result)
        
    def test_run_non_existent(self):
        result = run_python_file("calculator", "nonexistent.py")
        
        print(result)
        
    def test_run_non_python(self):
        result = run_python_file("calculator", "lorem.txt")
        
        print(result)


if __name__ == "__main__":
    unittest.main()