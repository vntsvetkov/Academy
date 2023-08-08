import unittest
from calculator import Calculator
import time


class TestCalculator(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calculator()
        self.begin_time = time.time()

    def tearDown(self) -> None:
        self.end_time = time.time()
        print(f"Время теста: ", self.end_time - self.begin_time)

    def test_add(self):
        self.assertEqual(self.calc.add(3, 2), 5)

    def test_sub(self):
        self.assertEqual(self.calc.sub(3, 2), 1)

    def test_mult(self):
        self.assertEqual(self.calc.mult(3, 2), 6)

    def test_div(self):
        self.assertEqual(self.calc.div(3, 2), 1.5)

    def test_div_by_zero(self):
        self.assertEqual(self.calc.div(3, 0), "Деление на ноль невозможно")

    def test_sqrt(self):
        self.assertEqual((self.calc.sqrt(9)), 3.0)

    def test_sqrt_exception(self):
        self.assertRaises(ValueError, self.calc.sqrt, -1)


if __name__ == "__main__":
    unittest.main()
