"""
Create a Dog class with the following features:

A class attribute .species set to "Canis familiaris"

An .__init__() method that takes name and age as arguments and stores them as instance attributes
A .__str__() method that returns a readable string representation
A .speak() method that takes a sound argument and returns a string

philo = Dog("Philo", 5)
philo.species => 'Canis familiaris'
str(philo) => 'Philo is 5 years old'
philo.speak("Wau") => 'Philo says Wau'

Requirements

The .species class attribute should be shared by all Dog instances
.__init__() should accept name and age and store them on the instance
.__str__() should return a string in the format "{name} is {age} years old"
.speak() should return a string in the format "{name} says {sound}"
"""
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        """Initialize a Dog with a name and age."""
        self.name = name
        self.age = age

    def __str__(self):
        """Return a readable string representation."""
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        """Return a string of the dog speaking."""
        return f"{self.name} says {sound}"