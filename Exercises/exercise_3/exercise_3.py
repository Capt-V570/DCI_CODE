######################################
### Task 1 - basic math operations ###
######################################

# Your task is to write a program which asks the user three times for a number. 
# If number is even print ‘Even number’, else print ‘Odd number’.

# Hint: you can use for or while loop to perform the same operation more than once!

# Some of your results could look like this:
# Enter number: 123
# Odd number
# Enter number: 32
# Even number
# Enter number: 121234
# Even number


print(" ######################## \n ######## Task 1 ######## \n ########################")




for i in range(0, 3):
    x = input("Enter any Number :" )
    if (int(x) % 2) == 0:
        print("This is an EVEN Number")
    else:
        print("This is an ODD Number")



#######################################################
### Task 2 - printing numbers with range() function ###
#######################################################

# Your task is to write a program which asks the user about number of arguments in range() function.
# If number is 1 program asks for another number and then prints digits from range() function with given number.
# If number is 2 program asks for two numbers and then prints digits from range() function with given range.
# If number is 3 program asks for three numbers and then prints digits from range() function with given range and given step.

# Execution: 


print(" ######################## \n ######## Task 2 ######## \n ########################")


num = int(input("Enter a Number: "))
steps = int(input("Enter a number of steps interval (range from 1 to 3): "))

for i in range(0, num+1, steps):
    print(i)
else:
    print("Task finished")



#############################################
### Task 3 - finding divisors of a number ###
#############################################


# Your task is to write a program which prints all the divisors of a number. 
# The number comes from the user's input.

print(" ######################## \n ######## Task 3 ######## \n ########################")

number = int(input("Enter a Number :"))

for i in range(2, number+1, 1):
    if number % i == 0:
        print(i)
    


###################################
### Task 4 - check prime number ###
###################################


# Your task is to write a program to check if input number is a prime number.

print(" ######################## \n ######## Task 4 ######## \n ########################")

number = int(input("Enter a Number :"))
val = True

for i in range(2, number):
    if number % i == 0:
        val = False
if val == True:
    print(number, "is a Prime Number")
else: 
    print(number, "is not a Prime Number")


#########################
### Task 5 - FizzBuzz ###
#########################

print(" ######################## \n ######## Task 5 ######## \n ########################")

# multiple_3 = [n for n in range(1, 100) if n % 3 == 0]
# multiple_5 = [n for n in range(1, 100) if n % 5 == 0]


for i in range(1, 101):
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
    elif (i % 3 == 0):
        print("Fizz")
    elif (i % 5 == 0):
        print("Buzz")
    else: 
        print(i)



##################################
### Task 6 - Divisible Numbers ###
##################################

# multiple_5 = [n for n in range(1000, 2001) if n % 5 == 0]

for i in range(1000, 2001):
    if (i % 7 == 0) and (i % 5 != 0):
        print(i)

