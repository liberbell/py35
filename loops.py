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
    print("Cat is %s and it weghts %s pounds." % (cat, weight))