import unittest
<<<<<<< HEAD
from calc_solution2 import add, subtract, multiply, divide, remainder, exponent, program
=======
from unittest.mock import patch
import importlib
import calc_v2

importlib.reload(calc_v2)

from calc_v2 import add, subtract, multiply, divide, remainder, exponent, program
>>>>>>> 685b30d (Updated test files and assigned to calc_v1/2/3)

class TestCalcSolution2(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 7), 21)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)

    def test_divide(self):
<<<<<<< HEAD
        self.assertEqual(divide(8, 4), 2)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(5, 2), 2.5)
=======
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(-1, -1), 1)
>>>>>>> 685b30d (Updated test files and assigned to calc_v1/2/3)
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)

    def test_remainder(self):
        self.assertEqual(remainder(10, 3), 1)
        self.assertEqual(remainder(-1, 1), 0)
<<<<<<< HEAD
        self.assertEqual(remainder(5, 2), 1)
=======
        self.assertEqual(remainder(-1, -1), 0)
>>>>>>> 685b30d (Updated test files and assigned to calc_v1/2/3)

    def test_exponent(self):
        self.assertEqual(exponent(2, 3), 8)
        self.assertEqual(exponent(-1, 1), -1)
<<<<<<< HEAD
        self.assertEqual(exponent(5, 0), 1)

    def test_program_repeat(self):
        import builtins
        input_values = ['6', '2', '3', 'no']
        output = []

        def mock_input(s):
            output.append(s)
            return input_values.pop(0)

        builtins.input = mock_input
        builtins.print = lambda s: output.append(s)

        program()

        self.assertIn('Would you like to run another program?(yes/no): ', output)
        self.assertIn('Bye!', output)

if __name__ == '__main__':
    unittest.main()
=======
        self.assertEqual(exponent(-1, -1), -1)

    @patch("builtins.input", side_effect=["1", "5", "3", "no"])  # Simulate: choice=1, num1=5, num2=3, exit program
    @patch("builtins.print")  # Mock print output
    def test_program_addition(self, mock_print, mock_input):
        program()  # Run the program function
        mock_print.assert_any_call(8)  # Expect output of 5 + 3 = 8

    @patch("builtins.input", side_effect=["4", "10", "2", "no"])  # Simulate: choice=4, num1=10, num2=2, exit
    @patch("builtins.print")  # Mock print output
    def test_program_division(self, mock_print, mock_input):
        program()  # Run the program function
        mock_print.assert_any_call(5)  # Expect output of 10 / 2 = 5

    @patch("builtins.input", side_effect=["6", "2", "3", "yes", "5", "10", "3", "no"])  
    @patch("builtins.print")  
    def test_program_exponent_and_remainder(self, mock_print, mock_input):
        program()  
        mock_print.assert_any_call(8)  # Expect 2^3 = 8
        mock_print.assert_any_call(1)  # Expect 10 % 3 = 1

if __name__ == "__main__":
    unittest.main()
>>>>>>> 685b30d (Updated test files and assigned to calc_v1/2/3)
