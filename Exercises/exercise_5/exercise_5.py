##############################
### Task 1 - calculate sum ###
##############################

# Your task is to write a Python program to calculate the sum of three integers given (prompted) by user.
# If the values are equal then calculate triple value of their sum.
# Print out an appropriate message to the user.
'''
print(" ############## \n ### Task 1 ### \n ##############")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# create calculator

if num1 != num2 != num3:
    print("The sum is: ", (num1 + num2 + num3))
elif num1 == num2 == num3:
    print("The triple sum is: ", 3*(num1) + 3*(num2) + 3*(num3))
else:
    print("The sum is: ", (num1 + num2 + num3))



###################################
### Task 2 - get the difference ###
###################################

# Your task is to write a Python program to get the difference between a two given numbers (prompted by user).
# If the first number is greater than second then calculate double difference between numbers.
# Otherwise calculate the absolute difference between numbers.
# Print out an appropriate message to the user.

print(" ############## \n ### Task 2 ### \n ##############")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The result of 'subtraction' is: ", (num1 - num2))

if num1 > num2:
    print("The result of 'double difference' calculation is: ", 2*(num1) - 2*(num2))




###################################
### Task 3 - odd or even number ###
###################################

# Your task is to write a Python program to find whether a given number (prompted from the user) is even or odd. 
# Print out an appropriate message to the user.

print(" ############## \n ### Task 3 ### \n ##############")

num = int(input("Enter the number to check: "))

if num % 2 == 0:
    print((num), "is an even number!")
else:
    print((num), "is an odd number!")



############################
### Task 4 - circle area ###
############################

# Your task is to write a Python program which accepts (prompts) the float radius of a circle from the user and compute its area.
# Round the result to two decimals!
# Print out an appropriate message to the user.

print(" ############## \n ### Task 4 ### \n ##############")

rad_value = float(input("Input the radius of the circle: "))

import math

circle_area = (math.pow(rad_value, 2)) * math.pi

print("The area of the circle with radius ", rad_value, " is: ", round(circle_area, 2)) 



###############################
### Task 5 - guess a number ###
###############################

# # Your task is to write a Python program to guess a number between 1 to 9.
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

# Hint: you don't know the random module yet, so set your number to guess hard-coded in your program.

print(" ############## \n ### Task 5 ### \n ##############")


guess = True

while guess:
    user_input = int(input("Guess a number between 1 and 10 until you get it right: "))
    if user_input == 7:
        print("Well guessed!")
        guess = False
    else:
        continue

'''
#################################################
### Task 6 - Celsius to Fahrenheit conversion ###
#################################################

# Your task is to write a Python program to convert temperatures to and from Celsius, Cahrenheit.

# In the centigrade scale, which is also called the Celsius scale, water freezes at 0 degrees and boils at 100 degrees.
# In the Fahrenheit scale, water freezes at 32 degrees and boils at 212 degrees.

# Note : User should be prompted twice:

# - to enter a temperature;
# - to enter a shortcut for given scale (C for Celsius, F for Fahrenheit).

print(" ############## \n ### Task 6 ### \n ##############")

scale = str(input("Input the scale shortcut you'd like to convert (F - Fahrenheit, C - Celsius): "))
Temp_C = float(input("Input the value of Celsius temperature you'd like to convert: "))
Temp_F = float(input("Input the value of Fahrenheit temperature you'd like to convert: "))
converting = True

while converting:
    if scale == str("c").capitalize:
        print("The temperature in Fahrenheit is :", ((Temp_C * 1.8) + 32))
        converting = False
    if scale == str("f").capitalize:
        print("The temperature in Celsius is :", ((Temp_F * 9/5 ) + 32))
        converting = False
    else:
        break

###########ERROR######### To check again


########################
### Task 7 - pattern ###
########################

# Your task is to write a Python program to construct the following pattern. Upper part should be done in one line of code without using a loop.
# Lower part can be done with any kind of loop or also with one line of code and without loops.