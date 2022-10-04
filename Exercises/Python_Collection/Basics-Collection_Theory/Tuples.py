##### TUPLES #####


# Tuples cannot be mutated, 
# however there are some situation, e.g. 

x = ( [], )

# adding to a data structure that can change
x[0].append("works")

# Converting from a tuple to a list
# pass the tuple to the list constructor
x = list(x)

# deduplication with a word:
word = "this worrd has many words with duplicates"
counts = {}

for char in word.lower():
    counts.setdefault(char, 0)
    counts[char] = counts[char] + 1


# same thing using a 'set':
# (Refer to the "word" variable above!)
counts = {}
for char in set(word.lower()):
    counts.setdefault(char, 0)
    counts[char] = counts[char] + 1










# In [13]: locations = { "Berlin" }

# In [15]: locations.update("Napoli", "Hamburg", "Sydney", "New York")

# In [16]: print(locations)
# {'m', 'S', 'i', 'k', 'a', 'r', 'g', 'p', 'w', 'e', 'Y', 'b', 'H', ' ', 'o', 'y', 'N', 'Berlin', 'u', 'l', 'd', 'n'}

'''
In [17]: locations.add("Napoli", "Hamburg", "Sydney", "New York")
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-17-3a627dfa9647> in <module>
----> 1 locations.add("Napoli", "Hamburg", "Sydney", "New York")

TypeError: set.add() takes exactly one argument (4 given)
'''

# In [18]: locations.add("Napoli",)

# In [19]: locations.add("Hamburg",)

# In [20]: locations.add("Sydney",)

# In [21]: locations.add("New York",)

# In [22]: print(locations)
# {'m', 'S', 'Napoli', 'Sydney', 'i', 'k', 'a', 'r', 'g', 'p', 'w', 'e', 'Y', 'b', 'H', ' ', 'o', 'Hamburg', 'y', 'N', 'New York', 'Berlin', 'u', 'l', 'd', 'n'}

