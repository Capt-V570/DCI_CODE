######################################################
############### DATETIME EXPLAINATION ################
######################################################


from datetime import datetime           # to import the datetime module
from datetime import date               # to import the date module

print(datetime.today())                 # returns current date and time 

print(date.today())                     # returns the current date only

date_as_string = "2022-09-15"

print(date.fromisoformat(date_as_string))

# let's create some datetime objects

