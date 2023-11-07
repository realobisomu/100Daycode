# # Quiz 1

# print('Welcome to rollercoaster ')
# height = int(input('What is your height in cm :  '))
# age = int(input('Enter your age:  '))
# bill = 0

# if height >= 120 :
#     print('You can ride')
#     if age < 12:
#         bill =+5
#         print('Please pay $5')
#     elif age <= 18:
#         bill=+7
#         print('Please pay $7')

#     elif age >= 45 and age <= 55:
#         print('Enjoy a free ride on the house')
#     else:
#         bill+=12
#         print('Please pay $12')


#     want_photo= input('Do you want a photo taken : Y or N. :\n ')
#     if want_photo == 'Y':
#         bill +=3

#     print(f'Your bill is {bill}')

# else:
#     print('Sorry, too short')

# # -----------------------------------------------------------


# # Quiz 2


# # num = int(input('Enter number:  '))


# # if num % 2 == 0:

# #     print('Number is an even number ')
# # else:
# #     print('Number is an odd number ')


# # --------------------------------------------------------


# # Quiz 3


# # height = float(input('Enter your height:  '))

# # weight = int(input('Enter your weight :  '))


# # bmi = weight / (height ** 2)

# # print(f'Your BMI: {bmi}')

# # if bmi < 18.5:

# #     print('You are underweight')


# # elif bmi >18.5 and bmi < 25 :
# #     print('Normal weight ')


# # elif bmi > 25 and bmi < 30 :
# #     print('Slight overweight')

# # elif bmi > 30 and bmi < 35 :
# #     print('Obese')

# # else:
# #     print('Clinically Obese')


# # ------------------------------------------------


# # Quiz 4


# # year = int(input('Enter year :  '))

# # if (year % 4 == 0):
# #     if (year % 100!=0):
# #         print('leap year')
# #     elif (year % 400 == 0):
# #         print('Year is a leap year ')
# #     else:
# #         print('Not a leap year ')
# # else:
# #     print('Sorry not a leap year')


# # -----------------------------------------------


# # if (year % 4 == 0) and (year % 100 != 0) and (year % 400 == 0):
# #     print('Year is a leap year')

# # else:

# #     print('Year is not a leap year ')

# # ---------------------------------------------------------------


# # Quiz 5


# # print('\nThank you for choosing Python Pizza Deliveries \n')

# # size = input(' What size of pizza do you want : (S, M, L): ')
# # add_pepperoni = input('Do you want pepperoni: (Y or N): ')
# # extra_cheese = input('Do you want extra cheese :  (Y or N): ')

# # pizza_price = 0

# # if size == 'S':
# #     pizza_price+= 15


# # elif size == 'M':
# #     pizza_price += 20


# # elif size == 'L':
# #     pizza_price += 25


# # if add_pepperoni == 'Y' and size == 'S':
# #     pizza_price += 2
# # else:
# #     pizza_price+=3


# # if extra_cheese == 'Y':
# #     pizza_price+=1


# # print(f'\nTotal bill ${pizza_price}\n')


# # ----------------------------------------------------


# Quiz 6

# print('The love calculator is calculating your score ...')


# name1 = input('What is your name:')
# name2 = input('What is their name:')

# combine_names = name1 + name2

# char_in_true_counter = 0
# char_in_love_counter = 0

# for i in combine_names.upper():
#     if i in 'TRUE':
#         char_in_true_counter+=1

#     if i in 'LOVE':
#         char_in_love_counter +=1

# result = str (char_in_true_counter)  + str(char_in_love_counter )


# if int(result) < 10 or int(result) > 90:
#     print(f'your score is {result} , you go togather like coke and mentos')

# elif int(result) > 40 and int(result)<50:
#     print(f'Your score is {result}, you are alright togather')

# else:
#     print(f'Your score is {result}')

# ////////////////////////////////////////////////////////////////////////


# Final Project

print('Welcome to treasure Island \n')
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')


name = input('Enter your name :  ')

game_start = input(
    f'{name}, are you ready to make a journey of a life time : (Y or N):  ').lower()


if game_start == 'y':
    print('Your mission is find the hidden treasure :  ')
    first_turn = input(
        'Your task is to locate the hidden treasure:  Enter right or left to begin (R or L): \n  ').lower()
    if first_turn == 'l':
        second_turn = input(
            'You have come to a riverside . Enter  (W) to wait for a boat or (S) to swim across :  ').lower()
        if second_turn == 's':
            third_turn = input(
                'You may it across, to a two doorway , one marked (R) and the other is marked black (B): ').lower()
            if third_turn == 'r':
                print('You found it . You win.')
            else:
                print('Game over , falled into a fire')
        else:
            print('The ship capsized, GAME OVER')

    else:
        print('You falled into a ditch .GAME OVER')
else:
    print('Come back , when  you are ready. !!!')
