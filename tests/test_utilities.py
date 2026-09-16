import unittest

from src.divide import divide
from src.main import add
from src.subtract import subtract


class UtilityFunctionsTest(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self) -> None:
        self.assertEqual(subtract(10, 3), 7)

    def test_divide(self) -> None:
        self.assertEqual(divide(8, 2), 4)

    def test_divide_by_zero(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)


if __name__ == "__main__":
    unittest.main()
