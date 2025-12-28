import unittest
from functions.write_file import write_file

class TestWriteFile(unittest.TestCase):
    def test_write_current_dir(self):
        file_path = "loren.txt"
        content = "wait, this isn't lorem ipsum"
        result = write_file("calculator", file_path, content)
        print(result)

        expected = f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

        self.assertEqual(expected, result)

    def test_write_pkg_dir(self):
        file_path = "pkg/morelorem.txt"
        content = "lorem ipsum dolor sit amet"
        result = write_file("calculator", file_path, content)
        print(result)

        expected = f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

        self.assertEqual(expected, result)

    def test_write_tmp_dir(self):
        file_path = "/tmp/temp.txt"
        content = "this should not be allowed"
        result = write_file("calculator", file_path, content)
        print(result)

        expected = f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        self.assertEqual(expected, result)



if __name__ == "__main__":
    unittest.main()

