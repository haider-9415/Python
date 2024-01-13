"""
    type-1 -  Built-in-namespace
    python creates it when interpreter is started
"""

print('dir() --> ',dir())
print('................................................................\n')



"""
    type-2 -  global-namespace or module-namespace
    it is creatd for a perticular namespace

    suppose there are two module 'example_1' and 'example_2' and they 
    have a function of same name then to call the function from anyone module
    'global namespace' functionality acts
"""
import example_1, example_2

print('example_1.display --> ',example_1.display)
print('example_2.display --> ',example_2.display)
print()

print('example_1.display() --> ',example_1.display())
print('example_2.display() --> ',example_2.display())
print('................................................................\n')



# local namespace
"""
    it is created for a peertcular class or function
"""
def func1():
    a = 1000
    def func3(num):
        num = 100
        print('in func3 - dir() --> ',dir(),'\n')

    print('in func1 - dir() --> ',dir(),'\n')
    func3(1)

def func2():
    a = 1000
    lt = [1,2,3,4,5]
    print('in func2 - dir() --> ',dir(),'\n')

func1()
func2()

print('................................................................\n')

