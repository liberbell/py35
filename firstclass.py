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