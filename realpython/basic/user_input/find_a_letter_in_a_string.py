'''
Exercise:Find a letter in a String
Write a program that accepts user input() and displays the
results of trying to find a particular letter in that input
using ".find()".
'''

#user_input = input("What is your name? ")
#name = user_input.find("a")
#print(name)

#turn the search letter into a user_input

user_input = input("What is your name? ")
user_char = input("What is your search character? ")
find_char = user_input.find(user_char)
print(find_char)