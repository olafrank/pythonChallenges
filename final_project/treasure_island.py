print('''
          ,-------------------------------.
          |  Island                       |
          | .---------------------------. |
          | |,---'!!!!!!`...'!,.'!!!!!!!| |
          | |'',.,'!!!,--.!!!!!!!!,-'%%%| |
          | |`'!!!!!!;/|||\--'%%%%%%%%%%| |
          | |!!!!!!!,||/||\\%%%%%%%%%%%%| |
          | !!,-'%%%$;/||\\\\###-.%%%%%%| |
          | |%%%%,-$/|||\\|\\\.###)%%%%%| |
          | |%%%(p$$$$::$$$_$$$&&,%%%%%%| |
          | |%%%%%`-.$$pp,' ;,--'%%%%%%%| |
          | `---------------------------' |
          | Land                      7   |
          | .---------------------------. |
          | |            ,              | |
          | |           /(              | |
          | |          /  \             | |
          | |         (   ))            | |
          | |          `--'             | |
          | |___________________________| |
          |      Illus.Tony Szczudlo      |
          |tm&C1993-1994 WoTC,Inc. 335/350|
''')
print('welcome to Treasure Island.')
print('Your mission is to find the treasure')

choice1 = input(
    'you\'at a crossroad,where do you want to go "left" or "right" ').lower()

if choice1 == "left":
    choice2 = input(
        'you\'ve come to a lake.there is an island in the middle of the lake.Type "wait" to wait for a boat. type "swim" to swim cross: ' ).lower()
    if choice2 == "wait":
        choice3 = input("you arrived pick a door between red,yellow and blue: ").lower()
        if choice3=="red":
            print('game over didnt find the treasure ')
        elif choice3=="yellow":
            print("try again you almost found it")
        elif choice3=="blue":
            print('congratulation you found the treaure ')
        else:     
            print('try harder next timee')  
    else:
        print('game over')
else:
    print('game over')
