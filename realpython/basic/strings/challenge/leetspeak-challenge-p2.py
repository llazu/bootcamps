'''
Challenge: Turn Your User Into a L33T H4Ck3r (2/3)

New Condition: Use method chaining

Use ".replace" to convert the text entered by the user
into leetspeak by making the following changes to lowercase letters

- The letter a becomes 4
- The letter b becomes 8
- The letter e brcomes 3
- The lrtter l becomed 1
- The letter o becomes 0
- The letter s becomes 5
- The letter t becomes 7
'''

code = input("Specify the message you would like to encrypt? ")

code = code.replace("a", "4")\
           .replace("b", "8")\
           .replace("e", "3")\
           .replace("l", "1")\
           .replace("o", "0")\
           .replace("s", "5")\
           .replace("t", "7")

print(code)