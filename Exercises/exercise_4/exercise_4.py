

#####################################
### Task 1 - comparison operators ###
#####################################

# Your task is to write a program which asks the user in 3 instances
# about two integer numbers to compare.
# use 'while' loop
# Create at least ten comparisons!

print(" ######################## \n ######## Task 1 ######## \n ########################")

print("Enter two numbers to compare ")


# 0 < threshold < 1000
threshold = 100
big_number = False

# loop
for i in range(3):
    num1 = int(input("Enter first number here: "))
    num2 = int(input("Enter second number here: "))

    if (num1 == num2):
        print("These numbers are equal")
    if (num1 != num2):
        print("These numbers are NOT equal")
    if (num1 > num2):
        print("First number is greater than second number")
    if (num1 < num2):
        print("Second number is greater than first number")
    if (num1 >= threshold) and (num2 >= threshold):
        print("Both numbers are big! \n big_number is set to True")
        big_number = True
    if (num1 <= threshold) and (num2 <= threshold):
        print("Both numbers are NOT big! \n big_number is set to False")
        big_number = False
        while big_number is False:          # something is not going right here :(
            if (num1 < threshold):
                print("First number is NOT big! \n big_number is set to False")
                big_number = False
            if (num2 < threshold):
                print("Second number is NOT big! \n big_number is set to False")
                big_number = False
            break



##########################################################
### Task 2 - convertion month name to a number of days ###
##########################################################

# Your task is to write a Python program to convert month name to a number of days.

print(" ######################## \n ######## Task 2 ######## \n ########################")

months = [
    "January", 
    "February", 
    "March", 
    "April", 
    "May", 
    "June", 
    "July", 
    "August", 
    "September", 
    "October", 
    "November", 
    "December"]

print("Months of the Year: " + str(months))
user_input = str(input("Input the name of the Month: "))

if user_input == months[0] or user_input == months[2] or user_input == months[4] or user_input == months[6] or user_input == months[7] or user_input == months[9] or user_input == months[11]:
    print("This month has 31 days")
elif user_input == months[3] or user_input == months[5] or user_input == months[8] or user_input == months[10]:
    print("This month has 30 days")
elif user_input == months[1]:
    print("This month has 28 days (29 days on a Leap Year // it means: once every 4 years February has 29 days)")
else: 
    print("This is not a valid input! Please try again.")