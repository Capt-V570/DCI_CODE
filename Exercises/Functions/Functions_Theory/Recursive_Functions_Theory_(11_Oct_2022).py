##############################################################
############# FUNCTIONS THEORY (11 OCTOBER 2022) #############
##############################################################




'''
def factorial(n):
    # base case
    if n == 0:
        return 1
    else:
        # expensive (your computer might crash)
        return n * factorial(n - 1)

print(factorial(3))
for i in range(1000):
    print(factorial(i), f"i->{i}")
'''



# 20 minutes, trying to rewrite this to use a recursive style:
'''
def get_sum(list):
    total = 0
    for i in list:
        total += i
    return total

# version 1:
def get_sum(list):
    #print(list)
    if not list:
        return 0
    else: 
        first = list.pop(0)
        return first + get_sum(list)
'''
# version 2:
def get_sum(list):
    print(list)
    if len(list) == 1:
        return list[0]
    else: 
        first = list.pop(0)
        return first + get_sum(list)
'''
# version 3 - ask pasco: Negative Slicing:
def get_sum(list):
'''

numbers = [1,2,3]

print(get_sum(numbers))