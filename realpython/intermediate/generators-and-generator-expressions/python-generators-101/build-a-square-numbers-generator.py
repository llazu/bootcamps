"""
Write a generator function infinite_squares() that yields the squares of consecutive integers indefinitely, starting from 0.

The sequence should be: 0, 1, 4, 9, 16, 25, …

Requirements
The first yielded value should be 0 (which is 0 squared)
Each subsequent value should be the square of the next integer
The generator should produce values indefinitely without running out of memory
"""

from itertools import islice

def infinite_squares():
    """Yield squares of consecutive integers indefinitely."""
    num = 0
    while True:
        squared_num = (num ** 2)
        yield squared_num
        num += 1

squares_galore = infinite_squares()

# Method 1: islice — cleanest Pythonic way to take N items from an infinite generator
for squares in islice(squares_galore, 5):
    print(squares)

squares_galore = infinite_squares()

# Method 2: next() in a range loop — explicit, no imports needed beyond the generator
for _ in range(5):
    print(next(squares_galore))

squares_galore = infinite_squares()

# Method 3: enumerate with break — useful when you need the index too
for i, squares in enumerate(squares_galore):
    if i >= 5:
        break
    print(squares)

for square in squares_galore:
    print(square)