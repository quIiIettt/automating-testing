import pytest
from eq_solver import square_eq_solver

def test_one_valid_root():
    result = square_eq_solver(1, -2, 1)
    assert result == [1.0]

def test_two_valid_roots():
    result = square_eq_solver(1, -3, 2)
    assert result == [1.0, 2.0]

def test_no_valid_roots():
    result = square_eq_solver(1, 2, 5)
    assert result == []