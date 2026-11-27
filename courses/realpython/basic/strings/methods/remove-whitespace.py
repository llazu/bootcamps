# Exercise: Remove Whitespace

# Write a program that removes whitespace from the
# following strings, then print out the strings with
# the whitespace removed:

string1 = "     Filet Mignon"
string2 = "Brisket     "
string3 = "   Cheeseburger   "

string1 = string1.lstrip()
print(string1)
string2 = string2.rstrip()
print(string2)
string3 = string3.strip()
print(string3)