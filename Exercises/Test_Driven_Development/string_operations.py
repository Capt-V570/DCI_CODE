#TODO:
# - Write a function to make two names titleized e.g. title_name(name1, name1)
# - Write a function, when given a list of names, it creates one name (test it too) e.g. join_names([‘name1’, ‘name2’, ‘name3’])


def titleize_names(name1, name2):
    return name1.title(), name2.title()

def join_names(name):
    return "".join(name)