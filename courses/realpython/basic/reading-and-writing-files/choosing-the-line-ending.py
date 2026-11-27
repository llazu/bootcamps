# learn where and how to choose the line ending
# You can read the chars a few at a time
# All at once, or line by line

# Each line is terminated by an 
# invisible newline character

# you don't see the invisible line ending, 
# but it counts towards the character length
line = 'Lorem ipsum dolor sit amet, consectetur\n'

print(line)

# remove the invisible line ending
# not removing is a common mistake
line.rstrip()

print(line)

# Major Line Endings
# Carriage Return (CR) - mac - \r
# Line Feed (LF) - mac, linux - \n
# (CR+LF) - windows - \r\n

chr(13) # CR
# '\r'
chr(10) # LF
# '\n'

# Python's Universal Newline
# Python translate platform specific line
# endings to \n when reading
from pathlib import Path
path = Path('filename.txt')
with path.open(
    mode = 'r',
    encoding='utf-8'
) as file:
    print(file.readlines())

# Python translates \n to the platform-specific
# line ending when writing
path = Path("filename-demo.txt")
with path.open(
    mode='w',
    encoding="utf-8"
) as file:
    file.write("The 1st line\n2nd line\n3rd line")

# override the universal new line
path = Path("filename-demo-1.txt")
with path.open(
    mode = 'w',
    encoding = 'utf-8',
    newline = '\r\n'
) as file:
    file.write("The 1st line\n2nd line\n3rd line")

