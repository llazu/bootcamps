"""
Write a function safe_divide() that takes two numbers and returns the result of dividing the first by the second.

Use a try/except block to handle the case where the second number is zero. 

If division by zero occurs, return the string "Cannot divide by zero" instead of crashing.

Examples
safe_divide(10, 2) -> 5.0
safe_divide(7, 3) -> 2.3333333333333335
safe_divide(0, 5) -> 0.0
safe_divide(10, 0)-> 'Cannot divide by zero'

Requirements
Return the division result on success
Use a try/except block to catch the appropriate exception
Return the exact string "Cannot divide by zero" when dividing by 
"""

def safe_divide(dividend, divisor):
    try:
        result = dividend/divisor
    except ZeroDivisionError as e:
        result = "Cannot divide by zero"
    return result

print(safe_divide(10, 2))
print(safe_divide(7, 3))
print(safe_divide(0, 5))
print(safe_divide(10, 0))

