"""
You write JSON with python using json.dump() to serialize
data to a file.

The JSON standard doesn't allow for comments, trailing commas,
or single quotes for strings.

serialization convert data to json
deserilization convert json to data
"""

# JSON is text based
{
    "greetings" : "Hello, World!"
}

# convert python dictionary to json
# dumps gives you a python string, not a json object
import json
food_rating = {"organic dog food": 2, "human food": 10}
food_rating_json = json.dumps(food_rating)
print(food_rating_json)

# The result is similar to using str
food_rating_string = str(food_rating)
print(food_rating_string)


# values do not translate directly into json
number_present = {1: True, 2: True, 3: False}
number_present_json = json.dumps(number_present)

print(number_present_json)

# keys are always converted to strings in json
dog_id = 1
dog_name = "Friends"
dog_registry = {dog_id: {"name": dog_name}}
dog_registry_json = json.dumps(dog_registry)
print(dog_registry_json)

"""
Python to JSON mapping

dict => object
list => array
tuple => array
str => string
int => number
float => number
True => true
False => false
None => null

tuples and list serialize to an array.
This is problematic when deserializing the data.
"""

# convert types to json with dumps
true_json = json.dumps(True)
print(true_json)

list_json = ["eating", "sleeping", "barking"]
print(list_json)

"""
For dictionaries, keys must me hashalble.
Therefore, list, dictionaries, and sets cannot
be used as keys in a dictionary.
Despite a tupel being hashable (immutable), it will 
generate an error when converted to JSON.
"""

available_nums = {(1,2): True, 3:False}
# json.dumps(available_nums)

"""
skipkeys skips any key that would generate a type error. 
"""

available_nums_json = json.dumps(available_nums, skipkeys=True)
print(available_nums_json)

"""
sort_keys allows for sorting the keys alphabetically
"""
toy_condition = {"chew bone": 7, "ball": 3, "sock": -1}
toy_condition_json = json.dumps(toy_condition, sort_keys=True)
print(toy_condition_json)