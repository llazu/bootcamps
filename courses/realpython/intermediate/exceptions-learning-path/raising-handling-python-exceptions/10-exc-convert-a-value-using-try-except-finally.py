"""
Write a function convert_to_int() that takes a string value and 
attempts to convert it to an integer using a try/except/else/finally block. 
Print a status message from each block.

Examples
>>> convert_to_int("42")
ok
done
42
>>> convert_to_int("hello")
error
done

Requirements
Use all four keywords: try, except, else, and finally
Print "ok" in the else block and return the integer
Print "error" in the except block and return None
Print "done" in the finally block
"""

def convert_to_int(my_string):
    """Try to convert value to an int, printing the outcome."""
    try:
        my_int = int(my_string)
    except ValueError as e:
        print("error", e)
    else:
        print("ok")
        return my_int
    finally:
        print("done")

convert_to_int("Hello")
print("\n")
convert_to_int("11")