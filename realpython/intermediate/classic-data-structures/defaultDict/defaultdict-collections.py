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