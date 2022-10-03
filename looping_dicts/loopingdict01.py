#!/usr/bin/env python3

## create a dictionary of fruit companies.
fruitcompanies= [{"name":"Zesty","employees":["Brian", "Colin", "Derik", "Emily", "Fortune"]},
                 {"name":"Ripe.ly","employees":["Kishor", "Leia", "Maria", "Jason"]},
                 {"name":"FruitBee","employees":["Monte", "Jarrad", "Pemba", "Don"]},
                 {"name":"HoneyGrove","employees":["Tim", "Travis", "Trung", "Torin"]}]

# Part 1
co_name = fruitcompanies[0]["name"]
print(f"Employees of", co_name)

for employee in fruitcompanies[0]["employees"]:
    print(employee, end=" ")

print("\n")

# Part 2

print("\nCompany Names")

for company_dicts in fruitcompanies:
    #print(company_dicts)
    company_name = company_dicts["name"]
    print(company_name, end=" ")

print("\n")

company = input("Which fruit company do you wish to see the employees for? ")
print("\nYou chose:", company)

for company_dicts in fruitcompanies:
    company_name = company_dicts["name"]
    if company_name == company:
        for emp_names in company_dicts["employees"]:
            if emp_names != "Jason":
                print(emp_names, end=" ")

print(" ")
