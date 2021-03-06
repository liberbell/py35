for letters in ["W", "e", "l", "c", "o", "m", "e"]:
    print(letters)
    
for letters in "Welcome":
    print(letters)
    
var_string = "Welcome to New York"
for char in var_string:
    print(char)
    
for digits in "20":
    print(digits)
    
# for digits in 10:
#     print(digits)

for company in "Google", "Microsoft", "Apple", "Meta", "Oracle", "Amazon":
    print(company)
    
cats = ("Snowshoe", "Calico", "British Shorthair", "Siamese", "Persian")
for cat in cats:
    print("It`s a ", cat)
    
cats = ["Snowshoe", "Calico", "British Shorthair", "Siamese", "Persian"]
for cat in cats:
    print("It`s a ", cat)
    
cats_weight = [("Snowshoe", 15),
               ("Calico", 20),
               ("Persian", 12)]
for cat, weight in cats_weight:
    print("Cat is %s and it weights %s pounds." % (cat, weight))
    
for i, (cat, weight) in enumerate(cats_weight):
    print("Cat at index %d is a %s and it weights %s pounds." % (i, cat, weight))
    
price_history = [
    {"ticker": "AAPL", "close price": 148.00, "volume": 2000000, "data": "2021-12-14"},
    {"ticker": "AAPL", "close price": 149.00, "volume": 2000000, "data": "2021-12-15"},
    {"ticker": "AAPL", "close price": 150.00, "volume": 2000000, "data": "2021-12-16"},
]

# for price_data in price_history:
#     print(price_data)
    
for price_data in price_history:
    if price_data['close price'] >= 149:
        print(price_data)
        
game_scores = {'Bob': 9,
               'Alex': 6,
               'Eric': 8,
               'Ed': 10}
print(game_scores)
print(game_scores.keys())
print(game_scores.values())
print(game_scores.items())

for name in game_scores.keys():
    print(name)
for name in game_scores:
    print(name)
    
for score in game_scores.values():
    print(score)

characters = {"a", "b", "c", "d"}
for letter in characters:
    print(letter)
else:
    print("no character left.")

years = [2016, 2017, 2018, 2019, 2020, 2021]
for year in years:
    if year % 4 == 0:
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")