###########################################################
################ WORKING WITH STRINGS #####################
###########################################################

# Task 1

city = "Napoli"
print(city)

# Taks 2

population = 950000

print(city + ":", population)

# Task 3 

city = "Napoli"

print("City: " + city, str(city.isalpha()))

print("Population:", population)


# Task 4

text1 = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."

print("capital:", text1.find("capital"))


# Task 5

text2 = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."

print(text2.split())


# Task 6

text3 = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."

print(text3.replace("capital","capital of Germany"))