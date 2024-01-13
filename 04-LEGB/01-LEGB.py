"""
    LEGB --> Local, Enclosed, Global and Built-in
"""
a = 'haider'  # global
def demo1():
    x = 1000  # local


# for enclosed or nonlocal
x = 10
def outer():

    # it will give error
    # x += 100
    # to avoid it, we use 'global'
    # global x
    # x += 100

    x = 100
    def inner():
        # it will give error
        # x += 1000
        # to avoid it, we use 'nonlocal'
        nonlocal x
        x += 1000
        print('from inner() - x = ',x ,'\n')

    print('from outer() - x = ',x , '\n')
    inner()

outer()
