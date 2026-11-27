"""
Exercise: Add a Main Module
Create a module called main.py that imports greet() from
greeter.py and calls the function with the argument "Real
Python" .
"""

from greeter import greet

# Call greet() directly without reassigning it to the name `greet`.
# Because greet() only prints and has no return statement, it returns None.
# Writing `greet = greet("Real Python")` would overwrite the imported function
# reference with None, causing a TypeError if greet() were called again.
greet("Real Python")
