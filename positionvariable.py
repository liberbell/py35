def display(*args):
    print(args)

display()
display("Python")
display("Pyhon", "Ruby")

languages_list = ["Python", "Java", "C++", "C#", "JavaScript"]
display(languages_list)
display(*languages_list)

languages_list = ("Python", "Java", "C++", "C#", "JavaScript")
display(*languages_list)

department_employee_mapping = {}
def add_employe_to_department(department, *employee):
    if department not in department_employee_mapping:
        department_employee_mapping[department] = []

    for employee in employees:
        department_employee_mapping[department].append(employee)

print(department_employee_mapping)
add_employe_to_department("Sales")
print(department_employee_mapping)