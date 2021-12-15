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

second_person = first_person.copy()
second_person[0] = "Eric"
print(second_person)

second_person[1][0] = "Brookline Avenue"
second_person[1][1] = "Washington"
print("First : ", first_person)
print("Second: ", second_person)