# subclassing dict to create a dict with all lowercase keys
class LowerDict(dict):
    def __setitem__(self, key, value):
        key = key.lower()
        super().__setitem__(key, value)


ordinals = LowerDict({"FIRST": 1, "SECOND": 2})

# works with this assignment
ordinals["THIRD"] = 3

# doesn't work with .update method
ordinals.update({"FOURTH": 4})

print(ordinals)

print(isinstance(ordinals, dict))

from collections import UserDict

class LowerDict(UserDict):
    def __setitem__(self, key, value):
        key = key.lower()
        super().__setitem__(key, value)

ordinals_new = LowerDict({"FIRST": 1, "SECOND": 2})
ordinals_new["THIRD"] = 3
ordinals_new.update({"FOURTH": 4})

print(ordinals_new)

print(isinstance(ordinals_new, dict))