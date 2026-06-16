
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

print(file.readline())