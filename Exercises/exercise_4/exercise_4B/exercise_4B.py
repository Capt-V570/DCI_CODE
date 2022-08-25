########################################################
################## length() in Python ##################
########################################################

# Write a program that detects if a string has an even/odd number 
# of characters and prints "even" or "odd" accordingly.

from colorama import *
from art      import *

tprint(text = "Length of Strings", font = "bubble")

user_input = ""           # to say to the program that there will be a string input (which we don't know the value)

while user_input.lower() != "end":
    user_input = str(input("Enter your message here to check whether its lenght is composed of Odd or Even numbers: "))
    if (len(user_input) % 2) != 0:
        print("The lenght of your text is Odd:", len(user_input), "characters")
    else:
        print("The lenght of your text is Even:", len(user_input), "characters")