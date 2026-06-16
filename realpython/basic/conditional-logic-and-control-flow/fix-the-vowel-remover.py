"""
The function remove_vowels() should take a string and return a new string with all vowels 
(a, e, i, o, u, both lowercase and uppercase) removed. However, it has a bug!

Find the bug and fix it so the function works correctly.
Examples
remove_vowels("hello") => 'hll'
remove_vowels("HELLO") => 'HLL'
remove_vowels("rhythm") => 'rhythm'
remove_vowels("aeiou") => ""
"""

def remove_vowels(text):
    """Remove all vowels from the text and return the result."""
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result