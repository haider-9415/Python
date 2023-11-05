# positional arguments
def power(p, q):
    print(p,'^',q,' = ',p**q, '\n')

power(2, 3) # p=2 and q=3
# after changing the positions
power(3, 2) # p=3 and q=2

# both of the following will give error because no. of arguments != no. of parameters
# power(3, 2, 4)
# power(3)
print('......................................................................\n')




# keyword arguments
def info(name, age):
    print(f'name: {name} - age:{age}')

info(name='haider', age=21) # name='haider and age=21
# after changing the positions
info( age=21, name='haider') # name='haider and age=21

# both of the following will give error because no. of arguments != no. of parameters
# info( age=21, name='haider', phone=1234567890)
# info( age=21)
print('......................................................................\n')




# default arguments
def print_stat(s='Hello, it is haider'):
    print('statement --> ',s)

# without passing arguments
print_stat()
# with passing arguments
print_stat('Hello, it is harry')


def func2(a = "welcome"):
    return a
print("func2() --> ",func2(),'\n')

def func3(a = "welcome", b = 20000, c = (1,2,3,4)):
    return a,b,c
print("func3() --> ",func3(),'\n')
# but we can change the default values
print("func2('hello') --> ",func2("hello"),'\n')
print("func3(1234,'haider',{1:'a',2:'b',3:'c'}) --> ",func3(1234,'haider',{1:'a',2:'b',3:'c'}),'\n')

""" if there are multiple parameters and you want to make one as 
    default then you have to place it in last otherwise it will give error
"""

print('......................................................................\n')




# variable length arguments
# syntax --> *para_name
def SUM1(*num):
    # the parameter 'num' obtains the tuple of the given arguments, so, we use loop
    sum = 0
    for i in num:
        sum += i
    print(f'num: {num}  -  sum: {sum}')

SUM1(10) # it sends (10)
SUM1(10,20) # it sends (10,20)
SUM1(10.30,20,30) # it sends (10.30,20,30)
SUM1(10.30,20.67,23.56,23,2,89.97) # it sends (10.30,20.67,23.56,23,2,89.97)
print

def func5(*args, email_id = 'xxxxxxx@gmail.com'):
    return args,email_id

print("func5() --> ",func5(),'\n')
print("func5(abcd) --> ",func5('abcd'),'\n')
print("func5('a','b','c','d','e','f','g','h') --> ",func5('a',
'b','c','d','e','f','g','h'),'\n')
print("func5(1,2,3,4,5, email_id='yyyyyyyy@gmail.com') --> ",
func5(1,2,3,4,5, email_id='yyyyyyyy@gmail.com'),'\n')

print('......................................................................\n')



# variable length keyword arguments
# syntax --> **para_name
def SUM2(**num):
    # the parameter 'num' obtains the dictonary of the given arguments, so, we use loop
    sum = 0
    for i in num:
        sum += num[i]
    print(f'num: {num}  -  sum: {sum} \n')
    # 'num' is dictionary so we can use its methods that we will see later
    print('num.keys() --> ',num.keys())
    print('num.values() --> ',num.values())

# we havee to pass arguments wwith their unique keys
SUM2(n1=10) # it sends {'n1': 10}
SUM2(n1=10,n2=20) # it sends {'n1': 10, 'n2': 20}
SUM2(n1=10.30,n2=20,n3=30) # it sends {'n1': 10.3, 'n2': 20, 'n3': 30}
SUM2(n1=10.30,n2=20.67,n3=23.56,n4=23,n5=2,n6=89.97) # it sends {'n1': 10.3, 'n2': 20.67, 'n3': 23.56, 'n4': 23, 'n5': 2, 'n6': 89.97}
print('......................................................................\n')


