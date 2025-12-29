import unittest
from functions.get_file_content import get_file_content

class TestGetFilesInfo(unittest.TestCase):
    def test_lorem_txt(self):
        result = get_file_content("calculator", "lorem.txt")
        
        print(len(result))
        print(result[10000:])
        
        self.assertEqual(10051, len(result))
        self.assertEqual('[...File "lorem.txt" truncated at 10000 characters]',result[10000:])
        
    def test_main_py(self):
        result = get_file_content("calculator", "main.py")
        
        print(len(result))
        print(result)
        
        self.assertIn("calculator/main.py", result)
        
    def test_calculator_py(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        
        print(len(result))
        print(result)
        
        self.assertIn("calculator/pkg/calculator.py", result)
        
    def test_file_outside_working_dir(self):
        file_path = "/bin/cat"
        result = get_file_content("calculator", file_path)
        
        print(result)
        
        self.assertEqual(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory', result)
        
    def test_file_does_not_exists(self):
        file_path = "pkg/does_not_exist.py"
        result = get_file_content("calculator", file_path)
        
        print(result)
        
        self.assertEqual(f'Error: File not found or is not a regular file: "{file_path}"', result)
        
    



if __name__ == "__main__":
    unittest.main()