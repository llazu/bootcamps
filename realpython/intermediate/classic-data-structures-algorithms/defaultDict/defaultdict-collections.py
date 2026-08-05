# Handling Missings Keys: default dict
# Handling a Key that doesn't exist produces a KeyError

favorites = {
        "pet": "dog", 
        "color": "blue",
        "language": "Python"
}

# KeyError
# favorites["fruit"]

# setdefault assings a default value to the key
print(favorites)
favorites.setdefault("fruits", "apples")
print(favorites)

favorites.setdefault("pet", "cat")

#return the current value not the default
print(favorites)

# Using .get() to return a suitable value if the key is missing
favorites = {
    "pet": "dog",
    "color": "blue",
    "language" : "Python"
}

print(favorites.get("fruit", "apple"))

# .get doesn't add the key value pair
print(favorites)

#Use defaultdict to group 
from collections import defaultdict
pets = [
    ("dog", "Affenpincher"),
    ("dog", "Terrier"),
    ("dog", "Boxer"),
    ("cat", "Abyssinian"),
    ("cat", "Birmam")
]

# create an empty when key doesn't exist
group_pets = defaultdict(list)

for pet, breed in pets:
    group_pets[pet].append(breed)

print(group_pets)

for pet, breeds in group_pets.items():
    print(pet, "->", breeds)
