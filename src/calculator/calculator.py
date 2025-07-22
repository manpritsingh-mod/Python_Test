"""
Simple calculator module with basic mathematical operations.
This module provides functions for addition, subtraction, multiplication, and division.
"""


class Calculator:
    """A simple calculator class with basic mathematical operations."""

    def add(self, first_number: float, second_number: float) -> float:
        """
        Add two numbers and return the result.
        
        Args:
            first_number (float): The first number to add
            second_number (float): The second number to add
            
        Returns:
            float: The sum of the two numbers
        """
        return first_number + second_number

    def subtract(self, first_number: float, second_number: float) -> float:
        """
        Subtract second number from first number and return the result.
        
        Args:
            first_number (float): The number to subtract from
            second_number (float): The number to subtract
            
        Returns:
            float: The difference between the two numbers
        """
        return first_number - second_number

    def multiply(self, first_number: float, second_number: float) -> float:
        """
        Multiply two numbers and return the result.
        
        Args:
            first_number (float): The first number to multiply
            second_number (float): The second number to multiply
            
        Returns:
            float: The product of the two numbers
        """
        return first_number * second_number

    def divide(self, first_number: float, second_number: float) -> float:
        """
        Divide first number by second number and return the result.
        
        Args:
            first_number (float): The dividend
            second_number (float): The divisor
            
        Returns:
            float: The quotient of the division
            
        Raises:
            ValueError: If attempting to divide by zero
        """
        if second_number == 0:
            raise ValueError("Cannot divide by zero")
        return first_number / second_number

    def power(self, base: float, exponent: float) -> float:
        """
        Raise base to the power of exponent.
        
        Args:
            base (float): The base number
            exponent (float): The exponent
            
        Returns:
            float: The result of base raised to exponent
        """
        return base ** exponent
