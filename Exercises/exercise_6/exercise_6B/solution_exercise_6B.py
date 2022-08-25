################################################################
####################### SUBSTRING IN PYTHON ####################
################################################################

given_string = """One morning, when Gregor Samsa woke from troubled dreams, 
he found himself transformed in his bed into a horrible vermin.
 He lay on his armour-like back, and if he lifted his head a 
little he could see his brown belly, slightly domed and divided by 
arches into stiff sections. The bedding was hardly able to cover 
it and seemed ready to slide off any moment. His many legs, pitifully 
thin compared with the size of the rest of him, waved about helplessly 
as he looked."""



def find_text(given_string, value_to_search):
    s = given_string.index(value_to_search)
    e = given_string.index(value_to_search)+len(value_to_search)
    return given_string[s:e]

var1 = find_text(given_string, "He")
var2 = find_text(given_string, "l")
var3 = find_text(given_string, "lo")
var4 = find_text(given_string, "Gregor")

"""   # VERSION 2
var1 = given_string.index("He")
var2 = given_string.index("l")
var3 = given_string.index("lo")
var4 = given_string.index("Gregor")
"""

print(var1 + var2 + var3, var4)

"""  # VERSION 2
# print(given_string[124:126] + given_string[46:47] + given_string[468:470], given_string[var4:24])
"""
