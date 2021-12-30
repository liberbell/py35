def square(x):
    y = x * x
    
    # print("Returns: ", y)
    return y

result = square(8)
print(result)
print(type(result))

result = square(10.22341)
print(result)
print(type(result))

def calculate(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2

    return add, sub, mul, div

result = calculate(10, 2)
print(result)
print(type(result))

# add_result, sub_result, mul_result, div_result = calculate(10, 2)
# print(add_result, sub_result, mul_result, div_result)
# print(type(result))

add_result, _, _, _, = calculate(100, 5)
print(add_result)

def positive_or_negative(num):
    if num > 0:
        return "Positive!"
    elif num < 0:
        return "Negative!"
    else:
        return "Zero!"

result = positive_or_negative(-4)
print(result)
print(type(result))