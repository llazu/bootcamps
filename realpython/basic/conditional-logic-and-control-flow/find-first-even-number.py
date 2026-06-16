"""
The starter code defines a list of numbers. 
Your job is to loop through them, find the first even number, print it, and stop the loop immediately using break.

After your edit, the program should print:
4

Requirements
Use a for loop to go through the numbers list
Use if with the % operator to check if a number is even
Print the first even number you find
Use break to stop the loop after printing
"""

numbers = [1, 3, 7, 4, 9, 2, 6]

for number in numbers:
    if number % 2 == 0:
        print(number)
        break