##################################################################
###### Theory on Basics - Collection (September 30th, 2022) ######
##################################################################


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



