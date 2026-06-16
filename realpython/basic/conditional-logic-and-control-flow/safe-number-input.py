"""
The starter code asks the user for a number and doubles it. 
But if the user types something that isn't a number (like "hello"), 
the program crashes with a ValueError.

Your job is to wrap the conversion in a try/except block so the program prints a friendly message instead of crashing.

If the user enters 5, the program should print:
10.0
If the user enters hello, the program should print:
That's not a valid number.

Requirements
Use try and except ValueError to catch the error
If the input is valid, print the doubled number
If the input is invalid, print That's not a valid number.
"""

text = input("Enter a number: ")

# Add try/except to handle invalid input
try:
    number = float(text)
    print(number * 2)
except ValueError: 
    print("That's not a valid number.")