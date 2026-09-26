# Mod4 Python Calculator

## Description



The calculator uses a Read-Eval-Print Loop (REPL) to allow users to continuously perform calculations during a session.

The app supports:

- Addition
- Subtraction
- Multiplication
- Division
- Calculation history
- Help commands
- Input validation
- Error handling
- Division-by-zero protection

## Project Structure

```text
app/
├── calculator/
│   ├── __init__.py
│   └── calculator.py
├── calculation/
│   ├── __init__.py
│   ├── calculation.py
│   └── factory.py
└── operation/
    ├── __init__.py
    └── operations.py

tests/
├── __init__.py
├── test_calculations.py
└── test_operations.py
