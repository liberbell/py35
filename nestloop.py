names = [["Bob", "Eric", "George"],
         ["Ed", "Alex", "Elton"]]

for sublist in names:
    print(sublist)

for sublist in names:
    for name in sublist:
        print(name)