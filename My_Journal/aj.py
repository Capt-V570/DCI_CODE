import os
import datetime
from   colorama import *
from   art      import *

# initialize colorama
init()

# datetime variable
now = datetime.datetime.today().strftime("%H:%M:%S %d-%m-%Y")

# display and format Journal Title:
print(Fore.RED+"")
tprint("Fausto's Journal", font="random")
print(""+Style.RESET_ALL)

# display current Journal entry:  
new_entry = input("ENTER DIARY ENTRY HERE >>> ")
# here = os.getcwd().replace("\\","/") # defining path variable if you wanna use it within 'if' statement later (then 'if' statement will have to be modified too)

if os.getcwd() in new_entry:    # if entry contains the os path (buggy), don't save it
    print("")
elif new_entry != "":           # if entry is not empty, save it! 
    with open("journal.txt", "a") as file:
        file.write(now + " " + new_entry + "\n")
else: 
    print("")                   # if entry is empty, don't save.


