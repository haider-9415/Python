# local variable
""" you will see the value of 'a' will not be changed after 
    calling the function it means 'a' outside of the function 
    is different from 'a' inside of the function
"""
a = 'haider'
def add(x, y):
    a = x+y
    print('a --> ',a)

add(100, 200)
print('a --> ',a)
# remember parameters of a function are also local variables of the function
print('.................................\n')


# global variable
""" you will see we can access 'b' with its value inside 
    the function
"""
b = 10
def mult(y):
    x = 5
    print(x,'x',y,'=', x*y)
    print(y,'x',b,'=', y*b)
    print('b --> ',b)
mult(100)
print('.................................\n')


# global keyword
c = 100
def add2(x, y):
    a = x+y
    print('a --> ',a)
    # on updating the global variable in the function it will give error
    # the error --> UnboundLocalError: local variable 'c' referenced before assignment
    # c = c+a
    # print('c --> ',c)
    
    # to avoid it we use 'global' keyword
    global c
    c = c+a
    print('inside the function - c --> ',c)

print('before calling the function - c --> ',c) 
add2(100, 200)
# now has been updated globaly 
print('after calling the function - c --> ',c) 
print('.................................\n')
