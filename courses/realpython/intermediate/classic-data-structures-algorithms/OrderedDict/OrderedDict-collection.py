from collections import OrderedDict

# creates an empty OrderDict
life_stages = OrderedDict()

# add values the same way regular dict does
# but ensures the orde of addition is preserved

life_stages["childhood"] = "0-9"
life_stages["adolescence"] = "9-18"
life_stages["adulthood"] = "18-65"
life_stages["old"] = "+65"

for stage, years in life_stages.items():
    print(stage, "->", years)

"""
What's the point of OrderedDict?

1. Intent communication
You're communicating that your code relies on order.
2. Control over the order of items
.move_to_end allows you to manipulate the order
.popitem() allows you to remove from either end
3. Equalituy test behavior
OrderedDicts are only equal if the have the same
content AND order.
"""

letters = OrderedDict(b=2, d=4, a=1, c=3)
print(letters)

# Move b to the right end
letters.move_to_end("b")
print(letters)

# Move b to the left end
letters.move_to_end("b", last=False)
print(letters)

print(sorted(letters))

# Sort letters by key
for key in sorted(letters):
    print(key)
    letters.move_to_end(key)

print(letters)

# Regular dictionaries compare the content only
letters_0 = dict(a=1, b=2, c=3, d=4)
letters_1 = dict(b=2, a=1, d=4, c=3)
print(letters_0 == letters_1)

# Ordered dictionaries compare content and order
letters_0 = OrderedDict(a=1, b=2, c=3, d=4)
letters_1 = OrderedDict(b=2, a=1, d=4, c=3)
print(letters_0)
print(letters_1)
print(letters_0 == letters_1)

letters_2 = OrderedDict(a=1, b=2, c=3, d=4)
print(letters_0 == letters_2)