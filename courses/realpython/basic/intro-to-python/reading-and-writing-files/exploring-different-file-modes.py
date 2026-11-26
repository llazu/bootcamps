# python uses the text and read-only mode by default
from pathlib import Path

path = Path("filename.txt")

with path.open(encoding="utf-8") as file:
    print(file.mode)

"""
# Use the mode argument with desired letter code
path.open(encoding="utf-8", mode="r+")
# the tex mode t is implied
path.open(encoding="utf-8", mode="rt+")
"""

"""
r = read only
r+ - read and write
w - write-only
w+ - write and read
a - append-only
a+ - append and read
x - exclusive create
if the file doesn't exist, x will create one
and open it in write mode.
if the file exist, x mode provides an error.
"""