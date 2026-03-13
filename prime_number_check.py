"""
Prime Number Checker

A prime number is a number greater than 1 that has no divisors
other than 1 and itself.

This program checks whether a given number is prime.
"""

import math


def is_prime(number):
    """Return True if the number is prime, otherwise False."""

    if number < 2:
        return False

    # Check divisibility up to square root of the number
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


# Get input from the user
n = int(input("Enter a number to check: "))

# Check and print result
if is_prime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
