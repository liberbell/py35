first_list = ["apple", "plum", "mango", "guava", "peer"]
print(first_list)

first_copy = first_list
print(first_copy)

first_list.remove("mango")
print("Original:", first_list)
print("Copy:   :", first_copy)

first_copy = first_list.copy()
print(first_copy)

first_list[0] = "pinapple"
print("Original:", first_list)
print("Copy:   :", first_copy)

first_person = ["Bob", ["1394 West Zenith St", "Massachusetts"]]
print(first_person)