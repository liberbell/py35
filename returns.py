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

result = positive_or_negative(0)
print(result)
print(type(result))

def create_list(some_string:str, num_times:int) -> list:
    """
    Returns a list containing the specified string tht specified
    number of times

    The first argument is the string you want printed, the second
    argument is the number of times you want the string printed

    Parameters (both required)
    some_string(str): The string to be printed
    num_times(int): The number of times the string should be printed 
    """
    return [(some_string for i in range(num_times))]

result = create_list("Hello", 10)
print(return)