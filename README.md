# Week 6 Assignment

## Files
* safe_tools.py - Contains functions handling ZeroDivisionError, ValueError, and KeyError safely.
* unbreakable.py - Demonstration file.

## Concept Question
Why can the if check not catch abc on its own?
An if statement checks conditions but cannot intercept core data-type cast errors raised by the Python interpreter. A try/except block is required to catch the ValueError raised when converting non-numeric text like "abc" using int().
