# PEP 8 - BAD vs GOOD Code - Python3

##################################################
################# EXAMPLE 1 ######################
##################################################

# Should a line break before or after a binary operator?

# For decades the recommended style was to break after binary operators. But this can hurt readability in two ways: 
# the operators tend to get scattered across different columns on the screen, and each operator is moved away from its operand and onto the previous line. 
# Here, the eye has to do extra work to tell which items are added and which are subtracted:

''' BAD: operators sit far away from their operands '''
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)

''' GOOD: easy to match operators with operands '''
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)

##################################################
################# EXAMPLE 2 ######################
##################################################

#Imports should usually be on separate lines, e.g.:

''' BAD example: '''
import os, sys

''' GOOD example '''
import os
import sys


##################################################
################# EXAMPLE 3 ######################
##################################################

# Function annotations should use the normal rules for colons and always have spaces around the -> arrow if present. 
# (See Function Annotations below for more about function annotations.)

''' BAD example: '''

def munge(input:AnyStr): ...
def munge()->PosInt: ...


''' GOOD example: '''

def munge(input: AnyStr): ...
def munge() -> AnyStr: ...



##################################################
############# OTHER RECOMMENDATIONS ##############
##################################################

# Avoid trailing whitespace anywhere. Because it’s usually invisible, it can be confusing: 
# e.g. a backslash followed by a space and a newline does not count as a line continuation marker. 
# Some editors don’t preserve it and many projects (like CPython itself) have pre-commit hooks that reject it.

# Always surround these binary operators with a single space on either side: 
# assignment (=), augmented assignment (+=, -= etc.), comparisons (==, <, >, !=, <>, <=, >=, in, not in, is, is not), Booleans (and, or, not).

# If operators with different priorities are used, consider adding whitespace around the operators with the lowest priority(ies). 
# Use your own judgment; however, never use more than one space, and always have the same amount of whitespace on both sides of a binary operator.

'''Yes:'''

i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)

'''No:'''

i=i+1
submitted +=1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)

# Don’t use spaces around the = sign when used to indicate a keyword argument or a default parameter value.

''' YES: '''

def complex(real, imag=0.0):
    return magic(r=real, i=imag)

''' No: '''

def complex(real, imag = 0.0):
    return magic(r = real, i = imag)

# Function annotations should use the normal rules for colons and always have spaces around the -> arrow if present. (See Function Annotations below for more about function annotations.)

''' YES: '''

    def munge(input: AnyStr): 
    def munge() -> AnyStr: 

'''No:'''

    def munge(input:AnyStr):
    def munge()->PosInt:

# When combining an argument annotation with a default value, use spaces around the = sign (but only for those arguments that have both an annotation and a default).

'''Yes:'''

    def munge(sep: AnyStr = None): ...
    def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...

'''No:'''

    def munge(input: AnyStr=None): ...
    def munge(input: AnyStr, limit = 1000): ...

# Compound statements (multiple statements on the same line) are generally discouraged.

'''Yes:'''

    if foo == 'blah':
        do_blah_thing()
    do_one()
    do_two()
    do_three()

'''Rather NOT:'''

    if foo == 'blah': do_blah_thing()
    do_one(); do_two(); do_three()

# While sometimes it’s okay to put an if/for/while with a small body on the same line, never do this for multi-clause statements. Also avoid folding such long lines!

'''Rather NOT:'''

    if foo == 'blah': do_blah_thing()
    for x in lst: total += x
    while t < 10: t = delay()

'''Definitely NOT:'''

    if foo == 'blah': do_blah_thing()
    else: do_non_blah_thing()

    try: something()
    finally: cleanup()

    do_one(); do_two(); do_three(long, argument,
                                 list, like, this)

    if foo == 'blah': one(); two(); three()