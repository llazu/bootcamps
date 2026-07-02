"""

The namedtuple is a factory function that creates tuple subclasses with named fields.
These fields give you direct access to the values in a given named tuple using the dot notation, like in obj.attr.

"""
# regular tuple
result = divmod(12, 5)
print(result)
# it not clear what result[0] and result[1] values are. 

# using namedtuple
from collections import namedtuple

def custom_divmod(x, y):
    DivMod = namedtuple("DivMod", "quotient remainder")
    return DivMod(*divmod(x, y))

# * is the unpacking operator

new_result = custom_divmod(12, 5)
print(new_result)

print("quotient: ", new_result.quotient)
print("remainder: ", new_result.remainder)

# create a new subclass using namedtuple()

# Use a list of strings as field names
Point = namedtuple("Point", ["x", "y"])
point = Point(2, 4)
print("point:", point)

## Access the coordinates
print("x:", point.x)

print("y:", point.y)

print("x:", point[0])

# Use a generator expression as field names
print(list((field for field in "xy")))

Point = namedtuple("Point", (field for field in "xy"))
print(Point(2,4))

# Use a string with comman-separated field names
Point = namedtuple("Point", "x, y")
print(Point(2, 4))

# Use a string with space-separated field names
Point = namedtuple("Point", "x y")
print(Point(2,4))

# Define default values for fields
Person = namedtuple("Person", "name job", defaults=["Python Developer"])
person = Person("Jane")
print(person)

# Create a dictionary from a named tuple
print(person._asdict())

# Replace the value of a field
person = person._replace(job="Web Developer")
print(person)