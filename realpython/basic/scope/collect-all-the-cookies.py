"""
Add return statements to the on_the_shelf() and under_the_sofa() functions so they return their cookie lists. 

Then combine the results into the cookies variable so the program prints all four cookies.

The program should output:

['Peanut', 'Chocolate', 'Oat', 'Salted Caramel']

Requirements
Each function should return its local cookie variable
Combine the return values of both functions into the cookies variable
"""

def on_the_shelf():
    """Check the shelf for cookies."""
    shelf_cookies = ["Peanut", "Chocolate"]
    #cookies.append(shelf_cookies)
    return shelf_cookies    
    ...


def under_the_sofa():
    """Check under the sofa for cookies."""
    sofa_cookies = ["Oat", "Salted Caramel"]
    #cookies.append(sofa_cookies)
    return sofa_cookies
    ...

cookies = on_the_shelf() + under_the_sofa()
print(cookies)