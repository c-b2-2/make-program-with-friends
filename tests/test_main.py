import unittest

from src.main import add


class AddTest(unittest.TestCase):
    def test_adds_positive_integers(self) -> None:
        self.assertEqual(add(2, 3), 5)

    def test_adds_negative_integer(self) -> None:
        self.assertEqual(add(-2, 3), 1)

    def test_adds_zero(self) -> None:
        self.assertEqual(add(0, 3), 3)


if __name__ == "__main__":
    unittest.main()
