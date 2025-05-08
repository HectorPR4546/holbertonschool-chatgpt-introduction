#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.

    Parameters:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of n.

    Raises:
        ValueError: If n is negative.
    """
    if n == 0:
        return 1
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
        f = factorial(n)
        print(f)
    except IndexError:
        print(f"Usage: {sys.argv[0]} <non-negative integer>")
        sys.exit(1)
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)
