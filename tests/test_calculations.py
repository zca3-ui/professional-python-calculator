
"""Tests for Calculation, CalculationFactory, and Calculator."""

from unittest.mock import patch

import pytest

from app.calculation.calculation import Calculation
from app.calculation.factory import CalculationFactory
from app.calculator.calculator import Calculator
from app.operation.operations import Operations


# ---------------------------------------------------------
# Calculation tests
# ---------------------------------------------------------

@pytest.mark.parametrize(
    "operation, first, second, expected",
    [
        (Operations.add, 2, 3, 5),
        (Operations.subtract, 5, 3, 2),
        (Operations.multiply, 4, 3, 12),
        (Operations.divide, 10, 2, 5),
    ],
)
def test_calculation_perform(operation, first, second, expected):
    """Test Calculation.perform with multiple operations."""
    calculation = Calculation(first, second, operation)

    assert calculation.perform() == expected


# ---------------------------------------------------------
# CalculationFactory tests
# ---------------------------------------------------------

@pytest.mark.parametrize(
    "operation_name, first, second, expected",
    [
        ("add", 2, 3, 5),
        ("subtract", 5, 3, 2),
        ("multiply", 4, 3, 12),
        ("divide", 10, 2, 5),
    ],
)
def test_factory_creates_calculations(
    operation_name,
    first,
    second,
    expected,
):
    """Test that the factory creates the correct calculations."""
    calculation = CalculationFactory.create(
        operation_name,
        first,
        second,
    )

    assert isinstance(calculation, Calculation)
    assert calculation.perform() == expected


def test_factory_accepts_uppercase_operation():
    """Test that operation names are case-insensitive."""
    calculation = CalculationFactory.create("ADD", 2, 3)

    assert calculation.perform() == 5


def test_factory_rejects_invalid_operation():
    """Test that unsupported operations raise ValueError."""
    with pytest.raises(
        ValueError,
        match="Unsupported operation: power",
    ):
        CalculationFactory.create("power", 2, 3)


# ---------------------------------------------------------
# Calculator initialization and help tests
# ---------------------------------------------------------

def test_calculator_history_starts_empty():
    """Test that a new calculator starts with empty history."""
    calculator = Calculator()

    assert calculator.history == []


def test_display_help(capsys):
    """Test that the help menu displays all commands."""
    Calculator.display_help()

    captured = capsys.readouterr()

    assert "Available commands:" in captured.out
    assert "add" in captured.out
    assert "subtract" in captured.out
    assert "multiply" in captured.out
    assert "divide" in captured.out
    assert "history" in captured.out
    assert "help" in captured.out
    assert "exit" in captured.out


# ---------------------------------------------------------
# Calculator history tests
# ---------------------------------------------------------

def test_display_history_when_empty(capsys):
    """Test the message shown when calculation history is empty."""
    calculator = Calculator()

    calculator.display_history()

    captured = capsys.readouterr()

    assert "No calculations have been performed yet." in captured.out


def test_display_history_with_addition(capsys):
    """Test displaying an addition calculation."""
    calculator = Calculator()

    calculation = Calculation(10, 5, Operations.add)
    calculator.history.append(calculation)

    calculator.display_history()

    captured = capsys.readouterr()

    assert "Calculation History:" in captured.out
    assert "1. 10 + 5 = 15" in captured.out


def test_display_history_with_subtraction(capsys):
    """Test displaying a subtraction calculation."""
    calculator = Calculator()

    calculation = Calculation(10, 5, Operations.subtract)
    calculator.history.append(calculation)

    calculator.display_history()

    captured = capsys.readouterr()

    assert "1. 10 - 5 = 5" in captured.out


def test_display_history_with_multiplication(capsys):
    """Test displaying a multiplication calculation."""
    calculator = Calculator()

    calculation = Calculation(10, 5, Operations.multiply)
    calculator.history.append(calculation)

    calculator.display_history()

    captured = capsys.readouterr()

    assert "1. 10 * 5 = 50" in captured.out


def test_display_history_with_division(capsys):
    """Test displaying a division calculation."""
    calculator = Calculator()

    calculation = Calculation(10, 5, Operations.divide)
    calculator.history.append(calculation)

    calculator.display_history()

    captured = capsys.readouterr()

    assert "1. 10 / 5 = 2.0" in captured.out


# ---------------------------------------------------------
# Calculator operation-name tests
# ---------------------------------------------------------

@pytest.mark.parametrize(
    "operation, expected",
    [
        (Operations.add, "+"),
        (Operations.subtract, "-"),
        (Operations.multiply, "*"),
        (Operations.divide, "/"),
    ],
)
def test_get_operation_name(operation, expected):
    """Test that each operation gets the correct symbol."""
    calculation = Calculation(1, 2, operation)

    assert Calculator._get_operation_name(calculation) == expected


def test_get_operation_name_unknown_operation():
    """Test the fallback for an unknown operation."""

    def custom_operation(first, second):
        return first + second

    calculation = Calculation(1, 2, custom_operation)

    assert Calculator._get_operation_name(calculation) == "?"


# ---------------------------------------------------------
# Calculator input validation tests
# ---------------------------------------------------------

def test_get_number_with_valid_input():
    """Test that a valid number is accepted."""
    with patch(
        "builtins.input",
        return_value="5",
    ):
        result = Calculator.get_number("Enter number: ")

    assert result == 5.0


def test_get_number_handles_invalid_input():
    """Test invalid input followed by valid input."""
    with patch(
        "builtins.input",
        side_effect=["not a number", "5"],
    ):
        with patch("builtins.print") as mock_print:
            result = Calculator.get_number("Enter number: ")

    assert result == 5.0

    mock_print.assert_called_once_with(
        "Invalid number. Please enter a valid number."
    )


# ---------------------------------------------------------
# Calculator calculation tests
# ---------------------------------------------------------

def test_perform_calculation_success(capsys):
    """Test a successful calculation."""
    calculator = Calculator()

    with patch(
        "builtins.input",
        side_effect=["10", "5"],
    ):
        calculator.perform_calculation("add")

    assert len(calculator.history) == 1

    captured = capsys.readouterr()

    assert "Result: 15.0" in captured.out


def test_perform_calculation_division_by_zero(capsys):
    """Test division by zero handling."""
    calculator = Calculator()

    with patch(
        "builtins.input",
        side_effect=["10", "0"],
    ):
        calculator.perform_calculation("divide")

    assert len(calculator.history) == 0

    captured = capsys.readouterr()

    assert "Error: Cannot divide by zero." in captured.out


def test_perform_calculation_invalid_operation(capsys):
    """Test handling of an invalid operation."""
    calculator = Calculator()

    with patch(
        "builtins.input",
        side_effect=["10", "5"],
    ):
        calculator.perform_calculation("power")

    assert len(calculator.history) == 0

    captured = capsys.readouterr()

    assert "Error: Unsupported operation: power" in captured.out


# ---------------------------------------------------------
# Calculator REPL tests
# ---------------------------------------------------------

def test_run_help_history_and_exit(capsys):
    """Test help, history, and exit commands."""
    calculator = Calculator()

    with patch(
        "builtins.input",
        side_effect=[
            "help",
            "history",
            "exit",
        ],
    ):
        calculator.run()

    captured = capsys.readouterr()

    assert "Welcome to the Python Calculator!" in captured.out
    assert "Available commands:" in captured.out
    assert "No calculations have been performed yet." in captured.out
    assert "Goodbye!" in captured.out


def test_run_unknown_command(capsys):
    """Test handling of an unknown command."""
    calculator = Calculator()

    with patch(
        "builtins.input",
        side_effect=[
            "something",
            "exit",
        ],
    ):
        calculator.run()

    captured = capsys.readouterr()

    assert "Unknown command." in captured.out
    assert "Goodbye!" in captured.out


def test_run_calculation(capsys):
    """Test performing a calculation through the REPL."""
    calculator = Calculator()

    with patch(
        "builtins.input",
        side_effect=[
            "add",
            "10",
            "5",
            "exit",
        ],
    ):
        calculator.run()

    captured = capsys.readouterr()

    assert "Result: 15.0" in captured.out
    assert "Goodbye!" in captured.out
