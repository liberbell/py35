from copy import deepcopy

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

first_person = ["Bob", ["1394 West Zenith St", "Massachusetts"]]
second_person = deepcopy(first_person)
print("First : ", first_person)
print("Second: ", second_person)

second_person[0] = "Eric"
second_person[1][0] = "Brookline Avenue"
print("First : ", first_person)
print("Second: ", second_person)

ice_cream_tuple = ("Vanilla", ["Chocolate", "Vanilla"], "Strawberry", "Blueberry")
print(ice_cream_tuple)

ice_cream_tuple_copy = ice_cream_tuple
print("original: ", ice_cream_tuple)
print("copied  : ", ice_cream_tuple_copy)

ice_cream_tuple_copy[1][0] = "Butterscotch"
print("original: ", ice_cream_tuple)
print("copied  : ", ice_cream_tuple_copy)

ice_cream_tuple = ("Vanilla", ["Chocolate", "Vanilla"], "Strawberry", "Blueberry")
# ice_cream_tuple_copy = ice_cream_tuple.copy()
# print("original: ", ice_cream_tuple)
# print("copied  : ", ice_cream_tuple_copy)

ice_cream_tuple_copy = deepcopy(ice_cream_tuple)
ice_cream_tuple_copy[1][0] = "Butterscotch"
print("original: ", ice_cream_tuple)
print("copied  : ", ice_cream_tuple_copy)

colors_set = {'blue', 'red', 'orange', 'yellow', 'pink'}
print(colors_set)

colors_set_copy = colors_set
print("original: ", colors_set)
print("copied  : ", colors_set_copy)

colors_set_copy.remove('red')
print("original: ", colors_set)
print("copied  : ", colors_set_copy)

colors_set_copy.add('magenta')
print("original: ", colors_set)
print("copied  : ", colors_set_copy)

colors_set = {'blue', 'red', ('orange', 'yellow'), 'pink'}
print(colors_set_copy)
print(colors_set_copy[2][1])