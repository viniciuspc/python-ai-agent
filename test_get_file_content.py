import unittest
from functions.get_file_content import get_file_content

class TestGetFilesInfo(unittest.TestCase):
    def test_current_dir(self):
        result = get_file_content("calculator", "lorem.txt")
        list_expected_strings = ["main.py", "pkg", "tests.py", "file_size=","is_dir=False", "is_dir=True"]
        
        print(len(result))



if __name__ == "__main__":
    unittest.main()