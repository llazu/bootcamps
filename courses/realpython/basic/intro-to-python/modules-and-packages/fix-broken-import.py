"""
The code below imports the helpers module but then calls its functions without the module prefix, causing a NameError.

Fix the function calls so they use the correct dot notation to match the import helpers statement.

The Bug => greeting = greet(name)
Traceback (most recent call last):
    ...
NamesError: name 'greet' is not defined
When you use import helpers, you must access its functions through the module name.

Requirements
Keep the import helpers statement at the top
Fix the function calls to use dot notation
"""
import helpers

def create_message(name):
    """Return a combined greeting and farewell message."""
    greeting = helpers.greet(name)
    farewell = helpers.farewell(name)
    return greeting + " " + farewell