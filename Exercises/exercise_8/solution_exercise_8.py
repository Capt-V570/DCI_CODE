#############################################
########## FIND Function in Python ##########
#############################################

print("""***************************
******** Find NEMO ********
***************************""")


#word_to_search = "Nemo"

# def find_text():
#     user_input = ""
#     word_to_search = "Nemo"
#     start_point = user_input.index("Nemo")
#     return user_input[start_point]

# word_to_search = "Nemo"
# nemo_found = ""

# while nemo_found:
#     user_input = str(input("Enter a Text with word 'Nemo', here: "))
#     if user_input == "End":
#         break
#     elif user_input != word_to_search:
#         print("I can't find Nemo :(")
#     elif user_input == word_to_search:
#         print("I found Nemo at", find_text() + "!")
#     else:
#         print("whatever")

def finding_Nemo():
    while finding_Nemo():
        user_input = str(input("Enter a Text with word 'Nemo' in it, here: "))
        index = user_input.find("Nemo")
        if user_input == "End":
            break
        elif index == -1:
            print("I can't find Nemo :(")
        else:
            print(f"I found Nemo at {index}!")

finding_Nemo()
print()

# STILL TO MODIFIY