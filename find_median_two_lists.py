"""
Median of Two Lists in Python

This script demonstrates three different ways to calculate the median
of numbers from two lists:

1. Using a custom Python function
2. Using NumPy
3. Using the built-in statistics module

The median is the middle value of a sorted list of numbers.
If the number of values is even, the median is the average of
the two middle numbers.
"""

# ------------------------------
# Method 1: Using a Python Function
# ------------------------------

def median(list1, list2):
    """
    Calculate the median of two lists using pure Python.
    """

    # Combine the two lists
    combined = list1 + list2

    # Sort the combined list
    combined.sort()

    # Total number of elements
    n = len(combined)

    # If number of elements is odd
    if n % 2 != 0:
        return combined[n // 2]

    # If number of elements is even
    else:
        return (combined[n // 2 - 1] + combined[n // 2]) / 2


# Example lists
l1 = [2, 15, 4, 8, 9, 7, 12]
l2 = [1, 3, 7, 8, 6]

# Call the custom median function
print("Median using Python function:", median(l1, l2))


# ------------------------------
# Method 2: Using NumPy
# ------------------------------

import numpy as np

# Combine lists
l3 = l1 + l2

# Calculate median using NumPy
print("Median using NumPy:", np.median(l3))


# ------------------------------
# Method 3: Using Statistics Module
# ------------------------------

import statistics as st

# Calculate median using statistics module
print("Median using statistics module:", st.median(l3))
