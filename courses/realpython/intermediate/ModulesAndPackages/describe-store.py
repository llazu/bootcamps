"""
Write a function describe_store() that imports store and returns a dictionary with these keys:

result = describe_store()
result["store_name"] = 'Real Python Bookstore'
result["greeting"] = 'Welcome to Real Python Bookstore!'
result["num_books"] = 3
result["featured"] = 'Python Tricks: $29.95'

Requirements
Import the store module and use dot notation to access its attributes
"store_name": the name of the store
"greeting": the store's greeting message
"num_books": how many books are in the catalog
"featured": a summary of a Product with title "Python Tricks" and price 29.95
"""

import store

def describe_store():
    """Return a dict describing the store module."""
    ...
    my_dict = {}
    product = store.Product("Python Tricks", 29.95)
    my_dict.update({'store_name' : store.name})
    my_dict.update({'greeting' : store.get_greeting()})
    my_dict.update({'num_books' : len(store.catalog)})
    my_dict.update({'featured' : product.summary()})
    return my_dict

print(describe_store())