"""
In the program on the botton, you can find these variables and functions:

address
cabinet_items
basement_items
print()

From the perspective of the mouse in the cabinet, order them into the four
scopes:
1. Local
2. Enclosing
3. Global
4. Built-in
"""

def explore_basement():
    def explore_cabinet():
        """🐭"""
        cabinet_items = ["keys", "sunglasses"]
        print(f"{cabinet_items=} is in the local scope")
        print(cabinet_items)
    basement_items = ["bed", "cabinet"]
    print(f"{basement_items=} is in the enclosing scope")
    explore_cabinet()
    print(basement_items)

address = "Python Palace"
print(f"{address=} is in the global scope")

explore_basement()

print(address)
print({f"print(address) is in the builtin scope"})