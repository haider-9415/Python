# we have to import it from 'functools'
from functools import partial

# syntax --> partial(func, arg1,arg2,arg3,arg4,....,argn)
def add(n1,n2,n3,n4,n5):
    return n1+n2+n3+n4+n5

add1 = partial(add, 10, 20) 
# now n1=10 and n2=20 have been fixed if you pass 5 arguments then it will give error

print('result1 = ',add1(30,40,50))

# the following will give error
# print('result1 = ',add1(1,2,30,40,50))

print('............................................\n')

# we can pass keyword arguments
add2 = partial(add, n3=100, n5=200) # now n3=100 and n5=200
# but we have to use keyword arguments in this also
print('result2 = ',add2(n2=300,n1=400,n4=500))

print('............................................\n')


