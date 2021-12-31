def order_food(name, food):
    print(f"My name is {name} and I have ordered {food}.")

order_food("Eric", "peach")
# order_food("Alex")

def create_student_record(name, age, major, gpa):
    return {
        "name": name,
        "age": age,
        "major": major,
        "gpa": gpa
    }

student_1 = create_student_record("Eric", 23, "Computer Science", 3.8)
print(student_1)

# student_2 = create_student_record("Alex", 4.6, 19, "Math")
# print(student_2)

student_2 = create_student_record(name = "Alex", age = 19, major = "Math", gpa = 4.6)
print(student_2)

student_3 = create_student_record(gpa = 3.2, age = 24, major = "Plants", name = "Elton")
print(student_3)

# student_3 = create_student_record(gpa = 3.2, age = 24, major = "Plants", name = "Elton", minor = "Philosophy")
# print(student_3)

student_4 = create_student_record("Bob", 18, major = "Plants", gpa = 3.2)
print(student_4)

def create_student_record(name, age, gpa, major = "Computer Science", university = "Priceton"):
    return {
        "name": name,
        "age": age,
        "gpa": gpa,
        "major": major,
        "university": university
    }

student_1 = create_student_record("Elton", 22, 3.4)
print(student_1)

student_2 = create_student_record("George", 20, 3.8, "English")
print(student_2)