from tabulate import tabulate

headers = ["Name", "Age", "Department"]
data = [
    ["Ravi", 25, "HR"],
    ["Anjali", 30, "Finance"],
    ["Mohan", 28, "IT"],
    ["Sneha", 24, "Marketing"],
    ["Anu", 32, "Logistics"],
]

print(tabulate(data, headers=headers, tablefmt="grid"))
