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