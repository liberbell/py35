# for letter in "James Bond":
#     print(letter)
#     if letter == "o":
#         break
    # print(letter)

for num in [3, 11, 22, 35, 90]:
    print(num)

    if (num == 35):
        print("The number %d has been found." % num)
        print("Terminating the loop...")
        break

places = ["New Zealand", "Norway", "Botswana", "Zimbabwe", "Uzbekistan", "Paraguay"]
burglar_at = input("Enter the country where the burglar actually is: ")
for place in places:
    print("Cops looking in ", place)

    if place == burglar_at:
        print("The burglar has been captured!")
        break
else:
    print("The burglar got away...")