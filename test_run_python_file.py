import unittest
from string import printable

from functions.run_python_file import run_python_file


class TestRun(unittest.TestCase):
    def test_main_info(self):
        a = run_python_file("calculator", "main.py")
        print(a)

    def test_main_8(self):
        print("plus test")
        a = run_python_file("calculator", "main.py", ["3 + 5"])
        print(a)

    def test_main_double_dot(self):
        print("plus test")
        a = run_python_file("calculator", "../main.py")
        print(a)

    def test_main_dne(self):
        print("plus test")
        a = run_python_file("calculator", "nonexistent.py")
        print(a)

    def test_main_lerem(self):
        print("plus test")
        a = run_python_file("calculator", "lorem.txt")
        print(a)


if __name__ == "__main__":
    unittest.main()
