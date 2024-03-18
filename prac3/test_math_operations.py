import pytest
from math_operations import add, subtract, multiply, divide
import random

@pytest.fixture
def random_numbers():
    num1 = random.randint(-100, 100)
    num2 = random.randint(-100, 100)
    return num1, num2

def test_addition(random_numbers):
    num1, num2 = random_numbers
    assert add(num1, num2) == num1 + num2

def test_subtraction(random_numbers):
    num1, num2 = random_numbers
    assert subtract(num1, num2) == num1 - num2

def test_multiplication(random_numbers):
    num1, num2 = random_numbers
    assert multiply(num1, num2) == num1 * num2

def test_division(random_numbers):
    num1, num2 = random_numbers
    if num2 != 0:
        assert divide(num1, num2) == num1 / num2
    else:
        with pytest.raises(ValueError):
            divide(num1, num2)
