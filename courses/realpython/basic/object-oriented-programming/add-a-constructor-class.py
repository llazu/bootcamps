"""
Add a Constructor to a Class
Coding Exercise 

Complete the Book class by filling in the .__init__() constructor 
so that it stores the title and author as instance attributes.

Examples
book = Book("1984", "George Orwell")
book.title => '1984'
book.author => 'George Orwell'

Requirements
Store title as an instance attribute called .title
Store author as an instance attribute called .author
"""

class Book:
    """A book with a title and an author."""

    def __init__(self, title, author):
        """Store the title and author as instance attributes."""
        self.title = title
        self.author = author