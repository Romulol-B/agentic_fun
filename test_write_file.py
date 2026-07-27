import unittest

from functions.write_file import write_file


class TestWrite(unittest.TestCase):
    def test(self) -> None:
        result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(result)

        result = write_file(
            "calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"
        )
        print(result)

        result = write_file("calculator", "/tmp/temp.txt", "this hould not be allowed")
        print(result)


if __name__ == "__main__":
    unittest.main()
