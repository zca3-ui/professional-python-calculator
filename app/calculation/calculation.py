"""Calculation model for the calculator application."""

from dataclasses import dataclass
from typing import Callable


@dataclass
class Calculation:
    """Represent a calculation involving two numbers."""

    first: float
    second: float
    operation: Callable[[float, float], float]

    def perform(self) -> float:
        """Perform the calculation and return the result."""
        return self.operation(self.first, self.second)