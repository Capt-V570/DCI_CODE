# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn

#########################################
#### Task 1 - printing single object ####
#########################################
# Your task is to print values of primitive data types, one type in one line. 
# Use following types: integer, float, complex, string, boolean

# - Your result could look like this:

# 234
# 43.12
# (3+2j)
# Hello
# True


print(234)
print(43.12)
print((3+2j))
print("Hello")
print(True)


#############################################
### Task 2 - printing type of given value ###
#############################################

# Your task is to print two objects with separator for the same primitive types as in task 1.   
# The first object is a value of given type, the second object is a type of value.  
# The separator is a string " is type of ".

# - Your result could look like this:

# 123 is type of <class 'int'>
# 43.23 is type of <class 'float'>
# (4-1j) is type of <class 'complex'>
# How are you? is type of<class 'str'>
# True is type of <class 'bool'>


# version 1

print(123, type(123), sep=" is type of ")
print(43.23, type(43.23), sep=" is type of ")
print((4-1j), type((4-1j)), sep=" is type of ")
print("How are you?", type("How are you?"), sep=" is type of ")
print(True, type(True), sep=" is type of ")

# version 2

var = " is type of "
print(123, type(123), sep=var)
print(43.23, type(43.23), sep=var)
print((4-1j), type((4-1j)), sep=var)
print("How are you?", type("How are you?"), sep=var)
print(True, type(True), sep=var)

#######################################
### Task 3 - checking type of value ###
#######################################

# Your task is to check if given value is the instance of given class type using ```isinstance()``` function.  
# The first argument of this function should be value, for example `city` and the second argument should be class type, for example `int`.   
# Print at least one result for every primitive data type ('int', 'float', 'bool', 'complex', and 'str'). 


# - Your result should look like this:

# True
# False
# True
# True
# False

print(isinstance(123, int))
print(isinstance(43.23, int))
print(isinstance(43.23, float))
print(isinstance(True, bool))
print(isinstance((4-1j), complex))
print(isinstance("Hello World", complex))
print(isinstance("Hello World", str))

####################################################
### Task 4 - checking type of values (version 2) ###
####################################################


# Your task is a slightly modification of task 3. Instead  printing `True` or `False` modify your code to get readable information about the type of your value. 

# - Your result should look like this:

# Is 123  an instance of int?:  True
# Is 43.23  an instance of bool?: False
# Is (4-1j)  an instance of complex?: True
# Is True  an instance of bool?: True
# Is 'How are you?'  an instance of float?: False

a = 123
b = 43.23
c = (4-1j)
d = True
e = "'How are you?'"

print("Is " + str(a) + " an instance of int?: " + str(isinstance(a, int)))
print("Is " + str(b) + " an instance of bool?: " + str(isinstance(b, bool)))
print("Is " + str(c) + " an instance of complex?: " + str(isinstance(c, complex)))
print("Is " + str(d) + " an instance of bool?: " + str(isinstance(d, bool)))
print("Is " + str(e) + " an instance of float?: " + str(isinstance(a, float)))

#######################################
### Task 5 - using comments in code ###
#######################################

# Use code from one of the earlier exercises and add [comments](https://www.python.org/dev/peps/pep-0008/#comments) to it.  
# Read most popular [answer](https://stackoverflow.com/questions/7696924/is-there-a-way-to-create-multiline-comments-in-python) about multiline comments in Python.
# Use  block comments, inline comments, and multiline comments to your code. 
# > Comments that contradict the code are worse than no comments. Always make a priority of keeping the comments up-to-date when the code changes!

# - Your result could look like this:


# This is my first comment
# Block comments are indented to the same level as that code

print("Hello")  # this is an example of a comment
print("Line with inline code!")  # remember about spacing!

print(type(123.45))  # getting type of number

# I definitely should read all these links and study hard! :)