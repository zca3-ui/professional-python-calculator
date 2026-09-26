"""Arithmetic operations used by the calculator."""


class Operations:
    """Provide basic arithmetic operations."""

    @staticmethod
    def add(first: float, second: float) -> float:
        """Return the sum of two numbers."""
        return first + second

    @staticmethod
    def subtract(first: float, second: float) -> float:
        """Return the difference between two numbers."""
        return first - second

    @staticmethod
    def multiply(first: float, second: float) -> float:
        """Return the product of two numbers."""
        return first * second

    @staticmethod
    def divide(first: float, second: float) -> float:
        """Return the quotient of two numbers.

        Raises:
            ZeroDivisionError: If the second number is zero.
        """
        if second == 0:
            raise ZeroDivisionError("Cannot divide by zero.")

        return first / second