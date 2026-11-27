"""
Complete the .area() method in the Rectangle class so that it returns the area of the rectangle.

The .__init__() constructor is already implemented for you. 
Your job is to write the .area() instance method.

Examples
rect = Rectangle(3, 4)
rect.area() => 12
Rectangle(5, 5).area() => 25
Rectangle(1, 10).area() => 10

Requirements
.area() must return the area (width multiplied by height)
Use the instance attributes self.width and self.height inside the method
"""

class Rectangle:
    """A rectangle with a width and height."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height