# to call it, we have to give it ame as we asssign values in variables
# remember we don't need to use 'return' statement
add = lambda a,b,c: a+b+c
# it returns function class 
print('type(add) --> ',type(add))
# and memory address
print('add --> ',add)

print('add(10, 20, 30) --> ',add(10, 20, 30), '\n')
print('......................................................................\n')



lf = lambda a,b: (a+b, a-b)
add, sub = lf(100, 50)
print('add --> ',add)
print('sub --> ',sub)
print('......................................................................\n')



# default argument
lf = lambda a,b=100: (a+b, a-b)
add, sub = lf(100)
print('add --> ',add)
print('sub --> ',sub)
print('......................................................................\n')



# keyword argument
lf = lambda a,b: (a+b, a-b)
add1, sub1 = lf(a=100, b=50)
print('add1 --> ',add1)
print('sub1 --> ',sub1)
print()
add2, sub2 = lf(b=50, a=100)
print('add2 --> ',add2)
print('sub2 --> ',sub2)
print('......................................................................\n')


# variable length arguments
l1 = lambda *args: args
print("l1(1,2,3,4,5,6) --> ",l1(1,2,3,4,5,6),'\n')
# when we use lambda function then the class will be 'function'
print("type(l1) --> ",type(l1),'\n')
print('......................................................................\n')



# variable length keyword arguments
l2 = lambda **kwargs: kwargs
print("l2(name='haider', class_sec='12th-b',board='UP' --> ",l2(name='haider', class_sec='12th-b',board='UP'),'\n')
print("type(l2) --> ",type(l2),'\n')
print('......................................................................\n')



# nested lambda function
ADD1 = lambda x: lambda y: x+y
print('ADD1(10) --> ',ADD1(10)) # x=10
print('type(ADD1(10)) --> ',type(ADD1(10)), '\n')

func1 = ADD1(10) # x=10
print('func1(40) --> ',func1(40), '\n') # y=40


square = lambda n: n**2
modify = lambda func: lambda num: func(num)+num
var = modify(square)
input = var(int(input('Enter a number: ')))
print('input: ',input)
print('......................................................................\n')
