l = [1,2,3,4,5]
s = 'haider'

def func1():
    a = 'abcd'
    lt = [10,20,30]

    print('for func1:')
    # it return a dictionary containing the local data of func1
    print('locals() --> ',locals())
    print('locals()["a"] --> ',locals()["a"])
    print('locals()["lt"] --> ',locals()["lt"])

func1()
print('..................................................\n')


def func2(num):    
    # similarly
    print('for func2:')
    print('locals() --> ',locals())
    return(num)

func2(100)
print('..................................................\n')


print('for the file:')
print('locals() --> ',locals())
print('locals()["l"] --> ',locals()["l"])
print('locals()["s"] --> ',locals()["s"])
print('locals()["func2"] --> ',locals()["func2"])
print('..................................................\n')
