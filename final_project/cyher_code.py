alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# METHOD 2

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ''
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position+shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"The {cipher_direction}d text is {end_text}")


should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt,type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    result = input(
        "Type 'yes' if you want to continue or 'no' if you want to exit\n")
    if result == 'no':
        should_continue = False
        print('Goodbye')

# def encrypt(plain_text, shift_amount):
#     cyher_text = ''
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position+shift_amount
#         new_letter = alphabet[new_position]
#         cyher_text += new_letter
#     print(f'The encode message is {cyher_text}')


# def decrypt(cyher_text, shift_amount):
#     cyher_decryt = ''
#     for letter in cyher_text:
#         position = alphabet.index(letter)
#         new_position = position-shift_amount
#         new_letter = alphabet[new_position]
#         cyher_decryt += new_letter
#     print(f'The decode message is {cyher_decryt}')


# if direction == 'encode':
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == 'decode':
#     decrypt(cyher_text=text, shift_amount=shift)


# METHOD 1
# def caesar(text, shift, direction):
#     cyher_text = ''
#     if direction == 'encode':
#         for letter in text:
#             position = alphabet.index(letter)
#             new_position = position+shift
#             new_letter = alphabet[new_position]
#             cyher_text += new_letter
#         print(f"the encode message is {cyher_text}")
#     elif direction == 'decode':
#         for letter in text:
#             position = alphabet.index(letter)
#             new_position = position-shift
#             new_letter = alphabet[new_position]
#             cyher_text += new_letter
#         print(f"the decode message is {cyher_text}")


# caesar(text=text, shift=shift, direction=direction)
