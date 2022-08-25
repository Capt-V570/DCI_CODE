# Test 

name = "Fausto"
print(name[0:3]) 
print(name.find("st"))

# Task 1

from stat import FILE_ATTRIBUTE_REPARSE_POINT


city = "London"
print(city)

# Task 2

city2 = "berlin"
population = 3645000
print(city2.capitalize() + ": " + str(population))

# Task 3

city3 = "london"
population_2 = 9000000
print("City: " + city3.capitalize() + " " + str(city3.isalpha()))
print("Population: " + str(population_2))

# Task 4

text = "Berlin is surrounded by the state of Brandenburg and contiguous with Potsdam, Brandenburg's capital"
print(text.find("capital"))

# Task 5

text2 = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."
print(text2.split())

# Task 6

text3 = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."
print(text3.replace("capital", "capital of Germany"))