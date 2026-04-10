"""
Exercise: Adjust the Address
You want to invite other animals to the party.
However, "Python Palace" may sound a bit scary to other rodents.

Add one line to the function body of explore_cabinet() to set the
global address to "Cookie Cabinet".
"""

def explore_basement():
    def explore_cabinet():
        """🐭"""
        global address
        address = "Cookie Cabinet"
        print(address)
    address = "Mouse House"
    explore_cabinet()
    print(address)

address = "Python Palace"
explore_basement()
print(address)