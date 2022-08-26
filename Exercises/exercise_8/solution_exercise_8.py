#############################################
########## FIND Function in Python ##########
#############################################

print("""***************************
******** Find NEMO ********
***************************""")

user_input = str(input("Enter a Text with word 'Nemo' in it, here: "))
word_to_search = "Nemo"

def find_text(user_input, word_to_search):
    start = user_input.index("Nemo")
    return user_input[start]

word_to_search = "Nemo"
nemo_found = ""

while nemo_found:
    user_input = str(input("Enter a Text with word 'Nemo', here: "))
    if user_input == "End":
        break
    elif user_input != word_to_search:
        print("I can't find Nemo :(")
    elif user_input == word_to_search:
        print("I found Nemo at", find_text() + "!")
    else:
        print("whatever")