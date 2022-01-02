# def print_student_details(name, age, gpa, enrolled):
#     print("Name:", name)
#     print("Age:", age)
#     print("GPA:", gpa)
#     print("Enrolled:", enrolled)

# print_student_details("Bob", 24, 4.1, True)

def print_student_details(name, age, gpa, enrolled):
    name = name.upper()
    age = age + 10
    gpa = gpa - 0.3
    enrolled = False
    
    print("Name:", name)
    print("Age:", age)
    print("GPA:", gpa)
    print("Enrolled:", enrolled)

print_student_details("Bob", 24, 4.1, True)