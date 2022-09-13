# REGULAR EXPRESSION

# Difference between 're.search' and 're.match'

#Python offers two different primitive operations based on regular expressions: 
#       - 'match' checks for a match only at the beginning of the string, while;
#       - 'search' checks for a match anywhere in the string 


import re           # import Regular Expression module (library)
 
Substring ='string'
 
 
String1 ='''We are learning regex with geeksforgeeks
         regex is very useful for string matching.
          It is fast too.'''
String2 ='''string We are learning regex with geeksforgeeks
         regex is very useful for string matching.
          It is fast too.'''
 
# Use of re.search() Method
print(re.search(Substring, String1, re.IGNORECASE))
# Use of re.match() Method
print(re.match(Substring, String1, re.IGNORECASE))
 
# Use of re.search() Method
print(re.search(Substring, String2, re.IGNORECASE))
# Use of re.match() Method
print(re.match(Substring, String2, re.IGNORECASE))