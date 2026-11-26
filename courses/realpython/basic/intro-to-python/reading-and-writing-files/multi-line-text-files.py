# open the file
file = open("zen.txt", encoding="utf-8")

# first line from file
print("1st line: ", repr(file.readline()))

# iterate over the lines in the file
for line in file:
    print("Each line on the file", line)

# each line end in a \n
# start from the beginning
print(file.seek(0))
# fix having a new line between each line
print("remove new lines")
for line in file:
    print(line.rstrip())

# reset file
print(file.seek(0))

# overide \n for ""
for line in file:
    print(line, end="")

# if you don't mind reading the entire file
print(file.readlines())
# returns an empty list if all lines were read
# reset to beginning
print(file.seek(0))
# print entire file
print(file.readlines())
file.close()

# open another file, r+ is read & write mode
file = open("incremental.txt", mode="r+" ,encoding="utf-8")
print(file.tell())
# read entire file, return a list
print(file.readline())

# writing to the file
file.writelines(["\n", "the 3rd line\n", "the 4th line\n", "the 5th line"])
# reset file to beginning
print(file.seek(0))
# print file with new lines
print(file.readlines())

# using print instead
print("Thie is", file=file)
print("written by print()", file=file)
print(file.seek(0))

print(file.read())

