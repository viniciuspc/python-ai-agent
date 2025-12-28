import unittest
from functions.get_files_info import get_files_info

class TestGetFilesInfo(unittest.TestCase):
    def test_current_dir(self):
        result = get_files_info("calculator", ".")
        list_expected_strings = ["main.py", "pkg", "tests.py", "file_size=","is_dir=False", "is_dir=True"]
        
        print(result)

        for expected in list_expected_strings:
            self.assertIn(expected, result)

    def test_pkg_directory(self):
        result = get_files_info("calculator", "pkg")
        list_expected_strings = ["calculator.py", "render.py", "file_size=","is_dir=False"]
        
        print(result)
        
        for expected in list_expected_strings:
            self.assertIn(expected, result)

    def test_root_bin_directory(self):
        result = get_files_info("calculator", "/bin")
        expected = 'Error: Cannot list "/bin" as it is outside the permitted working directory'

        print(result)

        self.assertEqual(expected, result)
    
    def test_parent_directory(self):
        result = get_files_info("calculator", "../")
        expected = 'Error: Cannot list "../" as it is outside the permitted working directory'
        
        print(result)
        
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()