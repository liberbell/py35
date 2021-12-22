# for letter in "James Bond":
#     print(letter)
#     if letter == "o":
#         break
    # print(letter)

# for num in [3, 11, 22, 35, 90]:
#     print(num)

#     if (num == 35):
#         print("The number %d has been found." % num)
#         print("Terminating the loop...")
#         break

# places = ["New Zealand", "Norway", "Botswana", "Zimbabwe", "Uzbekistan", "Paraguay"]
# burglar_at = input("Enter the country where the burglar actually is: ")
# for place in places:
#     print("Cops looking in ", place)

#     if place == burglar_at:
#         print("The burglar has been captured!")
#         break
# else:
#     print("The burglar got away...")

# letters = "James Bond"
# for letter in letters:
#     print(letter)
#     if letter in ["a", "i", "u", "e", "o"]:
#         continue

# dogs = ["Labrador", "Golden Retriever", "Pug", "Greyhound", "Bulldog", "Cooker Spaniel"]
# for pet in dogs:
#     if pet == "Pug":
#         continue
#     if pet == "Bulldog":
#         break
#     print(pet)


# for letter in "James Bond":
#     if letter in ["a", "i", "u", "e", "o"]:
#         pass
#         print("We are in the pass block")
#     else:
#         print(letter)

# print("Finally done")

for i in range(1, 8):
    print(i)
    if i > 4:
        pass
    else:
        print("hello")
    print("Complete iteration.")