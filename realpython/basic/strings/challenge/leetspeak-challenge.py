'''
Challenge: Turn Your User Into a L33T H4Ck3r (2/3)

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

'''
no need for if because replace searches and does nothing if there is no match
if "a" in code:
    code = code.replace("a", "4")

if "b" in code:
    code = code.replace("b", "8")

if "e" in code:
    code = code.replace("e", "3")

if "l" in code:
    code = code.replace("l", "1")

if "o" in code:
    code = code.replace("o", "0")

if "s" in code:
    code = code.replace("s", "5")

if "t" in code:
    code = code.replace("t", "7")
'''

code = code.replace("a", "4")
code = code.replace("b", "8")
code = code.replace("e", "3")
code = code.replace("l", "1")
code = code.replace("o", "0")
code = code.replace("s", "5")
code = code.replace("t", "7")

print(code)