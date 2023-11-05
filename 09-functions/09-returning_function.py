def outer():
    def inner():
        print('it is inner function')
    # to execute the inner() we have to call it inside outer()
    # inner()

    # to return inner()
    return inner

# we can not call inner() from heere because it is inside of outer()
# inner()
outer()


# to call inner() outside of outer(), we returns 'inner' with 'return'
func1 = outer()
func1()
print('..................................................')


# function as argument with returning function
def func1():
    return "hello, i am haider"

def func2(f):
    print('f() --> ', f())
    return f

func3 = func2(func1)
print('func3() --> ',func3())

print('..................................................')
