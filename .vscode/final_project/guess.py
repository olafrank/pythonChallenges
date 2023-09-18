from random import randint

HARD_LEVEL=5
EASY_LEVEL=10

def check_guess(guess,answer,turn):
    if guess>answer:
        print("Too High")
        return turn-1
    elif guess<answer:
        print("Too low")
        return  turn-1
    else:
        print(f"you win,you guess {answer} ")    

def set_difficulty():
    level=input("choose a difficulty level,Type 'easy' or 'hard' : ")
    if level =="easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL    
            

def game():
    print("Welcome to the number Guess Game")
    print("I am thinking of a number between 1 and 100")

    answer=randint(1,100)
    print(f"{answer}")
    turn=set_difficulty()
    

    guess=0
    while guess!=answer:
        print(f"you have {turn} left")
        guess=int(input("make a guess: "))

        turn=check_guess(guess,answer,turn)
        if turn==0:
            print("You have run out of live,YOU LOOSE")
            return
        elif guess!=answer:
            print("guess again")

game()

            
            




