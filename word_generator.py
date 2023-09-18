import random

word_list = ["ardvark", "baboon", "camel"]
word_pick = random.choice(word_list)

print(f'the chosen word is {word_pick}')

display = []

for letter in word_pick:
    display += "_"


end_game = False
while not end_game:

    guess = input('pick a letter: ').lower()

    for position in range(len(word_pick)):
        letter = word_pick[position]
        if letter == guess:
            display[position] = letter
    print(display)
    if '_' not in display:
        end_game = True
        print('YOU WIN !!!')
