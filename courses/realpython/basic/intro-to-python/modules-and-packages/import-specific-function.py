"""
A module called converter is available with three functions: to_upper(text), to_lower(text), and to_title(text).

Write a function format_name() that uses selective imports to format a name in two ways.

Examples
format_name("alice smith") => ('ALICE SMITH', 'Alice Smith')
format_name("BOB JONES") => ('BOB JONES', 'Bob Jones')

Requirements
Use from converter import to import only to_upper and to_title
Call the imported functions directly (without a module prefix)
Return a tuple of (uppercase version, title case version
"""

# Import to_upper and to_title from the converter module below
from converter import to_upper, to_title

def format_name(name):
    """Return a tuple of (upper_case, title_case) versions of name."""
    upper_case = to_upper(name)
    title_case = to_title(name)
    return upper_case, title_case

print(format_name("luiyi"))