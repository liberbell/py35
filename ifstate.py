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
                    "Eric": 39000,
                    "Alex": 32000}
print(employee_salaris)

if "Elton" not in employee_salaris:
    employee_salaris["Elton"] = 46000

print(employee_salaris)
if "Elton" in employee_salaris.keys():
    print("Elton`s salary is: ", employee_salaris["Elton"])
    
if employee_salaris["Eric"] > 30000 and employee_salaris["Eric"] < 40000:
    print("Eric`s original sarary: ", employee_salaris["Eric"])
    # print("log")
    employee_salaris["Eric"] = employee_salaris["Eric"] * 1.1
    print("Eric`s update salary: ", employee_salaris["Eric"])
print(names_list)
if ("Eric" in names_list) or ("Ray" in names_list):
    print("we found either Eric or Ray in the name list.")
    
if 20 <=100:
    print("20 is less than or equal to 100")
    
if not (20 <= 100):
    print("not of a True condition is False")
    
# student_score = int(input("Please enter your score: "))

# if student_score  > 45:
#     print("You`ve passed your exam!")
#     print("If block executed.")
# else:
#     print("You`ve failed your exam!")
#     print("Else block executed.")
    
num = 50
print("num before expression: ", num)
num = num - 20 if num > 20 else num + 20
print("num after expression: ", num)

num = 100
print("Number before expression: ", num)
num = num / 5 if num < 50 else num * 5
print("Number after exression: ", num)

student_score = int(input("Please enter your score: "))

if student_score  > 85:
    print("Your grade is A")
    print("You`ve passed your exam!")
    print("If block executed.")
elif student_score > 65:
    print("Your grade is B")
    print("First elif block execute.")
elif student_score > 50:
    print("Your score is C")
    print("Second elif block execute.")
else:
    print("You`ve failed your exam!")
    print("Else block executed.")
print("This is outside the if-elif-else blocks.")

item_ordered = int(input("Please enter how many items were orderd: "))
item_inventory = int(input("Please enter how many items are present in your inventory: "))