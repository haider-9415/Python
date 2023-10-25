# map(function,iterable(s)) --> it brings ith element of those iterables to the function as its parameters and compute on them
""" it returns map object we can convert it into list, set and tuple """
""" we can use loop to print a map object, because, it is also an iterable object """


# for string
""" we can use built-in-function """
# converting 'haider' in tuple class
print("map(tuple,'haider') --> ",map(tuple,'haider'))
print("type(map(tuple,'haider')) --> ",type(map(tuple,'haider')))
print("list(map(tuple,'haider')) --> ",list(map(tuple,'haider')),'\n')
# converting 'HANZALA' in set class
print("map(set,'HANZALA') --> ",map(set,'HANZALA'))
print("type(map(set,'HANZALA')) --> ",type(map(set,'HANZALA')))
print("tuple(map(set,'HANZALA')) --> ",tuple(map(set,'HANZALA')),'\n')

""" we use multiple strings """
# remember, if there are 'n' parameters in function then there must be 'n' iterables 

# add ith elements of lt1, lt2 and lt3
def add_ith_ele(x,y,z):
    return x+y+z
st1 = 'abc'; st2 = 'def'; st3 = 'ghi'
print("map(add_ith_ele,st1,st2,st3) --> ",map(add_ith_ele,st1,st2,st3))
print("type(map(add_ith_ele,st1,st2,st3)) --> ",type(map(add_ith_ele,st1,st2,st3)))
print("tuple(map(add_ith_ele,st1,st2,st3)) --> ",tuple(map(add_ith_ele,st1,st2,st3)))
print("set(map(add_ith_ele,st1,st2,st3)) --> ",set(map(add_ith_ele,st1,st2,st3)),'\n')

# # the following will give run time error, because, iterables have not been given equal to the parameters
# print("map(add_ith_ele,st1,st3) --> ",map(add_ith_ele,st1,st3))
# print("type(map(add_ith_ele,st1,st3)) --> ",type(map(add_ith_ele,st1,st3)))
# print("tuple(map(add_ith_ele,st1,st3)) --> ",tuple(map(add_ith_ele,st1,st3)))
# print("set(map(add_ith_ele,st1,st3)) --> ",set(map(add_ith_ele,st1,st3)),'\n')


""" if we give strings of different length then it will proceed till they have same length
    but it does not give run time error """
st4 = 'abcd'; st5 = 'efghijkl'
def addother(x,y):
    return x+y
print("map(addother,st5,st6) --> ",map(addother,st4,st5))
print("type(map(addother,st5,st6)) --> ",type(map(addother,st4,st5)))
print("list(map(addother,st5,st6)) --> ",list(map(addother,st4,st5)),'\n')

""" here, we can use lambda function(anonymous function) """
st8 = 'abcd'; st9 = '1234'
print("map(lambda x,y:x+y,st9,st8) --> ",map(lambda x,y:x+y,st9,st8))
print("list(map(lambda x,y:x+y,st9,st8)) --> ",list(map(lambda x,y:x+y,st9,st8)),'\n')




# for list
l1 = [1,2,3,4,5,6]

print("using loop: ")
list1 = []
for i in l1:
    a = i+i
    list1.append(a)
print("    list1 --> ",list1,'\n')

""" using map function, we can do this easly"""
""" we can create our function """
print("using map func: ")
def add_itself(x):
    return x+x
print("    list(map(add_itself,l6)) --> ",list(map(add_itself,l1)))
print("    map(add_itself,l6) --> ",map(add_itself,l1))
print("    type(map(add_itself,l6)) --> ",type(map(add_itself,l1)))
print("    id(map(add_itself,l6)) --> ",id(map(add_itself,l1)),'\n')

""" we can use built-in-function """
# converting [1,2,3,4,5,6] in float class
print("map(float,[1,2,3,4,5,6]) --> ",map(float,[1,2,3,4,5,6]))
print("type(map(float,[1,2,3,4,5,6])) --> ",type(map(float,[1,2,3,4,5,6])))
print("list(map(float,[1,2,3,4,5,6])) --> ",list(map(float,[1,2,3,4,5,6])),'\n')
# converting [1,2,3,4,5,6] in str class
print("map(str,[1,2,3,4,5,6]) --> ",map(str,[1,2,3,4,5,6]))
print("type(map(str,[1,2,3,4,5,6])) --> ",type(map(str,[1,2,3,4,5,6])))
print("tuple(map(str,[1,2,3,4,5,6])) --> ",tuple(map(str,[1,2,3,4,5,6])),'\n')

print("using loop: ")
var1 = map(abs,[19,202,-293,200,2,-293,-229])
print(var1,end=': ')
for i in var1:
    print(i,end=',')
print('\n')

""" we can use multiple lists """
# remember, if there are 'n' parameters in function then there must be 'n' iterables 

# add ith elements of lt1, lt2 and lt3
def add_ith_ele(x,y,z):
    return x+y+z
lt1 = ['a','b','c']; lt2 = ['d','e','f']; lt3 = ['g','h','i']
print("map(add_ith_ele,lt1,lt2,lt3) --> ",map(add_ith_ele,lt1,lt2,lt3))
print("type(map(add_ith_ele,lt1,lt2,lt3)) --> ",type(map(add_ith_ele,lt1,lt2,lt3)))
print("tuple(map(add_ith_ele,lt1,lt2,lt3)) --> ",tuple(map(add_ith_ele,lt1,lt2,lt3)))
print("set(map(add_ith_ele,lt1,lt2,lt3)) --> ",set(map(add_ith_ele,lt1,lt2,lt3)),'\n')

# # the following will give run time error, because, iterables have not been given equal to the parameters
# print("map(add_ith_ele,lt1,lt3) --> ",map(add_ith_ele,lt1,lt3))
# print("type(map(add_ith_ele,lt1,lt3)) --> ",type(map(add_ith_ele,lt1,lt3)))
# print("tuple(map(add_ith_ele,lt1,lt3)) --> ",tuple(map(add_ith_ele,lt1,lt3)))
# print("set(map(add_ith_ele,lt1,lt3)) --> ",set(map(add_ith_ele,lt1,lt3)),'\n')

# to get length of each element in lt4
lt4 = ['abc023','defjdueh','gef','^&*@']
def get_len(n):
    return len(n)
print("map(get_len,lt4) --> ",map(get_len,lt4))
print("type(map(get_len,lt4)) --> ",type(map(get_len,lt4)))
print("list(map(get_len,lt4)) --> ",list(map(get_len,lt4)),'\n')

print("map(len,lt4) --> ",map(len,lt4))
print("type(map(len,lt4)) --> ",type(map(len,lt4)))
print("list(map(len,lt4)) --> ",list(map(len,lt4)),'\n')

""" if we give lists of different length then it will proceed till they have same length
    but it does not give run time error """
lt5 = [1,2,3,4,5]; lt6 = [4,1,3,2,0,4,3]
def addother(x,y):
    return x+y
print("map(addother,lt5,lt6) --> ",map(addother,lt5,lt6))
print("type(map(addother,lt5,lt6)) --> ",type(map(addother,lt5,lt6)))
print("list(map(addother,lt5,lt6)) --> ",list(map(addother,lt5,lt6)),'\n')

""" here, we can use lambda functoin(anonymous function) """
lt7 = [10,20,30,40,50]; lt8 = ['a','b','c','d']; lt9 = ['10','20','30','40']
print("map(lambda n:n*n,lt7) --> ",map(lambda n:n*n,lt7))
print("list(map(lambda n:n*n,lt7)) --> ",list(map(lambda n:n*n,lt7)),'\n')
print("map(lambda n:n**n,lt7) --> ",map(lambda n:n**n,lt7))
print("list(map(lambda n:n**n,lt7)) --> ",list(map(lambda n:n**n,lt7)),'\n')
print("map(lambda n:n/2,lt7) --> ",map(lambda n:n/2,lt7))
print("list(map(lambda n:n/2,lt7)) --> ",list(map(lambda n:n/2,lt7)),'\n')
print("map(lambda x,y:x+y,lt9,lt8) --> ",map(lambda x,y:x+y,lt9,lt8))
print("list(map(lambda x,y:x+y,lt9,lt8)) --> ",list(map(lambda x,y:x+y,lt9,lt8)),'\n')

lt10 = [1,2,3,4,5]
def power(n):
    return n**2,n**3
print("map(power,lt10) --> ",map(power,lt10))
print("type(map(power,lt10)) --> ",type(map(power,lt10)))
print("list(map(power,lt10)) --> ",list(map(power,lt10)),'\n')




# for tuple
tp1 = (34.34,123.0,232.565,789.433)
tp2 = ('wad','ajh','aafre','yakf')
tp3 = ('A','B','C','D','E','F')

""" we can create our function """
def add_itself(x):
    return x+x
print("    list(map(add_itself,tp2)) --> ",list(map(add_itself,tp2)))
print("    map(add_itself,tp2) --> ",map(add_itself,tp2))
print("    type(map(add_itself,tp2)) --> ",type(map(add_itself,tp2)))
print("    id(map(add_itself,tp2)) --> ",id(map(add_itself,tp2)),'\n')

def power(n):
    return n**2,n**3
print("map(power,tp1) --> ",map(power,tp1))
print("type(map(power,tp1)) --> ",type(map(power,tp1)))
print("list(map(power,tp1)) --> ",list(map(power,tp1)),'\n')

""" we can use built-in-function """
# converting (1,2,3,4,5,6) in float class
print("map(float,(1,2,3,4,5,6)) --> ",map(float,(1,2,3,4,5,6)))
print("type(map(float,(1,2,3,4,5,6))) --> ",type(map(float,(1,2,3,4,5,6))))
print("list(map(float,(1,2,3,4,5,6))) --> ",list(map(float,(1,2,3,4,5,6))),'\n')
# converting (1,2,3,4,5,6) in str class
print("map(str,(1,2,3,4,5,6)) --> ",map(str,(1,2,3,4,5,6)))
print("type(map(str,(1,2,3,4,5,6))) --> ",type(map(str,(1,2,3,4,5,6))))
print("set(map(str([1,2,3,4,5,)])) --> ",set(map(str,(1,2,3,4,5,6))),'\n')

print("using loop: ")
var1 = map(abs,(19,202,-293,200,2,-293,-229))
print(var1,end=': ')
for i in var1:
    print(i,end=',')
print('\n')

""" we can use multiple tuple """
# remember, if there are 'n' parameters in function then there must be 'n' iterables 

# add ith elements of lt1, lt2 and lt3
def add_ith_ele(x,y,z):
    return x+y+z
t1 = ('a','b','c'); t2 = ('d','e','f'); t3 = ('g','h','i')
print("map(add_ith_ele,t1,t2,t3) --> ",map(add_ith_ele,t1,t2,t3))
print("type(map(add_ith_ele,t1,t2,t3)) --> ",type(map(add_ith_ele,t1,t2,t3)))
print("tuple(map(add_ith_ele,t1,t2,t3)) --> ",tuple(map(add_ith_ele,t1,t2,t3)))
print("set(map(add_ith_ele,t1,t2,t3)) --> ",set(map(add_ith_ele,t1,t2,t3)),'\n')

# # the following will give run time error, because, iterables have not been given equal to the parameters
# print("map(add_ith_ele,t1,t3) --> ",map(add_ith_ele,t1,t3))
# print("type(map(add_ith_ele,t1,t3)) --> ",type(map(add_ith_ele,t1,t3)))
# print("tuple(map(add_ith_ele,t1,t3)) --> ",tuple(map(add_ith_ele,t1,t3)))
# print("set(map(add_ith_ele,t1,t3)) --> ",set(map(add_ith_ele,t1,t3)),'\n')

""" here, we can use lambda functoin(anonymous function) """
t4 = (10,20,30,40,50); t5 = ('a','b','c','d'); t6 = ('10','20','30','40')
print("map(lambda n:n*n,t4) --> ",map(lambda n:n*n,t4))
print("list(map(lambda n:n*n,t4)) --> ",list(map(lambda n:n*n,t4)),'\n')
print("map(lambda n:n**n,t4) --> ",map(lambda n:n**n,t4))
print("list(map(lambda n:n**n,t4)) --> ",list(map(lambda n:n**n,t4)),'\n')
print("map(lambda n:n/2,t4) --> ",map(lambda n:n/2,t4))
print("list(map(lambda n:n/2,t4)) --> ",list(map(lambda n:n/2,t4)),'\n')
print("map(lambda x,y:x+y,t6,t5) --> ",map(lambda x,y:x+y,t6,t5))
print("list(map(lambda x,y:x+y,t6,t5)) --> ",list(map(lambda x,y:x+y,t6,t5)),'\n')




# for set
s1 = {34.34,123.0,232.565,789.433}
s2 = {'wad','ajh','aafre','yakf'}
s3 = {'A','B','C','D','E','F'}

""" we can create our function """
def add_itself(x):
    return x+x
print("    list(map(add_itself,s2)) --> ",list(map(add_itself,s2)))
print("    map(add_itself,s2) --> ",map(add_itself,s2))
print("    type(map(add_itself,s2)) --> ",type(map(add_itself,s2)))
print("    id(map(add_itself,s2)) --> ",id(map(add_itself,s2)),'\n')

def power(n):
    return n**2,n**3
print("map(power,s1) --> ",map(power,s1))
print("type(map(power,s1)) --> ",type(map(power,s1)))
print("list(map(power,s1)) --> ",list(map(power,s1)),'\n')

""" we can use built-in-function """
# converting {1,2,3,4,5,6} in float class
print("map(float,(1,2,3,4,5,6)) --> ",map(float,(1,2,3,4,5,6)))
print("type(map(float,(1,2,3,4,5,6))) --> ",type(map(float,(1,2,3,4,5,6))))
print("list(map(float,(1,2,3,4,5,6))) --> ",list(map(float,(1,2,3,4,5,6))),'\n')
# converting {1,2,3,4,5,6} in str class
print("map(str,(1,2,3,4,5,6)) --> ",map(str,(1,2,3,4,5,6)))
print("type(map(str,(1,2,3,4,5,6))) --> ",type(map(str,(1,2,3,4,5,6))))
print("set(map(str([1,2,3,4,5,)])) --> ",set(map(str,(1,2,3,4,5,6))),'\n')

print("using loop: ")
var1 = map(abs,{19,202,-293,200,2,-293,-229})
print(var1,end=': ')
for i in var1:
    print(i,end=',')
print('\n')

""" we can use multiple sets """
# remember, if there are 'n' parameters in function then there must be 'n' iterables 

# add ith elements of lt1, lt2 and lt3
def add_ith_ele(x,y,z):
    return x+y+z
t4 = {'a','b','c'}; t5 = {'d','e','f'}; t6 = {'g','h','i'}
print("map(add_ith_ele,t4,t5,t6) --> ",map(add_ith_ele,t4,t5,t6))
print("type(map(add_ith_ele,t4,t5,t6)) --> ",type(map(add_ith_ele,t4,t5,t6)))
print("tuple(map(add_ith_ele,t4,t5,t6)) --> ",tuple(map(add_ith_ele,t4,t5,t6)))
print("set(map(add_ith_ele,t4,t5,t6)) --> ",set(map(add_ith_ele,t4,t5,t6)),'\n')

# # the following will give run time error, because, iterables have not been given equal to the parameters
# print("map(add_ith_ele,t4,t6) --> ",map(add_ith_ele,t4,t6))
# print("type(map(add_ith_ele,t4,t6)) --> ",type(map(add_ith_ele,t4,t6)))
# print("tuple(map(add_ith_ele,t4,t6)) --> ",tuple(map(add_ith_ele,t4,t6)))
# print("set(map(add_ith_ele,t4,t6)) --> ",set(map(add_ith_ele,t4,t6)),'\n')

""" here, we can use lambda functoin(anonymous function) """
t7 = {10,20,30,40,50}; t8 = ('a','b','c','d'); t9 = {'10','20','30','40'}
print("map(lambda n:n*n,t7) --> ",map(lambda n:n*n,t7))
print("list(map(lambda n:n*n,t7)) --> ",list(map(lambda n:n*n,t7)),'\n')
print("map(lambda n:n**n,t7) --> ",map(lambda n:n**n,t7))
print("list(map(lambda n:n**n,t7)) --> ",list(map(lambda n:n**n,t7)),'\n')
print("map(lambda n:n/2,t7) --> ",map(lambda n:n/2,t7))
print("list(map(lambda n:n/2,t7)) --> ",list(map(lambda n:n/2,t7)),'\n')
print("map(lambda x,y:x+y,t9,t8) --> ",map(lambda x,y:x+y,t9,t8))
print("list(map(lambda x,y:x+y,t9,t8)) --> ",list(map(lambda x,y:x+y,t9,t8)),'\n')