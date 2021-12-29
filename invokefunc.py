# print("A function is a set of operations that accept inputs.")
# print("Functions performe some specific computation and produce output")

def my_function():
    print("A function is a set of operations that accept inputs.")
    print("Functions performe some specific computation and produce output")

# my_function()
# hello()

# def hello():
#     print("in function hello")
#     print("What does this print?")

# hello()

def hello():
    print("in function hello")

# print("This is outside the function defenition.")
# hello()

def happy_birthday_charlie():
    """I hope your celebration gives you many happy memories!"""
    print("I hope you have a great day.")

# print(happy_birthday_charlie.__doc__)
# happy_birthday_charlie

some_function = happy_birthday_charlie
# print(some_function)
# some_function()

def function_with_error():
    result = "a" + 2

    print(result)
# print(function_with_error())
# print(function_with_error)

def greet(name):
    print(f"Hi {name}")
    print("Welcome aboard!")

# greet("Bob")

def greet_fullname(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard!")

greet_fullname("Alex", "Hep")
# greet("Bob", "Alex")
# greet_fullname("Alex")

def divisible_by_5(some_number):
    if some_number % 5 == 0:
        print(f"This number {some_number} is divisible by 5.")
    else:
        print(f"This number {some_number} is not divisible by 5.")
divisible_by_5(11)