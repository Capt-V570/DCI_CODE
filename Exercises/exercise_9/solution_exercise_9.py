#############################################
#########  CAPS LOCK DAY is over!  ##########
#############################################

print("""*******************************
**** Normalize a Sentence *****
*******************************""")

var1 = "CAPS LOCK DAY IS OVER",
var2 = "today is not caps lock day.",
var3 = "let us stay calm, no need to panic."
variables = (var1, var2, var3)

user_input = str(input("Enter a text to normalize and capitalize, here: "))

def normalize(variables, user_input):
    #logic of normalize function
    if user_input == variables:
        return f"{variables.lower().capitalize()}!"
    elif user_input != "End":
        return f"{user_input.lower().capitalize()}!"
    else:
        return "This is not a valid input"

normalizing = ""

while normalizing:
    user_input = str(input("Enter a text to normalize and capitalize, here: "))
    if user_input != "End":
        print(normalize())
    elif user_input == variables:
        print(normalize())
    elif user_input == "End":
        break
    else:
        break


# STILL TO FINISH
    