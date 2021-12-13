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