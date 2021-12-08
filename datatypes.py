some_string = "programming in python is interesting."
print(type(some_string))

print(type(some_string))

some_number = 4.8
print(type(some_number))

some_complex_number = 20j
print(type(some_complex_number))

some_boolean = True
print(type(some_boolean))

some_bytes = bytes(10)
print(some_bytes)
print(type(some_bytes))

some_memoryview = memoryview(bytes(10))
print(some_memoryview)
print(type(some_memoryview))

numbers_list = [3, 5, 7, 9]
print(numbers_list)
print(type(numbers_list))
print(numbers_list[2])
print(type(numbers_list[2]))

mixed_list = [1, 3.4, "Bob", True]
print(mixed_list)
print(type(mixed_list))
print(type(mixed_list[1]))
print(type(mixed_list[2]))

record = ("Elton", 34, 10.2, True)
print(record)
print(type(record))
print(type(record[0]))
print(type(record[2]))
