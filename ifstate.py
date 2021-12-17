# if True:
#     print("This condition is always true, which means this code will always run!")
if False:
    print("This condition is always false, which means this code will never run!")
    
if 1000 > 100:
    print("1000 is greater than 100")
    
gross_salary = 500000
if gross_salary >= 500000:
    tax_rate = 30
print(tax_rate)
del tax_rate
# print(tax_rate)

# gross_salary = 400000
# if gross_salary >= 500000:
#     tax_rate = 30
# print(tax_rate)

names_list = ["Bob", "George", "Eric", "Alex", "Elton"]
if "Bob" in names_list:
    names_list.append("Edo")
    print("Bob was present in name list")
print(names_list)

employee_salaris = {"Bob": 34000,
                    "George": 35000,
                    "Eric": 41000,
                    "Alex": 32000}
print(employee_salaris)

if "Elton" not in employee_salaris:
    employee_salaris["Elton"] = 46000

print(employee_salaris)
if "Elton" in employee_salaris.keys():
    print("Elton`s salary is: ", employee_salaris["Elton"])
    
if employee_salaris["Eric"] > 30000 and employee_salaris["Eric"] < 40000:
    print("Eric`s original sarary: ", employee_salaris["Eric"])
    employee_salaris["Eric"] = employee_salaris["Eric"] * 1.1
    print("Eric`s update salary: ", employee_salaris["Eric"])