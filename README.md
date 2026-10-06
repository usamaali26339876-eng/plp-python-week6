# Week 6 Assignment: Python Exception Handling

## File Descriptions
* **safe_tools.py**: A collection of robust utility functions utilizing try/except blocks to handle division by zero, type conversions, and missing dictionary keys without crashing.
* **unbreakable.py**: An optional script demonstrating structured exception handling techniques to maintain runtime continuity under unexpected conditions.

## Concept Questions
### Why can an `if` check not catch "abc" on its own?
An `if` statement can only test structural criteria that evaluate to a boolean truth value (such as checking if string content contains numbers). It cannot intercept low-level compiler failures or data-type initialization errors. A `try/except` block is explicitly necessary to catch a runtime `ValueError` when Python's parsing engine fails to cast arbitrary alphanumeric text like `"abc"` into an integer.
