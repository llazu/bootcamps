"""
Write a function read_file() that reads and returns 
the entire contents of a text file.
"""

def read_file(path):
    file = open(path, encoding="utf-8")
    return file.read()

