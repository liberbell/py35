# number = 100
# while number > 99:
#     print(number)

num = 7
while num <= 10:
    print(num)
    num += 1

# num = 7
# while num >= 0:
#     print(num)
#     num -= 1

sum_upto = 20
i = 0
total = 0
while i <= sum_upto:
    total += i
    i += 1

print(f"Computed sum upto {sum_upto} and the result is {total}")

# invalid_num = True
# while invalid_num:
#     num = int(input("Enter a number in the range between 100 to 300:"))

#     if num >= 100 and num <= 300:
#         invalid_num = False
#     else:
#         print("Sorry the number is not valid")
#         print("Please try again")

# print("Valid number is :", num)
# print("We will only get here when we enter a valid number.")

current_num = 0
count = 0
total = 0
while current_num >= 0:
    current_num = int(input("Enter any number: "))

    if current_num >= 0:
        count = count + 1
        total = total + current_num

average = total / count
print("Number input: ", count, "Average: ", average)