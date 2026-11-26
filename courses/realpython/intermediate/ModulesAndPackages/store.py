name = "Real Python Bookstore"
catalog = ["Python Basics", "Python Tricks", "CPython Internals"]

def get_greeting():
    return f"Welcome to {name}!"

class Product:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def summary(self):
        return f"{self.title}: ${self.price:.2f}"