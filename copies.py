first_list = ["apple", "plum", "mango", "guava", "peer"]
print(first_list)

first_copy = first_list
print(first_copy)

first_list.remove("mango")
print("Original:", first_list)
print("Copy:   :", first_copy)

first_copy = first_list.copy()
print(first_copy)