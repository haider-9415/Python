# decorator function
def deco1(func):
    def inner():
        # existng functionality
        func()
        # adding new functionality
        print('hello from decorator \n')
    return inner


# method 1 to use decorator
def printer1():
    print('hello from printer1() \n')

printer1 = deco1( printer1 )
printer1()
print('.................................................\n')


# method 2 to use decorator
@deco1
def printer2():
    print('hello from printer2() \n')

printer2()
print('.................................................\n')

"""
    you can see we have added other functionality in the printer()
    from outside of it and it can be done with the help of decorator
"""

# another example
def deco2(func):
    def inner():
        # existng functionality
        result = func()
        # adding new functionality
        num3 = float(input('Enter third number: '))
        final = result + num3
        return final
    return inner

@deco2
def add():
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    result = num1 + num2
    return result

final = add()
print('result = ',final)
print('.................................................\n')
    