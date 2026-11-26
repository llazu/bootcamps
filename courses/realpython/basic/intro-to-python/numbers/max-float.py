''' Exercise 3 - Find the Maximum Number
In IDLE’s interactive window, try to find the smallest exponent N
for which 2e<N>, where <N> is replaced with your number, returns
inf.
'''

n = 200

max = float(f"2e{n}")

while max != float("inf"):
    n += 1
    print(f'the current n: {n}')
    max = float(f"2e{n}")
    print(f'the current max: {max}')

'''
Course Solution

import sys

print(sys.float_info.max_10_exp)
'''
