import unittest

from functions.get_files_info import get_files_info


class TestPath(unittest.TestCase):
    def test_get_files_info_dot(self):
        self.maxDiff = None
        case = {"working_directory": "calculator", "directory": "."}
        actual = get_files_info(case["working_directory"], case["directory"])
        expected = (
            "Result for current directory: "
            + "\n- main.py: file_size= bytes, is_dir=False"
            + "\n- tests.py: file_size= bytes, is_dir=False"
            + "\n- pkg: file_size=bytes, is_dir=True"
        )
        print("actual:", actual)
        print("expected", expected)

    def test_get_files_info_bin(self):
        case = {"working_directory": "calculator", "directory": "/bin"}
        actual = get_files_info(case["working_directory"], case["directory"])
        expected = """ Result for 'pkg' directory:
          - calculator.py: file_size=1721 bytes, is_dir=False
          - render.py: file_size=376 bytes, is_dir=False
       """
        print("actual:", actual)
        print("expected", expected)

    def test_get_files_info_parent(self):
        case = {"working_directory": "calculator", "directory": "../"}
        actual = get_files_info(case["working_directory"], case["directory"])
        expected = f'Error: Cannot list "{case["directory"]}" as it is outside the permitted working directory'
        print("actual:", actual)
        print("expected", expected)

    def test_get_files_info_pkg(self):
        case = {"working_directory": "calculator", "directory": "pkg"}
        actual = get_files_info(case["working_directory"], case["directory"])
        expected = """Result for 'pkg' directory:
          - calculator.py: file_size=1721 bytes, is_dir=False
          - render.py: file_size=376 bytes, is_dir=False
        """
        print("actual:", actual)
        print("expected", expected)

    def test_get_files_info_main(self):
        case = {"working_directory": "calculator", "directory": "main.py"}
        actual = get_files_info(case["working_directory"], case["directory"])
        expected = f'Error: "{case["directory"]}" is not a directory'
        print("actual:", actual)
        print("expected", expected)


if __name__ == "__main__":
    unittest.main()
