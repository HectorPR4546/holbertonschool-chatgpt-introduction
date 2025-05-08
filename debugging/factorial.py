#!/usr/bin/python3
import sys

def factorial(n):
    # Handle edge case: 0! is defined as 1
    if n == 0:
        return 1
    # Handle edge case: negative numbers don't have a factorial
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    result = 1
    while n > 1:
        result *= n
        n -= 1  # decrement n to avoid infinite loop
    return result

# Convert input argument to integer
# Note: For robustness, you could wrap this in a try/except block,
# but since the task doesn't require input validation, we'll keep it minimal.
f = factorial(int(sys.argv[1]))
print(f)
