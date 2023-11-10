# # Quiz 1

# def greet_with(name, location):
#     print(f'Hello {name}')
#     print(f'What is the weather like in {location}')


# greet_with(name='James', location='USA')


# ------------------------------------------------------------------

# Quiz 2

# import math


# def paint_calc(height, width, cover):
#     result = (height * width) / cover
#     return math.ceil(result)


# test_h = int(input('Enter the wall height : '))
# test_w = int(input('Enter the wall width:  '))
# coverage = 5

# print(
#     f'You need {paint_calc(height=test_h, width=test_w, cover=coverage)} of paint')

# -------------------------------------------------------------


# Quiz 3

# import random


# print('Prime number checker ')


# def prime_checker(number):
#     if number % number == 0 and number % 1 == number:
#         print(f'{number} is a prime number')
#     else:
#         print(f'{number} is not a prime')


# user_input = random.randint(1, 100)

# prime_checker(number=user_input)


# ------------------------------------------------------------

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         cipher_text += alphabet[new_position]
#     print(f"The encoded text is {cipher_text}")


# def decode(plain_text, shift_amount):
#     decoded_text = ''
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         decoded_text += alphabet[new_position]

#     print(f'The decoded text is {decoded_text}')


# def display():

#     print("""
#  ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
# a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
# 8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88
# "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
#  `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
#             88             88
#            ""             88
#                           88
#  ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
# a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
# 8b         88 88       d8 88       88 8PP""""""" 88
# "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
#  `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
#               88
#               88
# """)

#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))

#     direction = input(
#         "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
#     if direction == 'encode':
#         encrypt(plain_text=text, shift_amount=shift)
#     elif direction == 'decode':
#         decode(plain_text=text, shift_amount=shift)
#     else:
#         print('Wrong command')


# display()


# direction = input(
#     "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))


def caesar(command, plain_text, shift_amount):
    cipher_txt = ''
    for letter in plain_text:
        if command == 'encode':
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position+shift_amount
                cipher_txt += alphabet[new_position]
            else:
                cipher_txt += letter
        elif command == 'decode':
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position-shift_amount
                cipher_txt += alphabet[new_position]
            else:
                cipher_txt += letter
        else:
            print('Wrong command')

    return cipher_txt


def display():
    print("""           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""")
    print()
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    print(
        f'The message is {caesar(command=direction, plain_text=text, shift_amount=shift)}')


cont = True

while cont:
    display()
    cont_input = input('\n Do you wish to continue: (Y or N) ').lower()
    if cont_input == 'y':
        continue
    else:
        cont = False
        print('\n BYE')
        break
