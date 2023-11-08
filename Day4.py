# Quiz 1

# import random


# names = ['Angela', 'Ben', 'Jenny', 'Michael', 'Cloe']

# num_items = len(names)

# random_choice = random.randint(0, num_items-1)

# person_to_pay = names[random_choice]


# print(f' {person_to_pay}  is going to buy the meal today. ')


# -------------------------------


# Quiz 2


# line1 = [' ', ' ', ' ']
# line2 = [' ', ' ', ' ']
# line3 = [' ', ' ', ' ']

# map = [line1, line2, line3]


# print('Hiding your treasure: X makes the spot')

# position = input('Enter position:  ')
# letter = position[0].lower()
# abc = ['a', 'b', 'c']
# letter_index = abc.index(letter)
# number_index = int(position[1])-1
# map[number_index][letter_index] = 'X'


# print(f'{line1}\n{line2}\n{line3}')


# //////////////////////////////////////////////////////////////////////////

# Project of Day 4
import random
paper = '📄'
scissor = '✂️'
rock = '🪨'

user_input = int(input('Enter 0 - Rock , 1 - Paper and 2 - Scissors:\n '))

if user_input < 0 or user_input >= 3:
    print('Enter a valid input')
    exit()

else:
    game_image = [rock, scissor, paper]
    print()
    print(game_image[user_input])

computer_input = random.randint(0, 2)
print(f'\nComputer choice:\n')
print()
print(game_image[computer_input])

if user_input == 0 and computer_input == 2:
    print('You win')
elif computer_input == 0 and user_input == 2:
    print('You lose')
elif computer_input > user_input:
    print('You Lose')
elif user_input > computer_input:
    print('You win')
elif computer_input == user_input:
    print('Its is a draw')
elif user_input < 0 or user_input >= 3:

    print('Enter a valid input')
