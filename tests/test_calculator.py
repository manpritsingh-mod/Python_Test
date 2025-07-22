"""
Unit tests for the calculator module.
Tests all basic mathematical operations and edge cases.
"""

import pytest
from src.calculator.calculator import Calculator


class TestCalculator:
    """Test class for Calculator functionality."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.calculator = Calculator()

    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        result = self.calculator.add(5, 3)
        assert result == 8

    def test_add_negative_numbers(self):
        """Test addition of negative numbers."""
        result = self.calculator.add(-5, -3)
        assert result == -8

    def test_add_mixed_numbers(self):
        """Test addition of positive and negative numbers."""
        result = self.calculator.add(5, -3)
        assert result == 2

    def test_add_zero(self):
        """Test addition with zero."""
        result = self.calculator.add(5, 0)
        assert result == 5

    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        result = self.calculator.subtract(10, 4)
        assert result == 6

    def test_subtract_negative_numbers(self):
        """Test subtraction of negative numbers."""
        result = self.calculator.subtract(-10, -4)
        assert result == -6

    def test_subtract_to_negative(self):
        """Test subtraction resulting in negative number."""
        result = self.calculator.subtract(3, 8)
        assert result == -5

    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        result = self.calculator.multiply(4, 5)
        assert result == 20

    def test_multiply_negative_numbers(self):
        """Test multiplication of negative numbers."""
        result = self.calculator.multiply(-4, -5)
        assert result == 20

    def test_multiply_mixed_numbers(self):
        """Test multiplication of positive and negative numbers."""
        result = self.calculator.multiply(-4, 5)
        assert result == -20

    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        result = self.calculator.multiply(10, 0)
        assert result == 0

    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        result = self.calculator.divide(15, 3)
        assert result == 5

    def test_divide_negative_numbers(self):
        """Test division of negative numbers."""
        result = self.calculator.divide(-15, -3)
        assert result == 5

    def test_divide_mixed_numbers(self):
        """Test division of positive and negative numbers."""
        result = self.calculator.divide(-15, 3)
        assert result == -5

    def test_divide_by_zero_raises_error(self):
        """Test that division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calculator.divide(10, 0)

    def test_divide_zero_by_number(self):
        """Test division of zero by a number."""
        result = self.calculator.divide(0, 5)
        assert result == 0

    def test_power_positive_base_positive_exponent(self):
        """Test power with positive base and exponent."""
        result = self.calculator.power(2, 3)
        assert result == 8

    def test_power_positive_base_zero_exponent(self):
        """Test power with positive base and zero exponent."""
        result = self.calculator.power(5, 0)
        assert result == 1

    def test_power_positive_base_negative_exponent(self):
        """Test power with positive base and negative exponent."""
        result = self.calculator.power(2, -2)
        assert result == 0.25

    def test_power_negative_base_positive_exponent(self):
        """Test power with negative base and positive exponent."""
        result = self.calculator.power(-2, 3)
        assert result == -8

    def test_power_fractional_exponent(self):
        """Test power with fractional exponent (square root)."""
        result = self.calculator.power(9, 0.5)
        assert result == 3.0

    @pytest.mark.parametrize("a,b,expected", [
        (1, 1, 2),
        (0, 0, 0),
        (100, 200, 300),
        (-5, 5, 0),
        (1.5, 2.5, 4.0)
    ])
    def test_add_parametrized(self, a, b, expected):
        """Parametrized test for addition with multiple test cases."""
        result = self.calculator.add(a, b)
        assert result == expected

    @pytest.mark.parametrize("a,b,expected", [
        (10, 2, 5),
        (9, 3, 3),
        (-10, -2, 5),
        (7, 2, 3.5)
    ])
    def test_divide_parametrized(self, a, b, expected):
        """Parametrized test for division with multiple test cases."""
        result = self.calculator.divide(a, b)
        assert result == expected
