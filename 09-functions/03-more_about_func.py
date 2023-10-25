# we can call a function like this
def to_print(a,b):
    print("a --> ",a," & ","b --> ",b,'\n')

to_print(a = 'haider', b = 100)
to_print(b = 'haider', a = 100)
to_print('haider', b = 100) # it will work
# to_print(a = 'haider', 100) # but it will give error
print("..........................................................................................................................\n")

# def to_get1(x):
#     print(x)
# y = to_get1('hanzala') + " naeem"
# print("y --> ",y)
# the above code will give run time error, because, print() returns None type as we know  and string does not do concatination with any other data type
# to avoid this we use return keyword
def to_get2(x):
    return x
y = to_get2('hanzala') + " naeem"
print("y --> ",y,'\n')
print("..........................................................................................................................\n")


# when we use return for multiple parameters then it will return in a tuple
def func1(a,b,c,d):
    return a,b,c,d
a = func1("haider",[1,2,3,'a','b',89+9j],{'a','b','c','d'},2023)
print("a --> ",a)
print("type(a) --> ",type(a),'\n')
# we can assign them in multiple variables like this
e,f,g,h = func1("haider",[1,2,3,'a','b',89+9j],{'a','b','c','d'},2023)
print("e --> ",e);print("f --> ",f);print("g --> ",g);print("h --> ",h,'\n')
print("type(e) --> ",type(e));print("type(f) --> ",type(f));print("type(g) --> ",type(g));print("type(h) --> ",type(h),'\n')
print("..........................................................................................................................\n")


# we can give default values
def func2(a = "welcome"):
    return a
print("func2() --> ",func2(),'\n')

def func3(a = "welcome", b = 20000, c = (1,2,3,4)):
    return a,b,c
print("func3() --> ",func3(),'\n')
# but we can change the default values
print("func2('hello') --> ",func2("hello"),'\n')
print("func3(1234,'haider',{1:'a',2:'b',3:'c'}) --> ",func3(1234,'haider',{1:'a',2:'b',3:'c'}),'\n')
print("..........................................................................................................................\n")


# if you want to make a function of unlimited parameters then we use *
def func4(*parameters):
    return parameters
print("func4() --> ",func4(),'\n')
print("func4(10) --> ",func4(10),'\n')
print("func4(10,293) --> ",func4(10,293),'\n')
print("func4('haider','hanzala',1812.921,60+40,100//20,'a'+'b'+'c') --> ",func4('haider','hanzala',1812.921,60+40,100//20,'a'+'b'+'c'),'\n')
print("func4('naeem',[1,2,3,4,5],{'a','b','c'},('haider')) --> ",func4('naeem',[1,2,3,4,5],{'a','b','c'},('haider')),'\n')

def func5(*args, email_id = 'xxxxxxx@gmail.com'):
    return args,email_id
print("func5() --> ",func5(),'\n')
print("func5(abcd) --> ",func5('abcd'),'\n')
print("func5('a','b','c','d','e','f','g','h') --> ",func5('a','b','c','d','e','f','g','h'),'\n')
print("func5(1,2,3,4,5, email_id='yyyyyyyy@gmail.com') --> ",func5(1,2,3,4,5, email_id='yyyyyyyy@gmail.com'),'\n')

def func6(*args, email_id):
    return args,email_id
print("func6(1,2,3,4,5, email_id='zzzzzzzzzz@gmail.com') --> ",func6(1,2,3,4,5, email_id='zzzzzzzzzz@gmail.com'),'\n')
# print("func6(1,2,3,4,5, 'aaaaaaaaaaaaa@gmail.com') --> ",func6(1,2,3,4,5, 'aaaaaaaaaaaaa@gmail.com'),'\n') # it will give run time error

l1 = lambda *args: args
print("l1(1,2,3,4,5,6) --> ",l1(1,2,3,4,5,6),'\n')
# when we use lambda function then the class will be 'function'
print("type(l1) --> ",type(l1),'\n')
print("..........................................................................................................................\n")


""" if we want the function return a dictionary then we use ** and give parameters in kye value pairs in this way 
    'key = value'. Remember in this also range of aparmeters is unlimited       """
def func7(**para):
    return para
d1 = func7(name='haider', class_sec='12th-b',board='UP')
print("d1 --> ",d1,'\n')
print("type(d1) --> ",type(d1),'\n')

l2 = lambda **kwargs: kwargs
print("l2(name='haider', class_sec='12th-b',board='UP' --> ",l2(name='haider', class_sec='12th-b',board='UP'),'\n')
print("type(l2) --> ",type(l2),'\n')
print("..........................................................................................................................\n")






