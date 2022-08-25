###################################################
################## STORY PROGRAM ##################
###################################################

from colorama import *
from art      import *


tprint(text="STORY PROGRAM", font="random")

print(" ################################################### \n ################################################### \n -----> Youre in a dark alley. Where do you go? ... \n ...................................................")
print(" -----> Controls: \n --> (1) left \n --> (2) straight \n --> (3) right \n --> (4) go back")
choice = input("\n " + "Choose your option: ")
game = True

while game:
    if choice == "1":
        print("You go left and die")
    elif choice == "2":
        print("You go straight and now there is another crossing")   # continue tree here
    elif choice == "3": 
        print("You go right and now theres a wall")
    elif choice == "4":
        print("You go back and now you're safe")
    else:
        print("You just die for inaction")
    break