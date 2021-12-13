my_set = set()
print(type(my_set), my_set)

name_set = {"Bob", "Eric", "George", "Elton"}
print(name_set)

name_set = {"Bob", "Eric", "George", "Elton", "Ed", "Frank"}
print(name_set)

mixed_set = {10.3, 1, "George", True}
print(mixed_set)

mixed_set = {"George", 10, 50.5, True}
print(mixed_set)

another_mixed_set = {"Eric", 10, 10.5, True, (1, 2, 3)}
print(another_mixed_set)

# another_mixed_set = {"Eric", 10, 10.5, True, [1, 2, 3]}
# print(another_mixed_set)

laptop_set = {"HP", "Apple", "Dell", "MSI", "TOSHIBA", "Lenovo", "ASUS"}
print(laptop_set)

laptop_set.add("Genepac")
print(laptop_set.add("Apple"))
laptop_set.discard("Dell")
print(laptop_set)

laptop_set.remove("Lenovo")
# laptop_set.remove("Lenovo")

student_set1 = {"Eric", "Bob"}
student_set2 = {"George", "Ed"}
student_set3 = {"Ed", "Alex"}
print(student_set1.union(student_set2))
print(student_set1)
print(student_set2.intersection(student_set3))
print(student_set1.difference(student_set3))

print({1, 2, 3}.isdisjoint({4, 5, 6}))
print({10, 20}.issubset({10, 20, 30}))
print({10, 20, 30}.issuperset({10, 20}))

name_list = ["Eric", "Alex", "Jhon", "Alex", "Ed", "Jhon"]
name_tuple = ("Eric", "Alex", "Jhon", "Alex", "Ed", "Jhon")
print(name_list, name_tuple)
name_list_to_set = set(name_list)
print(name_list_to_set)