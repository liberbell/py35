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

print(laptop_set.add("Apple"))
laptop_set.discard("Dell")