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

print(sum(integers_list))

float_list = [5.7, 6.5, 90.2, 82.8, 3.5, 8.2]
print(float_list)
print(type(float_list))
print(max(float_list))

game_list = ['Soccer', 'Golf', 'BasketBall', 'Table tennis', 'Tennis', 'Skating']
print(game_list)
print(game_list[0:2])
print(game_list[1:6:2])

print(game_list[-5:-1])

movie_lists = ["Avatar", "Pacific rim", "The Golden Compass", "Monsters University", "X-Men: The Last Stand"]
print(movie_lists)
# movie_lists[5] = "The Amazing Spider-Man 2"
movie_lists.append("The Amazing Spider-Man 2")
movie_lists.insert(1, "The Legend of Zoro")
print(movie_lists)

movie_lists.reverse()
print(movie_lists)

movie_lists.extend(["King Kong", "Evan Almighty", "47 Ronin"])
print(movie_lists)

movie_lists.remove("47 Ronin")
print(movie_lists)

movie_lists.remove("pacific rim")