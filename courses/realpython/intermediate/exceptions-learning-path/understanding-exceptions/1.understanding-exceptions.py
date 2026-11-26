"""
Notes:
1. exceptions are mainly used for error handling
2. Also used for stop iteration and deprecation warnings
3. Styles for error handling
    A: Look Before You LEAP (LBYL). A piece of code returns
       a value indicationg its success or failure. It's the devs
       job to check it against errors (not how it will continue working).
    B: Easier to Ask Forgiveness than Permission (EAFP)
       You write a piece of code, let it run, if something goes wrong
       the language invokes the associated error. This is achieved through
       Try/Except statements. This allows you to associate multiple lines
       together and not have to worry about checking every single line.
4. Many languages use "throw" and "catch" for exceptions, but Python uses
   "raises" and "handles" exceptions. 
"""

names = ["Sue", "Jaspreet", "Alex"]
# using the sequence notation
# python is "0" indexed -> the 0 index is the 1st item
names[2] 

# IndexError - built into the standard exception library
# Traceback gives you what part of the code is causing an error who caused it
#name[3]

# Time to handle the error
try:
    names[3]
except IndexError as e:
    print("Your list doesn't have that index")
    
# raise IndexError()

# raise Exception("don't do that Dave")

error = Exception("don't", "do", "that", "Dave", 42)

print(error.args)

# raise error

# finally, run close even if an exception is raise
try:
    print("before rise")
    raise TypeError()
    print("don't go here")
except:
    print(("in handler"))
finally:
    print("always gets called")