"""
.send()
Allows you to send a value to the generator.
It slips a value into the last yield statement where you stopped.

.throw()
Allow you to throw and exception in a generator.

.close()
Allows you to close a generator if it hits a generator.
"""

# a function that detects palindrome
# a palindrome reads the same forward and backward

def is_palindrome(num):
    # Skips single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0
    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10
    if num == reversed_num:
        return True
    else:
        return False

# send is a placeholder where we can slide in a new value
def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            # assumes the value from the send method
            i = (yield num)
            if i is not None:
                num = i
        num += 1

pal_gen = infinite_palindromes()
for i in pal_gen:
    print(i)
    digits = len(str(i))
    # sending to generator
    if digits == 5:
        #pal_gen.throw(ValueError("We don't like large palindromes"))
        pal_gen.close() 
    pal_gen.send(10 ** digits)


