#Christopher Kenny
#CS 175
#Dictionaries Q3: Create a program to select only employees in sales

employees = {
    'Alice': {'age': 25, 'department': 'Sales'},
    'Bob': {'age': 30, 'department': 'Marketing'},
    'Charlie': {'age': 28, 'department': 'Sales'},
    'David': {'age': 22, 'department': 'It'}
}

sales_employees = {name: info for name, info in employees.items() if info['department'] == 'Sales'}
print(sales_employees)
