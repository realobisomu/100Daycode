# Quiz 1

# print('\n Student Height Calculator.\n')
# total_height = 0
# student_height = []
# while True:
#     studentInput = float(input('Enter your height: '))
#     student_height.append(studentInput)
#     cont = input('Do you wish to continue: ').lower()
#     if cont == 'y':
#         continue
#     else:
#         break

# for i in student_height:
#     total_height += i


# print(total_height)
# print(len(student_height))
# result = total_height / len(student_height)

# print(f'The average students height is :  {result}')


# Quiz 2
# print('\n Highest score picker.....\n')

# student_score = []
# high_score = 0
# while True:
#     studentInput = float(input('Enter your height: '))
#     student_score.append(studentInput)
#     cont = input('Do you wish to continue: ').lower()
#     if cont == 'y':
#         continue
#     else:
#         break


# for i in student_score:
#     if i > high_score:
#         high_score = i


# print(f'The highest score is : {high_score}')


# Quiz 3

# print('Range project......')

# start_num = int(input('Enter the starting number:  '))
# end_num = int(input('Enter the end number:  '))


# total_num = 0

# for num in range(start_num, end_num+1):
#     if num % 2 == 0:
#         total_num += num


# print(f'Total sum of even numbers:  {total_num}')


# Quiz 4

# import random


# print('\nproject :  FizzBuzz \n')

# for num in range(1, 101):
#     if num % 3 == 0 and num % 5 == 0:
#         print('Fizz')
#     elif num % 5 == 0:
#         print('Buzz')
#     elif num % 3 == 0:
#         print('FizzBuzz')
#     else:
#         print(num)


# Project Day-5

import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print('Password Generator ')

num_letters = int(input('Enter the number of letters:  '))
num_symbols = int(input('Enter the number of symbols:  '))
num_numbers = int(input('Enter the number of numbers: '))

password_list = []

for char in range(1, num_letters+1):
    password_list.append(random.choice(letters))
for char in range(1, num_symbols+1):
    password_list.append(random.choice(symbols))
for char in range(1, num_numbers+1):
    password_list.append(random.choice(numbers))

password_shuffle = random.shuffle(password_list)

password = ''

for char in password_list:
    password += char


print(f'Your password is {password}')
