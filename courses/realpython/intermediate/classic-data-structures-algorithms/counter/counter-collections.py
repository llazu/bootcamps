# counting the letters in mississipi

word = "mississippi"
counter = {}

for letter in word:
    if letter not in counter:
        counter[letter] = 0
    counter[letter] += 1

print(counter)

# defaultdict objects are convenient for counting
# because you don't have check if the key exist
from collections import defaultdict

counter = defaultdict(int)

for letter in "mississippi":
    # print(counter)
    counter[letter] += 1

print(counter)

from collections import Counter

letters = Counter("mississippi")

print("letters", letters)

# There are many ways to instantiate counter
# you can use list, tuples, or any iterable
# The object must be hashable (immu

# integer objects are hashable
print(Counter([1, 1, 2, 3, 3, 3, 4]))

# fails because list objects are unhashable
# print(Counter(([1], [1])))

# Update the counts of m and i
letters.update(m=3, i=4)
print(letters)

# Add a new key-count pair
letters.update({"a":2})
print(letters)

# Update with another counter
letters.update(Counter(["s", "s", "p"]))
print(letters)

# missing keys return 0
letters = Counter("mississippi")
print(letters["a"])

multiset = Counter([1, 1, 2, 3, 3, 3, 4, 4])
print(multiset)

print(multiset.keys() == {1, 2, 3, 4})

