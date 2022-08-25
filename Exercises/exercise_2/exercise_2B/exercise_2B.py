##################################################
################ WORKING WITH STRINGS ############
##################################################


# Task 1

text1 = "Berlin is a world city of culture, politics, media and science."

print(len(text1))

# Task 2

text2 = "Berlin is a world city of culture, politics, media and science."

print(text2[0], text2[62])


# Task 3

text3 = "Berlin is a world city of culture, politics, media and science."
first_characters = text3[0:3]

print(first_characters.upper())

# Task 4

text4 = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital"

print("B appears: ", text4.count("b"), "times")


# Task 5 

text5 = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."

print(len(text5))
print("The last 10 characters are:", text5[118:])

# Task 6

text6 = "---Python programming---"

print(text6.strip("---"))


# Task 7

name = "Fausto"
surname = "Ferrara"

print("First name:", name, "\nLast name:", surname)
