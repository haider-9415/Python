class decor:
    def __init__(self, function):
        self.func = function

    # __call_ is a magic method
    def __call__(self, a, b):
        result = self.func(a, b)
        return result**2

# @decor
def add(a, b):
    return a+b

obj = decor(add)
print('obj(2, 3) --> ',obj(2, 3), '\n') # obj.__call__(a, b)


# or simply place '@decorator_name' before the add function instead of creating the object
# and
# print('add(2, 3) --> ',add(2, 3), '\n')


