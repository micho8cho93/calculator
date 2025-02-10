import unittest
<<<<<<< HEAD
=======
from unittest.mock import patch
>>>>>>> 685b30d (Updated test files and assigned to calc_v1/2/3)
from calc_v3 import add, subtract, multiply, divide, remainder, exponent, program

class TestCalcSolution3(unittest.TestCase):

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
        self.assertEqual(divide(8, 4), 2)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(5, 2), 2.5)
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)

    def test_remainder(self):
        self.assertEqual(remainder(10, 3), 1)
        self.assertEqual(remainder(-1, 1), 0)
        self.assertEqual(remainder(5, 2), 1)

    def test_exponent(self):
        self.assertEqual(exponent(2, 3), 8)
        self.assertEqual(exponent(-1, 1), -1)
        self.assertEqual(exponent(5, 0), 1)

<<<<<<< HEAD
    def test_invalid_choice(self):
        import builtins
        input_values = ['7', 'no']
        output = []

        def mock_input(s):
            output.append(s)
            return input_values.pop(0)

        builtins.input = mock_input
        builtins.print = lambda s: output.append(s)

        program()

        self.assertIn('Invalid input', output)

    def test_invalid_decision(self):
        import builtins
        input_values = ['1', '2', '3', 'maybe']
        output = []

        def mock_input(s):
            output.append(s)
            return input_values.pop(0)

        builtins.input = mock_input
        builtins.print = lambda s: output.append(s)

        program()

        self.assertIn('Invalid input', output)

if __name__ == '__main__':
=======
    @patch("builtins.input", side_effect=["1", "2", "3", "no"])  # Simulating addition (1), num1=2, num2=3, then exit
    @patch("builtins.print")
    def test_program_addition(self, mock_print, mock_input):
        program()
        mock_print.assert_any_call(5)  # Expecting output 2 + 3 = 5

    @patch("builtins.input", side_effect=["4", "10", "2", "no"])  # Division: 10 / 2
    @patch("builtins.print")
    def test_program_division(self, mock_print, mock_input):
        program()
        mock_print.assert_any_call(5.0)

    @patch("builtins.input", side_effect=["6", "2", "3", "yes", "5", "10", "3", "no"])  
    @patch("builtins.print")  
    def test_program_exponent_and_remainder(self, mock_print, mock_input):
        program()
        mock_print.assert_any_call(8)  # Expect 2^3 = 8
        mock_print.assert_any_call(1)  # Expect 10 % 3 = 1

    @patch("builtins.input", side_effect=["7", "no"])  
    @patch("builtins.print")
    def test_invalid_choice(self, mock_print, mock_input):
        program()
        mock_print.assert_any_call("Invalid input")

    @patch("builtins.input", side_effect=["1", "2", "3", "maybe"])  
    @patch("builtins.print")
    def test_invalid_decision(self, mock_print, mock_input):
        program()
        mock_print.assert_any_call("Invalid input")

if __name__ == "__main__":
>>>>>>> 685b30d (Updated test files and assigned to calc_v1/2/3)
    unittest.main()