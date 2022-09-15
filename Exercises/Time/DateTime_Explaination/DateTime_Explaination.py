######################################################
############### DATETIME EXPLAINATION ################
######################################################


from datetime import datetime           # to import the datetime module
from datetime import date               # to import the date module

print(datetime.today())                 # returns current date and time 

print(date.today())                     # returns the current date only

date_as_string = "2022-09-15"

print(date.fromisoformat(date_as_string))

# How to create a datetime object with time:
date_1 = datetime(2022, 1, 26, 10, 30, 59)

print(date_1)

# How to create a datetime object with just the date:
date_2 = date(2022, 1, 26)

print(date_2)