# Exercise 1: Count the letters in the word "mississippi" using a standard dictionary.
# Initialize an empty dictionary, iterate through the letters, check if they exist,
# increment their count, and print the resulting dictionary.
from collections import abc
word = "mississippi"
# TODO: Write your code here
counter = {}
for letter in word:
    if letter not in counter: # study
        counter[letter] = 0
    counter[letter] += 1

print("counter", counter)


# Exercise 2: Count the letters in the word "mississippi" using collections.defaultdict.
# Import defaultdict, initialize a defaultdict with integer defaults, iterate,
# update the counts, and print the result.
# TODO: Write your code here

from collections import defaultdict

new_counter = defaultdict(int)

for letter in word:
    new_counter[letter] += 1

print(new_counter)
# Exercise 3: Count the letters in the word "mississippi" using collections.Counter.
# Import Counter, instantiate it directly with the word, and print the counter.
# TODO: Write your code here
from collections import Counter

next_counter = Counter(word)

print(next_counter)


# Exercise 4: Instantiate a Counter with a list of integers [1, 1, 2, 3, 3, 3, 4].
# Verify how it counts elements in an iterable.
# TODO: Write your code here
after_next_counter = Counter([1, 1, 2, 3, 3, 3, 4])

print(after_next_counter)


# Exercise 5: Test what happens when you try to instantiate a Counter with a tuple of unhashable objects.
# For example, attempt Counter(([1], [1])) inside a try-except block to handle and print the TypeError.
# TODO: Write your code here
print(Counter[(1, 1)])

try:
    print(Counter([1], [1]))
except:
    print("Counter has unhashable objects")


# Exercise 6: Update the Counter from Exercise 3:
# 1. Update the counts of 'm' by 3 and 'i' by 4 using keyword arguments (.update()).
# 2. Add or update key-count pairs using a dictionary (e.g., {"a": 2}).
# 3. Update the counter with another Counter or iterable (e.g., ["s", "s", "p"]).
# Print the counter after each update.
# TODO: Write your code here
next_counter.update(m=3, i=4)
print(next_counter)


# Exercise 7: Check behavior of missing keys in a Counter.
# Define a Counter with "mississippi" and access a key that does not exist (like "a").
# Verify and print the result to show what Counter returns for missing keys.
# TODO: Write your code here
add_obj_counter = Counter("mississippi")
add_obj_counter.update({"a": 2})
print(add_obj_counter)

# Exercise 8: Create a multiset Counter from [1, 1, 2, 3, 3, 3, 4, 4].
# Access its keys and check if they are equal to the set {1, 2, 3, 4}.
# TODO: Write your code here
final_counter = Counter([1, 1, 2, 3, 3, 3, 4, 4])
print(final_counter)

print(final_counter.keys() == [1, 2, 3, 4])