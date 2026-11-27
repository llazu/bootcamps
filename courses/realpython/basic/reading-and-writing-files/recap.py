from pathlib import Path

# Reading Code
path = Path("latin.txt")
with path.open("r", encoding="utf-8") as f:
    # load all the content with read
    print(f.read())
    # provide the number of characters to use
    # reset file pointer
    f.seek(0)
    print(f.read(20))
    # Read file into a python list
    print(f.readlines())

# iterate over the lines
#with path.open(mode="r", encoding="r") as file:
    #for line in file:
        # print(line, end='') removes new line
        #print(line)

print("new with block")
with open("latin.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line)

# Using readline() for more control
print("Using readline():")
with open("latin.txt", "r", encoding="utf-8") as f:
    # Read first line
    first_line = f.readline()
    print(f"First line: {first_line.strip()}")
    
    # Read second line
    second_line = f.readline()
    print(f"Second line: {second_line.strip()}")
    
    # Read remaining lines
    remaining_lines = f.readlines()
    for line in remaining_lines:
        print(f"Remaining: {line.strip()}")

path = Path("new.txt")
with path.open(mode="w", encoding="utf-8") as file:
    file.write("I am tired\n")
    file.write("I feel like shit\n")
    file.writelines([
        "Give me your money\n",
        "What up my peoples!\n"
    ])
    print("Hello world", file=file)
