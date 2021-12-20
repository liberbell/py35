from typing import SupportsComplex


names = [["Bob", "Eric", "George"],
         ["Ed", "Alex", "Elton"]]

for sublist in names:
    print(sublist)

for sublist in names:
    for name in sublist:
        print(name)

color_list = ["Red", "Green", "Blue"]
object_list = ["Pen", "Marker", "Pencil"]
for color in color_list:
    for obj in object_list:
        print(color, obj)

some_range = range(20)
print(some_range)
print(tuple(some_range))

print(list(range(-5, 5)))
for i in range(5):
    print(i)

for i in range(0, 30, 3):
    print(i, end=" ")

print("\n")

for i in range(-15, +15, 4):
    print(i, end=" ")
print("\n")

my_list = []
for i in range(0, 20):
    if (i % 2 or i % 4 == 0):
        my_list.append(i)
print(my_list)

for my_num in range(1, 7):
    print(my_num, "cube is", my_num ** 3)