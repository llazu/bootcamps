# maintaining Two Lists

from os import access
acronyms = ["Lol", "IDK", "TBH"]
translations = ["laugh out loud", "I don't know", "to be honest"]

# downside need to maintain both lists

del acronyms[0]
del translations[0]

print(acronyms)
print(translations)

# A Dictionary Maps Keys to Values

acronyms = {
    "LOL": "laugh out loud",
    "IDK": "I don't know",
    "TBH": "to be honest"    
}

print(acronyms["LOL"]) # use the key not the index

# Dictionaries Can Hold Anything
# like acronyms above which hold strings

# Dictionaries of strings to numbers
menu = {"Soup": 5, "Salad": 6}

# Dictionary of anything
my_dict = {10: 'helo', 2: 6.5}

# Creating a Dictionary and Adding Values
acronyms = {} # Creates an empty dictionary

acronyms["LOL"] = "laugh out loud" # add the key/value pair
acronyms["IDK"] = "I don't know" # add more items
acronyms["TBH"] = "to be honest" # add more items

print(acronyms)

# Updating Values in our Dictionary

acronyms["TBH"] = "honestly"

print(acronyms["TBH"])

# Removing Dictionary items
del acronyms["LOL"]

print(acronyms)

# Getting an Item That's NOT in the Dictionary

try: 
    definition = acronyms["BTW"] # returns None if key doesn't exist
except KeyError as e:
    print(e)
    print(f"the key {e} does not exists in the dictionary.")

print(acronyms)

# None Type
# None means the absence of a value, and values to False in a conditional

# Avoid the key error by using .get methods
definition = acronyms.get("BTW")

if definition:
    print(definition)
else:
    print("Key doesn't esist")

# Using a Dictionary to Translate a Sentence
acronyms = {
    "LOL": "laugh out loud",
    "IDK": "I don't know",
    "TBH": "to be honest"    
}

sentence = "IDK" + " what happened " + "TBH"
translation = acronyms.get("IDK") + " what happened " + acronyms.get("TBH")

print("sentence", sentence)
print("translation:", translation)