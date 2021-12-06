print(35000-15000)

gross_salary = 1000000
print(gross_salary)

income_tax = 50000
retirement_contribution = 1800
professional_tax = 300

net_salary = gross_salary - (income_tax + retirement_contribution + professional_tax)
print(net_salary)

student_score1 = 89
student_score2 = 75

total_score = student_score1 + student_score2
print(total_score)

average_score = (student_score1 + student_score2) / 2
print(average_score)

first_name = "Alice"
last_name = "Bond"

print(first_name + last_name)

full_name = first_name + " " + last_name
print(full_name)

salary1 = salary2 = salary3 = 3000000
print(salary1, salary2, salary3)
print(salary1 == salary2)

salary1 = salary1 + 10000
salary2 = salary2 * 1.12
print(salary1, salary2)

salary3 = salary3 - salary3 * 0.03
print(salary3)

print(salary1 == salary2)

my_int, my_float, my_bool, my_string = 12, 3.2, False, "Hello world"

print(type(my_int), type(my_float), type(my_bool), type(my_string))

result = my_int + my_float
print("The final result is: ", result)

# result = my_int + my_string
# print("The final result is: ", result)

# del net_salary
# print(net_salary)

del first_name
print(first_name)