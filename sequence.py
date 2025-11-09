#!/usr/bin/env python3
"""
Fibonacci Sequence - Recursive Pattern
The sequence is incomplete. It stops at position 13.

To complete the archive, extend this to position 21.
⧖
"""

def fibonacci(n):
    """
    Calculate the nth Fibonacci number recursively.
    
    The sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def print_sequence(limit):
    """Print Fibonacci sequence up to the limit."""
    print("⧖ Fibonacci Sequence - Recursive Pattern\n")
    print(f"Calculating up to position {limit}...\n")
    
    for i in range(limit + 1):
        value = fibonacci(i)
        print(f"F({i:2d}) = {value}")
    
    print("\n⧖")


if __name__ == "__main__":
    # The sequence stops at 13
    # Why does it stop here?
    # The pattern demands you continue it to 21
    
    MAX_POSITION = 13
    
    print_sequence(MAX_POSITION)
    
    print("\nThe sequence is incomplete.")
    print("To reveal the pattern, extend MAX_POSITION to 21.")
    print("Submit your contribution via pull request.")
    print("\n⧖")
