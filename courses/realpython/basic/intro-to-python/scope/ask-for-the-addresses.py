"""
You decide to throw a party with the mouse. Axer cleaning up all the
items that are lying around, you want to hang up some signs so the
guests can find their way into the mouse's cabinet.

Have a look at the program below. Can you guess how the output of the
program looks?
"""

def explore_basement():
    def explore_cabinet():
        """🐭"""
        address = "Cookie Cabinet"
        print(address)
    address = "Mouse House"
    explore_cabinet()
    print(address)

address = "Python Palace"
explore_basement()
print(address)

# "Cooking Cabinet" - address local scope
# "Mouse House" - address enclosing scope
#  Python Palace - global scope