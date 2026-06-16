#open("filename.txt")

open("customers-100.csv")

file = open("customers-100.csv")
print(file) # print file wrapper

file.close() # closed the file

print(file.closed) # checks closed status

# with behind the scenes
file = None
try:
    file = open("customers-100.csv")
finally:
    if file:
        file.close()

#old skool way
with open("customers-100.csv") as myFile:
    pass

#modern way
from pathlib import Path
path = Path("customers-100.csv")
with path.open() as myNewFile:
    pass