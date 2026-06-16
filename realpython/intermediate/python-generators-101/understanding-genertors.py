
# return num prevents the infinite sequence
def infinite_sequence():
    num = 0
    while True:
        return num
        num += 1

# print(infinite_sequence())

# replace return with yield makes infinite_sequence_gen infinite
def infinite_sequence_gen():
    num = 0
    while True:
        yield num
        num += 1

inf = infinite_sequence_gen()

# find the data type
# print(type(inf))

# get the 'next' values of inf
# print(next(inf))

# print(next(inf))

def infinite_sequence_gen_new():
    num = 0
    while True:
        yield num
        num += 1
        yield "This is a second yield statement"

inf_new = infinite_sequence_gen_new()

#print(type(inf_new))

# print(next(inf_new))
# print(next(inf_new))
# print(next(inf_new))
# print(next(inf_new))

# exhausting a generator
# finite sequence
# StopIteration exception
def finite_sequence():
    nums = [1,2,3]
    for num in nums:
        yield num

fin = finite_sequence()

print(next(fin))
print(next(fin))
print(next(fin))
print(next(fin))

#list comprehensions
nums_squared_lc = [num**2 for num in range(1,5)]
nums_squared_gc = (num**2 for num in range(1,5))

