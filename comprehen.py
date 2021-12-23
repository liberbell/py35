numbers = [100, 200, 300, 400, 500, 600]
print(numbers)

numbers_copy = []
print(numbers_copy)

for number in numbers:
    numbers_copy.append(number)

print(numbers_copy)

numbers_copy_using_comprehension = [number for number in numbers]
print(numbers_copy_using_comprehension)