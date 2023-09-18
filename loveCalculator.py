print("Welcome to the Love Calculator")

name1 = input("What is your name?\n").lower()
name2 = input("What is their name?\n").lower()


total_name = name1+name2

t = total_name.count('t')
r = total_name.count('r')
u = total_name.count('u')
e = total_name.count('e')

true = t+r+u+e

l = total_name.count('l')
o = total_name.count('o')
v = total_name.count('v')
e = total_name.count('e')

love = l+o+v+e

truelove = true+love


if truelove < 10 or truelove > 90:
    print(f"your score is {truelove} you go together like coke and mento")
elif truelove >= 40 and truelove <= 50:
    print(f'your score is {truelove} you are alright together')
else:
    print(f'your score is {truelove}')
