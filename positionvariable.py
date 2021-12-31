def display(*args):
    print(args)

display()
display("Python")
display("Pyhon", "Ruby")

languages_list = ["Python", "Java", "C++", "C#", "JavaScript"]
display(languages_list)
display(*languages_list)

languages_list = ("Python", "Java", "C++", "C#", "JavaScript")
display(*languages_list)