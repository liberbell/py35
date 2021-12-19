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