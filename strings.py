string1 = 'Python allow you to define strings using single quotes'
print(string1)

string2 = "Python allow you to define strings using double quotes"
print(string2)

string3 = """Python allow you to define strings using triple quotes"""
print(string3)

# multiline_string = 'Strings cannot span multiple
# lines when encloded in single quote'
# print(multiline_string)

# multiline_string = "Strings cannot span multiple
# lines when encloded in double quote"
# print(multiline_string)

multiline_string = """Strings cannot span multiple
lines when encloded in triple quote"""
print(multiline_string)

nicely_formatted_string = """
Triples quotes are useful because
you can format and display your strings nicely in code
you can include 'single quote' and "double quotes"
within the string
"""
print(nicely_formatted_string)

some_string = 'That happend to be Jack\'s baseball bat'
print(some_string)

some_string = "That happend to be Jack's baseball bat"
print(some_string)

another_string = "I assigned the value of that variable to \"red\""
print(another_string)

another_string = 'I assigned the value of that variable to "red"'
print(another_string)

print('C:\\Users\\Projects')

some_text = "Did you watch the gaem last night\t I stayed up to watch the end!"
print(some_text)

favorite_sport = "baseball"
time_spent = 2
# print("I love watching {} on TV - yesterday for {} hours.".format(favorite_sport, time_spent))

favorite_sport = "soccer"
print("I love watching %s on TV - yesterday for %d hours." % (favorite_sport, time_spent))

favorite_sport = "basketball"
time_spent = 2.5
print(f"I love watching {favorite_sport} on TV - yesterday for {time_spent} hours.")