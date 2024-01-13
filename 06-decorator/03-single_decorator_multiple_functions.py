"""
    we will create a program, in which we will show an string instead of
    error when the Denominator is zero and we will do it with the help of 
    decorator
"""

def deco(func):
    def inner(*args): # args contains a tupel
        # to check the denominator
        for num in args[1:]:
            if num == 0:
                return "Cannot divide by zero - Denominator must be non-zero"
        return func(*args)
    return inner

@deco
def div1(x, y):
    return x/y

@deco
def div2(x, y, z):
    return x/y/z

print('div1(10, 5) --> ',div1(10, 5), '\n')
print('div1(10, 0) --> ',div1(10, 0), '\n')
print('div1(0, 5) --> ',div1(0, 5), '\n')

print('div2(625, 25, 5) --> ',div2(625, 25, 5), '\n')
print('div2(625, 0, 5) --> ',div2(625, 25, 0), '\n')
print('div2(625, 25, 0) --> ',div2(625, 25, 0), '\n')
print('div2(0, 25, 5) --> ',div2(0, 25, 5), '\n')

