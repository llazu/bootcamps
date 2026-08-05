from string import templatelib
from collections import ChainMap

cmd_proxy = {} # The user doesn't provide a proxy
local_proxy = {"proxy": "proxy.local.com"}
global_proxy = {"proxy" : "proxy.global.com"}

config = ChainMap(cmd_proxy, local_proxy, global_proxy)
print(config["proxy"])

numbers = {"one": 1, "two": 2}
letters = {"a": "A", "b": "B"}

alpha_nums = ChainMap(numbers, letters)
# the .maps gives an internal list of the maps
print(alpha_nums.maps)

# we have the .new_child() and .parents method
dad = {"name": "John", "age": 35}
mom = {"name": "Jane", "age": 31 }

family = ChainMap(mom, dad)
print(family)

son = {"name": "Mike", "age": 0}
family = family.new_child(son)
print("adding son", family)

for person in family.maps:
    print(person)

print(family.parents)

# mutating operations
number = {"one": 1, "two": 2}
letters = {"a": "A", "b": "B"}

alpha_nums = ChainMap(numbers, letters)
print(alpha_nums)

# Add a new key-pair value
alpha_nums["c"] = "C"
print(alpha_nums)

# Pop a key that exists in the first dictionary
alpha_nums.pop("two")
print(alpha_nums)

# Delete keys that don't exist in the first
# dict but do in others
try:
    del alpha_nums["a"]
except:
    pass

# Clear the dictionary
alpha_nums.clear()
print(alpha_nums)

# These examples show the mutating operations on a ChainMap
# Object only affect the first mapping in the internal list
# This is an important detail to consider when you're working
# with ChainMap

