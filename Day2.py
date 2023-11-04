#Quiz 1

# two_digit_number = input('Enter a two digit number: ')

# first_digit = int(two_digit_number[0])
# second_digit = int(two_digit_number[1])

# result = first_digit + second_digit

# print(result)

# -----------------------------
#Quiz 2 

# height = float(input('Enter your height :  '))
# weight = int(input('Enter your weight : '))


# BMI = int(weight / height ** 2)

# print(f'Your BMI is : {BMI}')


# ----------------------------------------------


# Quiz 3 
# LIFE = 90
# age = int(input('Enter your Age :  '))

# year = LIFE - age

# weeks = year * 52

# days = year * 365


# print(f'Your have {weeks} Weeks or {days} Days  left')



# -------------------------------------------------------


# Project - Day 1 

print('Welcome to the Tip Calculator ')

bill = float(input('Enter the total bill amount:  '))

tip = int(input('What is  percentage tip you want to give :  '))

num_person = int(input('How many are you :  '))

tip_percent = tip / 100
total_tip_amount= bill * tip_percent
total_bill = bill + total_tip_amount

tip_per_person = total_bill/num_person


print(f'Each person is to pay {round(tip_per_person,2)}')

