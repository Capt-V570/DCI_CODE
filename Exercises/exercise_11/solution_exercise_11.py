##########################################
#########  replace() in python  ##########
##########################################

print("""************************************
**** replace('word') in Python *****
************************************""")

sentence = """A dogmatic dog buys dogecoin to become rich and
buy hotdogs every day."""

# VERSION 1 - (SOLUTION WITH TWO LINES OF CODE)
new_sentence = sentence.replace(" dog ", " cat ")

print(f"{sentence}\nOutput: {new_sentence}")

"""
# VERSION 2 - (SOLUTION WITH JUST ONE LINE OF CODE) 
print(f"{sentence}\nOutput: {sentence.replace(' dog ', ' cat ')}")
"""