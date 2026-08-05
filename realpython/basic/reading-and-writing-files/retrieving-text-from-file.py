# read to read the entire file's content
file = open("incremental.txt", encoding="utf-8")
read = file.read()
print(read)
# receive empty string because end of file reached
read_next = file.read()
print(read_next)

# reset the read to the beginning
seek = file.seek(0)
print(seek)