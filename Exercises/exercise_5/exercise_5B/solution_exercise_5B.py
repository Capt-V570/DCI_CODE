####################################################
############# CONCATENATION OF STRINGS #############
####################################################

print("""********************************* 
*** FUNCTION 'INATOR' PROGRAM *** 
*********************************""")


def terminator(user_input):
    suffix_con = "inator"
    suffix_vow = "-inator"
    vowels = ("a", "e", "i", "o", "u")
    if user_input.endswith(vowels):
        return f"{user_input}{suffix_vow} {str(len(user_input))}000"
    else:
        return f"{user_input}{suffix_con} {str(len(user_input))}000"

user_input = str(input("Enter a cool name: "))

while user_input != "End":
    print(terminator(user_input))
    user_input = str(input("Enter a cool name: "))