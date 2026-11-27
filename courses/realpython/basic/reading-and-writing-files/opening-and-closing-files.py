#open("filename.txt")

open("customers-100.csv")

file = open("customers-100.csv")
print(file) # print file wrapper

"""
Failing to close can lead to memory leaksm, Lock other promgrams 
from accessping the file until python is exited, or it could corrupt
your data by not flasing the internal buffer on time. 
"""

file.close() # closed the file

print(file.closed) # checks closed status



# with behind the scenes
file = None
try:
    file = open("customers-100.csv")
finally:
    if file:
        file.close()

# old skool way
# don't need to remember closing the file
# The drawback of open is that there no abstraction
# that accounts for OS differences in file path.
with open("customers-100.csv") as myFile:
    pass

# modern way
# path open methods doesn't need to provide a string
from pathlib import Path
path = Path("customers-100.csv")
with path.open() as myNewFile:
    pass