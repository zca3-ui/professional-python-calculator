"""Tests for arithmetic operations."""

import pytest

from app.operation.operations import Operations


@pytest.mark.parametrize(
    "first, second, expected",
    [
        (2, 3, 5),
        (0, 5, 5),
        (-2, 3, 1),
        (2.5, 2.5, 5),
    ],
)
def test_add(first, second, expected):
    """Test addition with multiple inputs."""
    assert Operations.add(first, second) == expected


@pytest.mark.parametrize(
    "first, second, expected",
    [
        (5, 3, 2),
        (0, 5, -5),
        (-2, -3, 1),
        (2.5, 1.5, 1),
    ],
)
def test_subtract(first, second, expected):
    """Test subtraction with multiple inputs."""
    assert Operations.subtract(first, second) == expected


@pytest.mark.parametrize(
    "first, second, expected",
    [
        (2, 3, 6),
        (0, 5, 0),
        (-2, 3, -6),
        (2.5, 2, 5),
    ],
)
def test_multiply(first, second, expected):
    """Test multiplication with multiple inputs."""
    assert Operations.multiply(first, second) == expected


@pytest.mark.parametrize(
    "first, second, expected",
    [
        (10, 2, 5),
        (9, 3, 3),
        (-10, 2, -5),
        (2.5, 0.5, 5),
    ],
)
def test_divide(first, second, expected):
    """Test division with multiple inputs."""
    assert Operations.divide(first, second) == expected


def test_divide_by_zero():
    """Test that division by zero raises an appropriate error."""
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero."):
        Operations.divide(10, 0)