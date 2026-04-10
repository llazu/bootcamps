# Exercise - write a program that uses string
# methods to alter each string so that
# .startswith("be") returns True for all of them

string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = "  bEautiful"

string1 = string1.replace("B", "b")
print(string1)
string3 = string2.lower()
print(string3)
string4 = string4.strip().replace("E", "e")
print(string4)

print(string1.startswith("be"))
print(string2.startswith("be"))
print(string3.startswith("be"))
print(string4.startswith("be"))