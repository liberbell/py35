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
print([x ** x for x in my_num])

list_of_words = ["to", "be", "or", "not", "to", "be", "that", "is", "the", "question"]
uppercase_list = [word.upper() for word in list_of_words]
print(uppercase_list)

first_two_letters = [word[:2] for word in list_of_words]
print(first_two_letters)

print([x * x for x in range(20) if x % 2 == 0])

multiples_13 = [i for i in range(200) if i % 13 == 0]
print(multiples_13)

print([i for i in "Harry Potter" if i.upper() not in ["A", "I", "U", "E", "O"]])

shapes = ["Square", "Circle", "Triangle"]
colors = ["Red", "Blue", "Green"]
combined = [(color, shape) for shape in shapes for color in colors]
print(combined)

number_list = [number for number in range(200) if number % 7 == 0 if number % 13 == 0]
print(number_list)

num = [(i, "Even") if i % 2 == 0 else (i, "Odd") for i in range(8)]