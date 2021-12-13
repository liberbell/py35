my_dict = {}
print(type(my_dict), my_dict)

my_employee = {"Bob": 4000,
               "Eric": 5000,
               "Alex": 2500,
               "Jhon": 5500}

print(my_employee)
print(my_employee["Alex"])
my_employee["Eric"] = 6000
print(my_employee)
my_employee["Eric"] *= 2
print(my_employee)

del my_employee["Jhon"]
print(my_employee)

dictionary_with_int_keys = {1: "Bob", 2: "George", 3: "Elton", 4: "Ed"}
print(dictionary_with_int_keys)

dictionary_with_float_keys = {1.1: "Bob", 1.2: "George", 1.3: "Elton", 1.4: "Ed"}
print(dictionary_with_float_keys)

print(my_employee)
my_employee.pop("Eric")
print(my_employee)

print(my_employee.keys())
print(len(my_employee)) 

d = my_employee
for i in d.values():
    print(i)