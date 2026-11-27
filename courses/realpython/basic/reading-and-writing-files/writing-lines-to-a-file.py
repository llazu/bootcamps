"""
Write a function write_lines() that writes a list of 
strings to a text file, one string per line.

Examples
>>> write_lines("output.txt", ["hello", "world"])
After calling the function, output.txt contains:

hello
world
Requirements
Open the file in write mode using the with statement
Use UTF-8 encoding
Each string should appear on its own line (add a newline after each)
"""

def write_lines(path, lines):
    """Write each string in lines to the file, one per line."""
    with open(path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

write_lines("output.txt", ["What up, bro?", "How you doing", "Que lo que mi hermano!"])