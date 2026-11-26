'''
1. a) Create a "float" object named "weight" with value 0.2.
1. b) Create a string object named "animal" with value "newt".
2. c) The use these objects to print the following string using only string concatenation:

    "0.2 kg is the weight of the newt."

2. Display the same string by using ".format()" and empty {} placeholders.

3. Display the same string using f-string.

'''

#Exercise 1

#1. a)
weight = 0.2

#1. b)
animal = "newt"

#1. c)
animal_weight_str = str(weight) + " is kg the weight of the " + str(animal) + "."
print(animal_weight_str)

#Exercise 2

animal_weight_str = "{} is kg the weight of the {}.".format(weight, animal)
print(animal_weight_str)

#Exercise 3
animal_weight_str = f"{weight} is the kg weight of the {animal}."
print(animal_weight_str)