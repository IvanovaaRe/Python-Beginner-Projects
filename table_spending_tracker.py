table_bills = {
    "Table 1": 125,
    "Table 2": 35,
    "Table 3": 85,
    "Table 4": 15,
    "Table 5": 60
}

spending_status = {}

for table, spending in table_bills.items():
    if spending >= 100:
        spending_status[table] = "Premium Spending"
    elif 40 <= spending <= 99:
        spending_status[table] = "Average Spending"
    else:
        spending_status[table] = "Low Spending"

print(spending_status)
