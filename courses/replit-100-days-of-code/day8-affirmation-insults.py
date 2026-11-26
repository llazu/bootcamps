"""
Exercise 8
Create a Custom Affirmation or Custom Insult Generator.

1. Ask the user for their name.
2. Then ask for follow-up, like what's the day of the week, favorite thing to do?
3. For the insult generated, say something comical, not disparaging.
4. Deal with both lower and capital first letter on the name.
"""

print("It's time to generate motivation!")
name = input("What is your name? ").lower().strip()
day = input("What is the day of the week? ").lower().strip()
favorite_thing = input("What is your favorite thing to do? ").lower().strip()
print("Hey " + name + ", " + day + " is a great day to " + favorite_thing + ".")

tracker = input("Hey " + name + ", did you do your " + favorite_thing + " today? ").lower().strip()

if tracker == "no":
    print("Don't overthink it! This is called inertia. Just do it!")

if tracker == "yes":
    input("How better is your mood after " + favorite_thing + "? ")
