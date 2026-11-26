# 1. Write a program that converts the following strings to lowercase
    # "Animals"
    # "Badger"
    # "Honey Bee"
    # "Honey Badger"

#2 Now convert each of these strings to uppercase instead of lowercase

Species = ["Animals", "Badger", "Honey Bee", "Honey Badger"]

for species in Species:
    print(species.lower())
    
for species in Species:
    print(species.upper())

# In the course, the instructor did not use list or for loops.

String1 = "Animals"
String2 = "Badger"
String3 = "Honey Bee"
String4 = "Honey Badger"

# Then a bunch of prints statements, manually typed

print(String1.lower())
# ...
# ...
# ...

# Once all the lowers are finished, then the uppers

print(String1.upper())
# ...
# ...
# ...