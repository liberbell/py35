numbers = [100, 200, 300, 400, 500, 600]
print(numbers)

numbers_copy = []
print(numbers_copy)

for number in numbers:
    numbers_copy.append(number)

print(numbers_copy)

numbers_copy_using_comprehension = [number for number in numbers]
print(numbers_copy_using_comprehension)

number_square = [n * n for n in numbers]
print(number_square)

numbers_divided_by_ten = [n / 10 for n in numbers]
print(numbers_divided_by_ten)

my_num = range(2, 10)
print(my_num)