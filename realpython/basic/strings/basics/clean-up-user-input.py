"""
In this exercise, you'll practice using string methods to clean up messy text.

The starter code defines a variable raw_input that holds a string with extra spaces and inconsistent capitalization. 
Your job is to clean it up by removing the leading and trailing whitespace and converting the text to all lowercase.

After your edit, the program should print:

hello, python!

Requirements
Use .strip() to remove the whitespace from both ends
Use .lower() to convert the text to lowercase
Print the cleaned-up result
"""

raw_input = "   Hello, PYTHON!   "
cleaned = raw_input.strip().lower()
print(cleaned)