
# Python Introduction

## Math operators

# In this exercise, we will focus on the usage of the basic math operators, including:  
 # - `+` (add), 
 # - `-` (subtract), 
 # - `*` (multiply),
 # - `/` (divide), 
 # - `%` (modulo), 
 # - `**` (power), 
 # - `//` (floor rounding).  

 # We will also focus on the use of useful math functions, including: 

# - `max()` (maximum value),
# - `min()` (minimum value),
# - `abs()` (absolute value),
# - `pow()` (value to the power of the value),
# - `ceil()` (rounds a number upwards to its nearest integer),
# - `floor()` (rounds a number downwards to its nearest integer).  
# > Hint: Two last functions must be imported form `math` module!

## 

############
## Tasks: ##
############

######################################
### Task 1 - basic math operations ###
######################################

# Your task is to check in action every basic math operators with combination of integers, floating point numbers, complex numbers and booleans. Do at least two calculations for every operator. 
# Also make use of [round()](https://www.w3schools.com/python/ref_func_round.asp) function to round your floating point results to specific number of decimals.  
# You can mix integer with floats inside given math operation.  
# > Hint: You can assign math operation to a variable, and then perform another math operation on this variable, for example:  

# a = 2/3
# print(round(a, 2))  # result is 0.67

# Check what happens after division by zero :smiley:

# - Some of your results could look like this:


# 12 + 34 = 46
# 43 - 56 = -13
# 4 * 4 = 16
# 4 / 5 = 0.8
# 12 % 5 = 2
# 2 ** 4 = 16
# 12.2 // 3 = 4.0
# True * False = 0
# 5 * (2 - 3j) = (10-15j)


### Execution: 

print(" ###################################### \n ### Task 1 - basic math operations ### \n ######################################") 

a = 12 + 34  
print(a)  # version 1
print(12 + 34) # version 2
b = 43 - 56
print(b) # # version 1
print(43 - 56) # version 2

print(4 * 4)

print(round(4/5, 2))

print(round(12 % 5, 2))

print((2 ** 4))

print((12.2 // 3))
print(True * False)
print(5 * (2 - 3j))




#####################################
### Task 2 - basic math functions ###
#####################################

# Your task is to check in action every basic math function mentioned earlier with combination of integers, floating point numbers, complex numbers and booleans. Do at least two calculations for every function. 

# - Some of your results could look like this:

# max(2, 2.0, -0.5) = 2
# min(23, 22, 55.0) = 22
# abs(-34.23) = 34.23
# pow(3, 4) = 81
# ceil(34/5) = 7
# floor(34/5) = 6
# max(True, False) = True
# abs(4 - 3j) = 5.0


### Execution:

print(" #################################### \n ### Task 2 - basic math function ### \n ####################################") 

x = max(2, 2.0, -0.5)
print("Max. value is =", x)

y = min(23, 22, 55.0)
print("Min. value is =", y)

print("Absolute value of -34.23 is =", abs(-34.23))
print("Value of 3 to the Power of 4 is =", pow(3, 4))

import math # this will import "math module" with additional functions
x = 34/5

math.ceil(x)
print("The Ceiling value of 34/5 is =", math.ceil(x))

math.floor(x)
print("The Floor Division of 34/5 =", math.floor(x))

print("The Max. value between True and False is =", max(True, False))

print("The Absolute value of (4 - 3j) =", abs((4 - 3j)))


# The End