'''
Write a program that asks the user to input a number and then displays that number rounded to two decimal places.

For example, if the user enters 5.432:

Enter a number: 5.432
5.432 rounded to 2 decimal places is 5.43

Requirements
Use input() to get a number from the user
Convert the input to a float
Use the built-in round() function to round to two decimal places
Print the result in the format shown above
'''

number = float(input("Please provide a fractional number: "))

rounded_number = round(number, 2)

print(f"{number} rounded to 2 decimal places is {rounded_number}")