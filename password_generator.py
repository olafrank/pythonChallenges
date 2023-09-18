import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = ['!', '#', '&', '$', '(', ')', '.', '/', '+']

print('Welcome to the pyPassword Generator')
nr_letters = int(input(f'How many letters would\n'))
nr_numbers = int(input(f'How many numbers would\n'))
nr_symbols = int(input(f'How many symbols would\n'))

# password = ''

# for char in range(1, nr_letters+1):
#     password += random.choice(letters)

# for char in range(1, nr_numbers+1):
#     password += random.choice(numbers)

# for char in range(1, nr_symbols+1):
#     password += random.choice(symbol)

# print(password)


# HARD LEVEL
password_list = []

for char in range(1, nr_letters+1):
    password_list.append(random.choice(letters))

for char in range(1, nr_numbers+1):
    password_list += random.choice(numbers)

for char in range(1, nr_symbols+1):
    password_list += random.choice(symbol)

random.shuffle(password_list)

password_string = ''

for char in password_list:
    password_string += char

print(f'your password is: {password_string}')



