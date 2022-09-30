##################################################################
###### Theory on Basics - Collection (September 30th, 2022) ######
##################################################################


# Study from Module 2 - Python Programming // Python Collection Slides

# Exercise:

lists = [ ["John",[ {"name": "Mary"} ], "Amy"], [ 32, 43,{'age': 100}, 51] ]

'''
Print the value of Mary
Print the age of 100.
'''

# Output:

print(lists[0][1][0]["name"])
print(lists[1][2]["age"])


# RANGE:

sequence = range(1, 5, 2)

print(sequence)

print(list(sequence))

s = range(1,5)

list(s)

# Lists: Accessing Values

#### SORTING ####

# Reverse:

words = ['cat', 'aadvark', 'elephant', 'squirrel', 'hippo']

words.reverse()             # proper way to use this method: using it by itself - without re/assigning it to any variable (otherwise returns 'None')

print(words)


# Sort:
words = ['cat', 'aadvark', 'elephant', 'squirrel', 'hippo']

#words = words.sort()       # doing this, will just return 'None' in CLI
words.sort()                # this is the proper way how to use this method (likewise to the method 'reverse()')

print(words)


# NOTE: Playing around:

words.sort(reverse=True)    # this will sort AND reverse at the same time

print(words)

# Remove Replace:

words = ['cat', 'aadvark', 'elephant', 'squirrel', 'hippo']

words[1:3] = ["lion"]       # this, will 'slice' the list and replace these items from [1:3] with the single item 'lion'
#words[3] = "lion"          # this, will only replace position 3 in the list with 'lion' - not useful for this scope

print(words)