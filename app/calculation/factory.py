"""Factory for creating Calculation objects."""

from app.calculation.calculation import Calculation
from app.operation.operations import Operations


class CalculationFactory:
    """Create Calculation objects based on an operation name."""

    OPERATIONS = {
        "add": Operations.add,
        "subtract": Operations.subtract,
        "multiply": Operations.multiply,
        "divide": Operations.divide,
    }

    @classmethod
    def create(
        cls,
        operation_name: str,
        first: float,
        second: float,
    ) -> Calculation:
        """Create a Calculation for the requested operation.

        Raises:
            ValueError: If the operation is not supported.
        """
        try:
            operation = cls.OPERATIONS[operation_name.lower()]
        except KeyError as error:
            raise ValueError(
                f"Unsupported operation: {operation_name}"
            ) from error

        return Calculation(first, second, operation)