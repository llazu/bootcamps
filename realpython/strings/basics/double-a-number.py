"""
In this exercise, you'll practice converting between strings and numbers.

The starter code uses input() to ask the user for a number. 
Remember that input() always returns a string, even if the user types a number. 
Your job is to convert that string to a number, double it, and print the result.

For example, if the user enters 5, your program should print:

10.0

If the user enters 3.5, your program should print:

7.0

Requirements

Convert the input to a number using float()
Multiply the number by 2
Print the result
"""

text = input("Enter a number: ")
result = float(text)*2
print(result)