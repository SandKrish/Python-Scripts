"""
FizzBuzz Program in Python

This program prints numbers from 1 to 100.

Rules:
1. If the number is divisible by 3, print "Fizz".
2. If the number is divisible by 5, print "Buzz".
3. If the number is divisible by both 3 and 5, print "FizzBuzz".
4. Otherwise, print the number itself.

FizzBuzz is a common programming exercise used in coding interviews
to test basic logic and control flow.
"""

# Loop through numbers from 1 to 100
for i in range(1, 101):

    # If number is divisible by both 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    # If number is divisible by 3
    elif i % 3 == 0:
        print("Fizz")

    # If number is divisible by 5
    elif i % 5 == 0:
        print("Buzz")

    # Otherwise print the number
    else:
        print(i)
