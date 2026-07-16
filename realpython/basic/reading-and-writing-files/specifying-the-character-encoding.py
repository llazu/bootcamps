# convert to byte string literal
"cash".encode()

# numeric ASCII codes
print(list("cash".encode()))

# use bytes constructor to compute the inverse
print(bytes([99, 97, 115, 104]).decode())

# non english encoding
# if encoding not specified, python uses OS char encoding
# Therefore, always specify the character encoding
# If in doubt, use UTF-8 which has becoming a  widespread standard
print(bytes([99, 97, 102, 195, 169]).decode("utf-8"))

# when opening a file, tell python the file's encoding
# generates unicode error
# with open("italiano.text", encoding="ascii") as file:
    # file.read()

# could generate gardbage
with open("italiano.txt", encoding="iso-8859-2") as file:
    print(file.read())

# The library chardet can help you guess the encoding in a file

# encodings your python version supports

from encodings.aliases import aliases
print(set(aliases.values()))

# Unicode Encodings
for encoding in ("utf-8", "utf-16", "utf-32"):
    print (
        format(encoding, ">7"),
        list("😊".encode(encoding))
    )

# Always specify the encoding of a file
from pathlib import Path

path = Path("italiano.txt")

with path.open(mode="r", encoding="utf-8") as file:
    ...

# Avoid this common mistake
from pathlib import Path

path = Path("italiano.txt")

with path.open(mode='r') as file: # Missing encoding!
    ...