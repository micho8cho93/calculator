import unittest
from calc_v2 import add, subtract, multiply, divide, remainder, exponent, program

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