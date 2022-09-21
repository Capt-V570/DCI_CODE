####################################
####### DateTime - Task 1 ##########
####################################

from datetime import datetime
import time

current_datetime = datetime.now()


print(dir(current_datetime))      # print the dir means The dir() function returns all properties and methods of the specified object, without the values. This function will return all the properties and methods, even built-in properties which are default for all object.


# Task 1
print("###### Task 1 ######")

print(current_datetime.year)


# Task 2
print("###### Task 2 ######")

some_date = datetime(2021, 7, 14)

current_date = datetime.isoweekday(some_date)

print(current_date)

# Task 3
print("###### Task 3 ######")
