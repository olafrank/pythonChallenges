print("welcome to tip calculator")

total = input("what was the total bill? $")

tip = input('what percentage tip would you like to give? 10,12, or 15? ')

tip_percent = int(total)*int(tip)/100

tip_total = round(tip_percent, 2)

people_split = input('how many people to split the bill? ')

total_payment = tip_total/int(people_split)

pay = round(total_payment, 2)

print(f"each person should pay:{pay}")
