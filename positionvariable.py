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
def add_employe_to_department(department, *employees):
    if department not in department_employee_mapping:
        department_employee_mapping[department] = []

    for employee in employees:
        department_employee_mapping[department].append(employee)

print(department_employee_mapping)
add_employe_to_department("Sales")
print(department_employee_mapping)

add_employe_to_department("Sales", "Eric", "Alex", "George")
print(department_employee_mapping)
add_employe_to_department("Engineering", "Elton", "Jhon", "Ringo")
print(department_employee_mapping)

department_employee_mapping = {}
def add_employee_to_department(*employees, department):
    if department not in department_employee_mapping:
        department_employee_mapping[department] = []
    for employee in employees:
        department_employee_mapping[department].append(employee)

# add_employee_to_department("Sales", "Bob", "Eric", "Jhon")
# print(department_employee_mapping)

add_employee_to_department("Bob", "Eric", "Jhon", department= "Sales")
print(department_employee_mapping)

def add_employee_details(**kwargs):
    print(type(kwargs))
    print(kwargs)

add_employee_details(name="Bob", age=34)

employee_detail_mapping = {}
def add_employee_details(**employee_details):
    employee_detail_mapping[employee_details["name"]] = employee_details

add_employee_details(name = "Eric", age = 45)
print(employee_detail_mapping)

add_employee_details(name="Alex", age=31, salary=450000, department="Human Resource")
print(employee_detail_mapping)

def students_in_college(*student_name, **college_details):
    print("Students--")
    for s in student_name:
        print(s)

    print()

    print("College Details--")
    for key, value in college_details.items():
        print(key, value)

students_in_college("Eric", "Bob", "Ringo", name="Stanford", city="Palo Alto")