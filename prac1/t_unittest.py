import unittest
from eq_solver import square_eq_solver

class TestSquareEqSolver(unittest.TestCase):

    def test_one_valid_root(self):
        result = square_eq_solver(1, -2, 1)
        self.assertEqual(result, [1.0])

    def test_two_valid_roots(self):
        result = square_eq_solver(1, -3, 2)
        self.assertEqual(result, [1.0, 2.0])

    def test_no_valid_roots(self):
        result = square_eq_solver(1, 2, 5)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
