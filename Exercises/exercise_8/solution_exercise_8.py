#############################################
########## FIND Function in Python ##########
#############################################

print("""***************************
******** Find NEMO ********
***************************""")

def finding_Nemo():
    user_input = str(input("Enter a Text with word 'Nemo' in it, here: "))
    index = user_input.find("Nemo")
    if index == -1:
        print("I can't find Nemo :(")
    else:
        print(f"I found Nemo at {index}!")

finding_Nemo()
print()

# creating While Loop - TO CHECK AND CONTINUE
# nemoing = ""
# while nemoing:
#     finding_Nemo()
#     if user_input == "End":
#         break
#     else:
#         print()

