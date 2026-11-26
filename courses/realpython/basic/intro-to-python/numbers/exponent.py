'''
Write a program that receives two numbers from the user and displays the first number raised to the power of the second number.

Your program should prompt the user for a base and an exponent, then print the result.

For example, if the user enters 1.2 and 3:

Enter a base: 1.2
Enter an exponent: 3
1.2 to the power of 3.0 = 1.7279999999999998
Requirements
Use input() to get the base and exponent from the user
Convert both inputs to floats before calculating
Raise the base to the power of the exponent using **
Print the result using an f-string
'''

first_number = float(input("Enter your first number? "))
second_number = float(input("Enter your second number? "))

result = first_number ** second_number

print(f"The result of {first_number} raised to the {second_number} is {result}")