'''
Floating Numbers - Exercise 1
Limit Decimal Places
Instructions
Print the result pf the calculatio `3 ** .125` as a fixed-point
number with three decimal places.
'''

num = 3 * .125

print(f'f-string method: {num:.3f}')

print("format helper method: " + format(num, ".3f"))

print('replacement field method: {:.3f}'.format(num))