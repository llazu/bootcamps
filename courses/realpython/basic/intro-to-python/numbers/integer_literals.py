'''
Exercise: Write a program that creates two variables, num1 and num2.

Both num1 and num2 should be assigned the integer liter 25000000,
one written with underscores and one without.

Print num1 and num2 on two separate lines.
'''

num1 = 25000000
num2 = 25_000_000

print(f"printing num1 'as-is': {num1}")
print(f"printing num2 with underscores: {num2}")

'''
post-exercise notes

Despite num2 having underscores, python printed it as `25000000`.

This is becaused python ignores the undersores; both num1 and num2 have the same numeric value. git
'''
