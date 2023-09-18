import random

names_string = input("give me everybody's names, seperated by a coma.")
names = names_string.split(",")

# num_items = len(names)
# name_choice = random.randint(0, num_items - 1)

# name_gen = names[name_choice]

name_gen = random.choice(names)

print(f'{name_gen} is gonna buy the meal today')
