
# ord returns character ordinal value
ord('c')
print(ord("c"))

# chr returns the character
chr(99)
print(chr(99))

# text mode
file = open("customers-100.csv")

for character in file.read():
    print(character)

# read entire file
print(file.readline())

# binary mode
for byte in file.read():
    print(byte)

 # By default, the file mode for open is text

from pathlib import Path

path = Path("customers-100.csv")
with path.open(mode="rb") as file: # or rt ot r for text mode
    print(file.mode)
    print(file.readable)
    print(file.writable)

# Potential Problems in Text Mode
# Character encoding(ASCII, UTF-8, UTF-16)
# Line Ending  (CR, LF, CRLF)