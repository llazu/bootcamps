# read to read the entire file's content
file = open("incremental.txt", encoding="utf-8")
read = file.read()
print("read entire file", read)
# receive empty string because end of file reached
read_next = file.read()
print("empty string EOF", read_next)

# reset the the start of file
seek = file.seek(0)
print("resetting to start of file", seek)

# read from the begining
print("read from the start", file.read())

#index 5 
seek = file.seek(5)
print("set index of 5", seek)
#reading will start from offset and go to the EOF
print("read after index 5", file.read())

# read x amount of characters
file.seek(0) # reset file
read_char = file.read(5)
print("read up to index 5", read_char)
# read 5 more characters from file
print("the next 5 characters: ",file.read(5))
# read 1000 chars; python doesn't raise error if end of file
print("read the next 1000: ", file.read(1000))
# find out the offset
print("offset is: ", file.tell())
file.close()

file = open("zen.txt", encodings="utf-8")