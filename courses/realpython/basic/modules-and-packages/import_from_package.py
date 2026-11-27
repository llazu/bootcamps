"""
A package called texttools is available. It contains a module called formatting with two functions: 
bold(text) returns text wrapped in ** markers, and italic(text) returns text wrapped in * markers.

Write a function format_text() that imports and uses both functions from the package.

Examples
format_text("hello") => ('**hello**', '*hello*')
format_text("Python") => ('**Python**', '*Python*')

Requirements
Import bold and italic from texttools.formatting
Return a tuple of (bold version, italic version)
"""

# Import bold and italic from the texttools.formatting module below
from texttools.formatting import bold, italic

def format_text(text):
    """Return a tuple of (bold, italic) versions of text."""
    return (bold(text), italic(text))

print(format_text("Luigi"))