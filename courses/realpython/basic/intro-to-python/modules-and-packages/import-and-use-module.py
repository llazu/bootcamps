"""
A module called helpers is available with two functions: greet(name) returns a greeting and farewell(name) returns a farewell.

Write a function create_message() that imports and uses both functions to build a combined message.

Examples
create_message("Alice") => 'Hello, Alice! Goodbye, Alice!\'
create_message("Bob") => 'Hello, Bob! Goodbye, Bob!'

Requirements
Import the helpers module using import helpers
Use dot notation to call helpers.greet() and helpers.farewell()
Return a single string combining the greeting and farewell, separated by a space
"""

# Import the helpers module here
import helpers

# helpers.greet("Alice")
# helpers.farewell("Alice")

def create_message(name):
    return helpers.greet(name) + " " + helpers.farewell(name)

print(create_message("Alice"))