my_list = []
print(my_list)
print(type(my_list))

empty_list = list()
print(empty_list)
print(type(empty_list))

game_list = ['Badminton', 'Golf', 'Basketball', 'Tennis']
print(game_list)
print(type(game_list))
print(game_list[1], game_list[3])
print(game_list[-1], game_list[-2])

boolean_list = [True, False, False, True]
print(boolean_list)
print(len(game_list))
print(len(boolean_list))

mixed_list = ["Bob", "Eric", 22, 1, 4.5, False, True]
print(mixed_list)
print(type(mixed_list))
print(len(mixed_list))

print(game_list)
game_list[0] = "soccer"
print(game_list)
game_list[3] = "Table tennis"
print(game_list)

integers_list = [10, 20, 30, 40, 50]
print(integers_list)
integers_list[1] += 100
print(integers_list)