"""
Adjust explore_basement() to return its local address value, 
and use the return value so the last output of the program is "Mouse House" instead of "Python Palace". 

The global address line has been removed from explore_cabinet().

The program should output:

Cookie Cabinet
Mouse House
Mouse House

Requirements
Add a return statement at the end of explore_basement() to return address
Use the return value of explore_basement() in the last print() call
Keep the line address = "Python Palace" in your code
"""

def explore_basement():
    def explore_cabinet():
        """🐭"""
        address = "Cookie Cabinet"
        print(address)

    address = "Mouse House"
    explore_cabinet()
    print(address)
    return address


address = "Python Palace"
print(explore_basement())

"""
address = "Python Palace"
address = explore_basement()
print(address)
"""