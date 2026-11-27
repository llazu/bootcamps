import csv
from pathlib import Path

path = Path("December_Expenses.csv")

# new line disables universal line character
with path.open(encoding="utf-8", newline="") as file:
    # yields rows
    reader = csv.reader(file)
    for row in reader:
        print(row)

file = path.open(encoding="utf-8", newline="")
reader = csv.DictReader(file)
print(reader.fieldnames)
print(reader)

file.close()

with path.open(mode="w", encoding="utf-8", newline="")as file:
    writer = csv.writer(file)
    # you can use tuples or other sequences in writerow
    writer.writerow(["John", "Doe", "42"])
    writer.writerow(["Anna", "Smith", "24"])
    writer.writerows([
        ["Peter", "Jones", 36],
        ["Jane", "Brown", 63]
    ])

with path.open(mode="w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, ["first_name", "last_name", "age"])
    writer.writeheader()
    writer.writerow({"first_name": "John", "last_name": "Doe", "age": 42})

with path.open(mode="r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)