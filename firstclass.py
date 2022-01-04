def say_hello(name):
    return f"HELLO {name}"

print(say_hello("Bob"))
greet_hello = say_hello
print(greet_hello("Eric"))
print(dir(say_hello))

print(say_hello.__str__)

def square(number):
    return number * number

def cube(number):
    return number * number * number

def raise_to_four(number):
    return number ** 4

def raise_to_n(number, n):
    return number ** n

def cube_root(number):
    return number ** (1/3)

def square_root(number):
    return number ** (1/2)
    
def calculate(number, func):
    return func(number)

print(calculate(10, square))
print(calculate(10, cube))
print(calculate(10, raise_to_four))

def calculate(*args, func):
    return func(*args)
print(calculate(10, 2, func=raise_to_n))

def get_function(computaion = "square"):
    if computaion == "square":
        return square
    elif computaion == "cube":
        return cube
    elif computaion == "square_root":
        return square_root
    elif computaion == "cube_root":
        return cube_root
    elif computaion == "raise_to_n":
        return raise_to_n

fn = get_function()
print(fn)
print(fn(10))

fn = get_function("cube_root")
print(fn(10))

# print(square())
# print(cube())
# print(raise_to_four())
# print(raise_to_n())