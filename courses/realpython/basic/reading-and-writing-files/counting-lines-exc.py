"""
Write a function count_lines() that returns the number of lines in a text file.

Examples
Given a file with three lines of text:

count_lines("three_lines.txt")
outputs
3

Requirements
Open the file using the with statement
Use UTF-8 encoding
Return the total number of lines as an integer
"""


def count_lines(path):
    """Return the number of lines in a text file."""
    with open(path, "r", encoding="utf-8") as f:
        #lines = [line for line in f.readline()]
        #return len(lines)
        return len(f.readlines())

def count_lines_too(path):
    """Return the number of lines in a text file."""
    with open(path, "r", encoding="utf-8") as f:
        # remove whitespace \n new line character
        lines = [line.rstrip() for line in f]
        return len(lines)

#print(count_lines("customers-100.csv"))
print(count_lines_too("customers-100.csv"))