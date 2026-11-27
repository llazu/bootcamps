"""
Create a Car class with a constructor, an instance method, and two dunder methods.

Constructor
>>> car = Car("Aston Martin", "DB5", 1964)
.__init__() should store make, model, and year as instance attributes and set .mileage to 0.

Instance Method
.drive(miles) adds the given number of miles to the car's .mileage.

>>> car.drive(100)
>>> car.mileage
100
Dunder Methods
.__str__() returns a string in the format "year make model":

>>> print(car)
1964 Aston Martin DB5
.__eq__() returns True when two cars have the same make, model, and year. Mileage does not affect equality.

>>> car1 = Car("Aston Martin", "DB5", 1964)
>>> car2 = Car("Aston Martin", "DB5", 1964)
>>> car1 == car2
True

Requirements
.mileage starts at 0 and is not a constructor parameter
.drive() increases .mileage by the given amount
.__str__() returns a string in the exact format shown above
.__eq__() compares make, model, and year only
"""

class Car:
    """Represents a car with make, model, year, and mileage."""

    def __init__(self, make, model, year):
        """Store make, model, year and set mileage to zero."""
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0

    def drive(self, miles):
        """Add miles to the car's mileage."""
        self.mileage += miles

    def __str__(self):
        """Return a string like '1964 Aston Martin DB5'."""
        return f"{self.year} {self.make} {self.model}"

    def __eq__(self, other):
        """Two cars are equal if they share make, model, and year."""
        return (
            self.make == other.make and
            self.model == other.model and
            self.year == other.year
        )