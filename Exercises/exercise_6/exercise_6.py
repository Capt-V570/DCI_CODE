#################################
### Task 1 - fix the FizzBuzz ###
#################################

# Your Task is to fix program non-working correctly. The FizzBuzz problem:
# For all integers between 1 and 99 (include both):

# print 'fizz' for multiples of 3;
# print 'buzz' for multiples of 5;
# print 'fizzbuzz' for multiples of 3 and 5.


print(" ############## \n ### Task 1 ### \n ############## ")

three_mul = 'fizz'      #1st bug: misses a quotation mark (')
five_mul = 'buzz'
num1 = 3
num2 = 5                #2nd bug: number must be number 5, (was 4)
max_num = 100
   
for i in range(1,max_num):
    # % or modulo division gives you the remainder 
    
    if i%num1 == 0 and i%num2 == 0:     #6th bug: wrong order in the if statement #7th bug: due to 6th bug, the statement must start with 'if', not an 'elif'  #### NOTE: The condition that is expected to happens for the least amount of times must go above all others.
        print(i, three_mul+five_mul)    #5th bug: print statement must be indentend
    elif i%num1 == 0:                   #3rd bug: add another (=) to the statement for running the comparision  #4th bug: 
        print(i, three_mul)
    elif i%num2 == 0:
        print(i, five_mul)

# I counted 7 bugs: cool!


#################################
### Task 2 - summing integers ###
#################################

# Your task is to fix program non-working correctly. The problem:

# sum integers from 1 to 5 using while loop
# calculate what result should be and what you get after running the program

print(" ############## \n ### Task 2 ### \n ############## ")

n = 5
number = 1
sum = 0
while number < n + 1:
    print(number)           # this is just to visualize the changin variables
    sum = sum + number      # variable "number" will be added to the sum at every iteration    ## alt. ver.: could also have been written (sum += sum)
    number = number + 1
print("Sum =", sum)


##############################################
### Task 3 - summing integers with range() ###
##############################################

print(" ############## \n ### Task 3 ### \n ############## ")

n = 5
sum = 0

for num in range(n):      # either we put (n+1) in the range...
    print(num)              # this is just to visualize the changin variables
    sum += num +1           # ...or we add '+1' to num        
print("Sum =", sum)



##################################
### Task 4 - printing in loops ###
##################################

print(" ############## \n ### Task 4 ### \n ############## ")

print(" >>> Program 1 <<< ")

for x in range(3):      # add colon (:) at the end of the for loop
    print(x)



print(" >>> Program 2 <<< ")

for j in range(5):
    print("This is loop number", j)     # add comma (,) before the (j) in the print statement and j is a variable (not string)


print(" >>> Program 3 <<< ")

x = 10              # variable need always to be before 'while loop'

while x > 0:
    print(x)
    x -= 1
    
print(" >>> Program 4 <<< ")

countdown = 5       #bug: the countdown should start from 5 (not 0, as it was). So the variable is to be changed to 5

while countdown:        # could also been written more clearly while countdown != 0
    print(f"{countdown}")
    countdown -= 1
else:
    print("Start!")


#######################################
### Task 5 - summing three integers ###
#######################################

# Your task is to fix program non-working correctly. The problem:

# sum the three prompted integers
# however, if two values are equal sum should be zero
# calculate what result should be and what you get after running the program

print(" ############## \n ### Task 5 ### \n ############## ")

x = int(input("First number: "))        # 1bug: add integer and append the input within parenthesis '( ... )'
y = int(input("Second number: "))       # 2bug: add integer and append the input within parenthesis '( ... )
z = int(input("Third number: "))        # 3bug: add integer and append the input within parenthesis the first '( ' parenthesis

if x == y or y == z or x == z:          # 4th bug: the equals (=) must be two. in order for python to compare. # 5th bug: add condition ('or x == z')
    result = 0
else:
    result = x + y + z              #bug: change name of variable 'sum', to 'result'
print("Calculated sum is ", result)



#####################################
### Task 6 - summing two integers ###
#####################################

# Your task is to fix program non-working correctly. The problem:

# sum the two prompted integers
# however, if the sum is between 15 to 20 (both numbers included) it should be calculated to 20
# calculate what result should be and what you get after running the program


print(" ############## \n ### Task 6 ### \n ############## ")

x = int(input("First number: "))        # 1st bug: input value should be formatted to integer
y = int(input("Second number: "))       # 2nd bug: input value should be formatted to integer

result = x + y

if result > 15 and result < 20:         # 3rd bug: change the 'or', to 'and'  /// # alternative version: 'if 15 <= result <= 20'
    result = 20
print("Calculated sum is ", result)


###################################
### Task 7 - swapping variables ###
###################################

# Your task is to fix program non-working correctly. The problem:

# prompt two values and assign them to variables a and b
# write the Python program to swap these two variables
# calculate what result should be and what you get after running the program


print(" ############## \n ### Task 7 ### \n ############## ")

a = input("First value: ")            # 1st bug: remove int and add 'input'
b = input("Second value: ")           # 2nd bug: remove int and add 'input'

print("Before swapping: a =", a, ", b = ", b)

temp = a
a = b
b = temp            # 3rd bug: was missing to store the b variable as temporary variable

print("After swapping: a =", a, ", b = ", b)



###################################
### Task 8 - max and min values ###
###################################

# Your task is to fix program non-working correctly. The problem:

# prompt three float numbers and determine the largest and the smallest one
# calculate what result should be and what you get after running the program

print(" ############## \n ### Task 8 ### \n ############## ")

x = input("First number: ")         # 1st bug: remove one of the two (=) for storing the variable
y = input("Second number: ")         # 2nd bug: remove one of the two (=) for storing the variable
z = input("Third number: ")         # 3rd bug: remove one of the two (=) for storing the variable

print("The maximum value is ", max(x, y ,z))  # 4th bug: add function 'max' before parenthesis      
print("The minimum value is ", min(x, y ,z))     # 5th bug: replace function 'abs' with 'min' before parenthesis



###########################
### Task 9 - convertion ###
###########################

# Your task is to fix program non-working correctly. The problem:

# prompt value from the user and assign it to some variable
# if given value is 0 (zero) convert it to False and if given value is 1 convert it to True
# display results

print(" ############## \n ### Task 9 ### \n ############## ")

x = input("Type your value: ")  #bug: adding a quotation mark (") at the end, to close the string.

if x == "0":    # bug: here the 0 is not an integer
    x = False   # bug: F of false must be capitalized
elif x == "1":    # bug: add one more (=) to let python compare to the value. Otherwise is a variable (with only one equal =)  # bug: add quotation mark for 1 as in this case it is a value not integer.
    x = True    # bug: T of true must be capitalized
else:
    pass        # bug: 'pass' must be indentend

print("Your entered value is now ", x)



##################################
### Task 10 - divisible number ###
##################################

# Your task is to fix program non-working correctly. The problem:

# accept (prompt) two integers values from the user
# check whether a first number is divisible by second number and vice versa
# display results

print(" ############### \n ### Task 10 ### \n ############### ")

x = int(input("First number: "))    # bug add integer for formatting the variable
y = int(input("Second number: "))   # bug add integer for formatting the variable

if x % y == 0:      # bug: only one modulus (%) is needed. + # bug: comparision must be expressed as (== 0), rather than (>= 0)
    print("First number is divisible by second number, result =", (x / y))
elif y % x == 0:    # bug: only one modulus (%) is needed  + # bug: comparision must be expressed as (== 0), rather than (>= 0)
    print("Second number is divisible by first number, result =", (y / x))
else:
    print("Numbers are non-divisible!")     # typo: divisible (not 'divisable' :P) ....

# exercise finished