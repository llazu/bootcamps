"""
Write a function total_spent(purchases, buyer) that calculates the total amount spent by a specific buyer from a list of purchases.

Use a pipeline of generator expressions to process the data lazily, without loading all intermediate results into memory at once.

Each purchase is a tuple of (buyer_name, amount).

Requirements
Filter purchases to only include those matching the specified buyer
Extract the amounts from the matching purchases
Return the sum of those amounts
Use generator expressions in the processing pipeline, not list comprehensions
"""
from functools import total_ordering

sample_purchase = [
    ("Alice", 120),
    ("Bob", 85),
    ("Alice", 45),
    ("Charlie", 200),
    ("Bob", 150),
]

def total_spent(purchases, buyer):
    """Calculate total spent by a buyer using a generator pipeline."""
    matching = (purchase for purchase in purchases if purchase[0] == buyer)
    amounts = (amount for name, amount in matching)
    return sum(amounts)

print("total spent: ", total_spent(sample_purchase, "Bob"))