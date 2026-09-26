"""Command-line calculator with a REPL interface."""

from app.calculation.calculation import Calculation
from app.calculation.factory import CalculationFactory


class Calculator:
    """Manage the calculator's interactive session."""

    def __init__(self) -> None:
        """Initialize an empty calculation history."""
        self.history: list[Calculation] = []

    @staticmethod
    def display_help() -> None:
        """Display available commands."""
        print("\nAvailable commands:")
        print("  add       - Add two numbers")
        print("  subtract  - Subtract the second number from the first")
        print("  multiply  - Multiply two numbers")
        print("  divide    - Divide the first number by the second")
        print("  history   - Show calculations from this session")
        print("  help      - Show this help message")
        print("  exit      - Exit the calculator")

    def display_history(self) -> None:
        """Display all calculations from the current session."""
        if not self.history:
            print("\nNo calculations have been performed yet.")
            return

        print("\nCalculation History:")

        for number, calculation in enumerate(self.history, start=1):
            result = calculation.perform()
            operation_name = self._get_operation_name(calculation)
            print(
                f"{number}. "
                f"{calculation.first} {operation_name} "
                f"{calculation.second} = {result}"
            )

    @staticmethod
    def _get_operation_name(calculation: Calculation) -> str:
        """Return a symbol for the calculation's operation."""
        operation_names = {
            "add": "+",
            "subtract": "-",
            "multiply": "*",
            "divide": "/",
        }

        for name, operation in CalculationFactory.OPERATIONS.items():
            if calculation.operation == operation:
                return operation_names[name]

        return "?"

    @staticmethod
    def get_number(prompt: str) -> float:
        """Request and validate a number from the user."""
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid number. Please enter a valid number.")

    def perform_calculation(self, operation_name: str) -> None:
        """Request numbers, create a calculation, and display its result."""
        first = self.get_number("Enter the first number: ")
        second = self.get_number("Enter the second number: ")

        try:
            calculation = CalculationFactory.create(
                operation_name,
                first,
                second,
            )
            result = calculation.perform()
        except (ValueError, ZeroDivisionError) as error:
            print(f"Error: {error}")
            return

        self.history.append(calculation)
        print(f"Result: {result}")

    def run(self) -> None:
        """Run the calculator REPL until the user exits."""
        print("Welcome to the Python Calculator!")
        print("Type 'help' to see available commands.")

        while True:
            command = input("\nEnter a command: ").strip().lower()

            if command == "exit":
                print("Goodbye!")
                break

            if command == "help":
                self.display_help()
                continue

            if command == "history":
                self.display_history()
                continue

            if command in CalculationFactory.OPERATIONS:
                self.perform_calculation(command)
                continue

            print(
                "Unknown command. Type 'help' to see available commands."
            )


if __name__ == "__main__":  # pragma: no cover
    Calculator().run()