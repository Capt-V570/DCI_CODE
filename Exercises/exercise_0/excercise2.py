# -----------------------------------------------------------------------------------------------
# ---------------------------------------EXERCISE 2----------------------------------------------
# -----------------------------------------------------------------------------------------------

# TASK 1 - Create a variable called text to store the data: 
# Berlin is a world city of culture, politics, media and science. 
# Your task is to print the length of the text variable on the screen.

text = "Berlin is a world city of culture, politics, media and science."
print(len(text))

# TASK 2 - Reuse the variable called text and print the first and the last characters on the screen.

print(text[0],text[-1])

# TASK 3 - Reuse the variable called text and print the first three characters in upper case.

firstThree = "First three characters: " + text[:3].upper()
print(firstThree)

# TASK 4 - Create the variable called text with the following content: 
# Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital , 
# then count how many times the letter B appears in the text. 

text_2 = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital "
print("B appears: " + str(text_2.count("B")) + " times")

# TASK 5 - Create a variable called text to store the data: 
# "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."  
# Your task is to print the last 10 characters of the text variable on screen.

text_3 = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."  
print ("Last ten characters: " + (text_3[118:128]))

# TASK 6 - Create a variable called text to store the data: ---Python programming--- . 
# Your task is to remove the hyphen (-) character from the string.

text_4 = "---Python programming---"
# print(text_4[3:21])     (NOT SO COOL ALTERNATIVE)
print(text_4.strip("-"))

# TASK 7 - Create two variables to store your first and your last name. Your task is to concatenate the two variables using the appropriate labels.

    # You should provide a single line print statement.

name = "Fausto"
surname = "Ferrara"
print("Firstname: " + str(name) + "\n Lastname: " + str(surname))