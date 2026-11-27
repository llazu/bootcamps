"""
Write a function total_expenses() that reads a CSV file of expenses and returns the total amount.

The CSV file has columns: Date, Category, Amount, and Description. For example:

Date,Category,Amount,Description
2024-01-15,Food,45.99,Grocery shopping
2024-01-16,Transport,12.50,Bus pass
2024-01-17,Food,8.75,Lunch

total_expenses("expenses.csv")
outputs 67.24

Requirements
Use csv.DictReader to read the CSV file
Open the file with newline="" as recommended for CSV files
Convert each Amount value from a string to a float before summing
Return the total as a float
"""
import csv
from pathlib import Path

def total_expenses(file):
    path = Path(file)
    with path.open(mode="r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip csv headers
        total = 0
        for row in reader:
            total += float(row[2])
    return total

print(f"The toatl expense is ${total_expenses("expense.csv"):.2f}")
