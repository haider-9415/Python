"""
    we will write a program which will take first and last name as input and, with the help
    a decorator, we will convert the whole name in upper-case and, with the hep of another 
    decorator, we will make thse first and last name as the elements of al ist
"""

# to convert whole name in upper-case
def deco1(func):
    def inner():
        name = func()
        return name.upper()
    return inner

# to split in a list containing first and last name as its elements
def deco2(func):
    def inner():
        name = func()
        return name.split()
    return inner

@deco2
@deco1
def get_name():
    first = input('Enter first name: ')
    last = input('Enter last name: ')
    return first+" "+last

# or

# get_name = deco1(get_name)
# get_name = deco2(get_name)

# or

# get_name = deco2(deco1(get_name))

name = get_name()
print('\nname --> ', name)

print('...............................................\n')