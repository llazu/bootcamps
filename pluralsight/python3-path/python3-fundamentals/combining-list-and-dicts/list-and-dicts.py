# Breakfast, Lunch, and Dinner Lists
# Let's say we have three separate menu lists
# Breakfast, Lunch, Dinner

breakfast = ["Egg Sandwich", "Bagel", "Coffee"]
lunch = ["BLT", "PB&J", "Turkey Sandwich"]
dinner = ["Soup", "Salad", "Spaghetti", "Taco"]

# How would you combine into one list?
# You can have a container of containers

menus = [
    ["Egg Sandwich", "Bagel", "Coffee"],
    ["BLT", "PB&J", "Turkey Sandwich"],
    ["Soup", "Salad", "Spaghetti", "Taco"]
]

# Use indeces to print each menu
print("Breakfast Menu:\t", menus[0])
print("Lunch Menu:\t", menus[1])
print("Dinner Menu:\t", menus[2])

# How to access an individual item within a list?

# prints Bagel
print(menus[0][1])

# Instead of using a list of Lists, we can use a dictionary.

new_menus = {
    "breakfast" : ["Egg Sandwich", "Bagel", "Coffee"],
    "lunch" : ["BLT", "PB&J", "Turkey Sandwich"],
    "dinner" : ["Soup", "Salad", "Spaghetti", "Taco"]
}

# Use Keys to print each menu
print("Breakfast Menu:\t", new_menus["breakfast"])
print("Lunch Menu:\t", new_menus["lunch"])
print("Dinner Menu:\t", new_menus["dinner"])

# for loops just prints the keys in a dict
# Use .items to get keys and values
for name, menu in new_menus.items():
    print(name, ":", menu)

# We can use dictionary to represent objects
# The attributes are saved a key/value pairs
person = {
    "name": "Sara Smith",
    "city": "Orlando",
    "age": "100"
}

print(person.get('name'), "is", person.get('age'), "years old.")