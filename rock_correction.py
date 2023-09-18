import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
game_images = [rock, paper, scissors]


user_choice = int(
    input('what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor: '))
if user_choice >= 3 or user_choice < 0:
    print('invalid number,you lose')
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print('computer chose: ')
    print(game_images[computer_choice])
    if user_choice == 0 and computer_choice == 2:
        print('you win')
    elif computer_choice == 0 and user_choice == 2:
        print('you lose')
    elif computer_choice > user_choice:
        print('you lose')
    elif user_choice > computer_choice:
        print('you win')
    elif computer_choice == user_choice:
        print('it a draw')
    elif user_choice >= 3 or user_choice < 0:
        print('invalid number')
