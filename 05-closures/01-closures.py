def outer():
    def inner():
        x = 'haider'
        return x
    return inner

new = outer()
print('new() --> ',new())

"""
    after the execution of a function, the function is deleted from the memory
    so the outer() and its content has been deleted after its execution, e.i.,
    after line 7 but we an access 'x' that is in inner() but there is no inner()
    in the memory, it is because 'new' stores the code of inner() which has the 
    value of 'x', therefore we can it and this property of python is called 
    "closure"
"""


