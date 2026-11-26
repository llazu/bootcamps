"""
Exercise 1
Write the following text to a file in your home
directory called starship.txt

Discovery
Enterprise
Defiant
Voyager

Each word should on a separate line
"""
import os

# Escape the backslash
esc_path ="C:\\Users\\luisl\\startships.txt"
# Use raw string
raw_path = r"C:\Users\luisl\starships-raw.txt"
# Cross-platform solution
home_dir = os.path.expanduser("~")
file_path = os.path.join(home_dir, "starships.txt")

with open(file_path, "w", encoding="utf-8", newline="") as f:
    f.write("Discovery\n")
    f.write("Enterprise\n")
    f.write("Defiant\n")
    f.write("Voyager")

with open(raw_path, "w", encoding="utf-8", newline="") as f:
    f.writelines([
        "Discovery\n",
        "Enterprise\n",
        "Defiant\n",
        "Voyager"
    ])