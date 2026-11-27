'''
Exercise - 
1). Write a program that uses the input() twice to get two numbers from the user.
2). Multiply the numbers togeher and display the results. 
3). Print the string "The product of X and Y is Z". Where X and Y are integers and Z is a float.
'''

first_number = int(input("Provide your first number? "))

second_number = int(input("Provide your second number? "))

product = float(first_number * second_number)

print("The product of " + str(first_number) + " and " + str(second_number) + " is " + str(product))