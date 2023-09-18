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

choice_list = [rock, paper, scissors]

choice = input('what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor: ')

if choice == "0":
    print('You Choose')
    print(rock)
    print('computer choose: ')
    computer_choice = random.choice(choice_list)
    print(computer_choice)
elif choice == "1":
    print('You Choose')
    print(paper)
    print('computer choose: ')
    computer_choice = random.choice(choice_list)
    print(computer_choice)
elif choice == "2":
    print('You Choose')
    print(scissors)
    print('computer choose: ')
    computer_choice = random.choice(choice_list)
    print(computer_choice)

