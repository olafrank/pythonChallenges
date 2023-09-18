print("welcome to the rollercoaster")

height = int(input("what is your height in cm?"))
bill = 0

if height >= 120:
    print("you can ride the rollercoaster")
    age = int(input('what is your age?'))
    if age < 12:
        bill = 5
        print('child ticket are $5.')
    elif age <= 18:
        bill = 7
        print('youth ticket are $7.')
    elif age >= 45 and age <= 55:
        print("you can have a free ride")
    else:
        bill = 12
        print("Adult tickets are 12.")
    want_photo = input("do youn want a photo taken? Y or N.")
    if want_photo == "Y":
        bill += 3
    print(f'your final bill is {bill}')
else:
    print('sorry,you have to grow taller before you can ride')
