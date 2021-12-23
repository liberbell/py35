numbers = [100, 200, 300, 400, 500, 600]
print(numbers)

numbers_copy = numbers
print(numbers_copy)

for number in numbers:
    numbers_copy.append(number)

print(numbers_copy)