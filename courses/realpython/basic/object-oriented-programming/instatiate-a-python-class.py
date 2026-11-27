"""
Write a function make_dog() that creates and returns a new instance of the Dog class.

The Dog class is already defined for you. 
Your job is to create an instance by calling the class and return it.

Example
>>> dog = make_dog()
>>> type(dog)
<class 'Dog'>
Each call to make_dog() should produce a new, independent Dog object.

Requirements
Create a new Dog instance by calling the class with parentheses
Return the new instance from the function
Each call should create a separate object
"""

class Dog:
    pass


def make_dog():
    """Create and return a new Dog instance."""
    return Dog()

bubba = Dog()
bubba_clone = make_dog()