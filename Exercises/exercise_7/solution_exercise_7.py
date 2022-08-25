###################################################
############ UPPER / lower in Python ##############
###################################################

"""
Overview:
The python string upper() method converts all characters of the string into uppercase. 
The python string lower() method converts all characters of the string into lowercase.

Task
Write a Python program to convert all the characters in a string to uppercase.
Write a Python program to convert all the characters in a string to lowercase.
"""





user_input = str(input("Enter your text here: " ))

uppering_lowering = True

while uppering_lowering:
    if user_input == "":
        print(user_input)
    else:
        print(user_input + "\n" + str(user_input.upper()) + "\n" + str(user_input.lower()))
    break