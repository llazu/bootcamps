"""
In this exercise, you'll practice using f-strings to build a formatted message from variables.

The starter code defines an item and a price. 
Your job is to use an f-string to print a message that includes both values.

After your edit, the program should print:

The coffee costs $4.99.

Requirements

Use an f-string (a string prefixed with f) to build the message
Include both item and price inside the f-string using {}
The output must match the format exactly: The <item> costs $<price>.
"""

item = "coffee"
price = 4.99
print(f"The {item} costs ${price}.")
