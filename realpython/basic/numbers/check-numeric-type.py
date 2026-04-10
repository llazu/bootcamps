'''
exercise: check numeric type

Write a program that asks the user to input two numbers, 
then displays whether the difference between those two numbers is an integer.

For example, if the user enters 1.5 and .5:

Enter a number: 1.5
Enter another number: .5
The difference between 1.5 and 0.5 is an integer? True!
If the difference is not a whole number:

Enter a number: 1.5
Enter another number: 1.0
The difference between 1.5 and 1.0 is an integer? False!

Requirements
Use input() twice to get two numbers from the user
Convert both inputs to floats
Calculate the difference between the first and second number
Use the .is_integer() method on the difference to check if it is a whole number
Print the result in the format shown above
'''

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

diff = abs(num2 - num1)

if diff.is_integer():
    print(f"The difference betwewn {num1} and {num2} is an integer? {diff.is_integer()}")
else:
    print(f"The difference betwewn {num1} and {num2} is an integer? {diff.is_integer()}")
