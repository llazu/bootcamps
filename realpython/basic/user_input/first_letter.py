''' 
Exercise: Pick Apart Your User's Input
1). Write a program that prompts the user for input with the string "Tell me your password: "
2). The program should then determine the first letter of the user's input, convert it to uppercase, and display it back.
3). Display back with string "The first letter you entered was: ?".
'''

password = input("What your password? ")

first_letter = password[0]

upper_case = first_letter.upper()

print("The first letter you entered was: {}".format(upper_case))