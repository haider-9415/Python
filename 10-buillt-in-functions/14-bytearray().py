"""   
   bytearray(object,encoding,errors) --> it is like bytes() but it returns a mutable object 'bytearray'
   1byte = 8bits & 1bit has 2 possiblities --> 1byte has 2^8 possiblities = 256 possiblities
   bytearray object is an iterable object so we can use loop to print it
"""


# for string

""" we can creat empty bite object """
print("bytearray() --> ",bytearray())
print("type(bytearray()) --> ",type(bytearray()),'\n')

""" if the object is an integer 'n' then it will return an empty byte object of length 'n' 
    remember the integer must be non -ve """
print("bytearray(0) --> ",bytearray(0))
print("type(bytearray(0)) --> ",type(bytearray(0)))
print("len(bytearray(0)) --> ",len(bytearray(0)),'\n')
print("bytearray(1) --> ",bytearray(1))
print("type(bytearray(1)) --> ",type(bytearray(1)))
print("len(bytearray(1)) --> ",len(bytearray(1)),'\n')
print("bytearray(2) --> ",bytearray(2))
print("type(bytearray(2)) --> ",type(bytearray(2)))
print("len(bytearray(2)) --> ",len(bytearray(2)),'\n')
print("bytearray(3) --> ",bytearray(3))
print("type(bytearray(3)) --> ",type(bytearray(3)))
print("len(bytearray(3)) --> ",len(bytearray(3)),'\n')
print("bytearray(10) --> ",bytearray(10))
print("type(bytearray(10)) --> ",type(bytearray(10)))
print("len(bytearray(10)) --> ",len(bytearray(10)),'\n')

""" the object must not be float and complex ,therefore
    the following code will give run time error """
# print("bytearray(15.45) --> ",bytearray(15.45))
# print("type(bytearray(15.45)) --> ",type(bytearray(15.45)))
# print("len(bytearray(15.45)) --> ",len(bytearray(15.45)),'\n')
# print("bytearray(1.0) --> ",bytearray(1.0))
# print("type(bytearray(1.0)) --> ",type(bytearray(1.0)))
# print("len(bytearray(1.0)) --> ",len(bytearray(1.0)),'\n')
# print("bytearray(0.0) --> ",bytearray(0.0))
# print("type(bytearray(0.0)) --> ",type(bytearray(0.0)))
# print("len(bytearray(0.0)) --> ",len(bytearray(0.0)),'\n')
# print("bytearray(15-83j) --> ",bytearray(15-83j))
# print("type(bytearray(15-83j)) --> ",type(bytearray(15-83j)))
# print("len(bytearray(15-83j)) --> ",len(bytearray(15-83j)),'\n')
# print("bytearray(15+0j) --> ",bytearray(15+0j))
# print("type(bytearray(15+0j)) --> ",type(bytearray(15+0j)))
# print("len(bytearray(15+0j)) --> ",len(bytearray(15+0j)),'\n')

""" if the object is string then the parameters 'encoding' & 'errors' are necessary 
    otherwise it will give run time error """

# # the following will give run time error
# print("bytearray('0') --> ",bytearray('0'))
# print("type(bytearray('0')) --> ",type(bytearray('0')))
# print("len(bytearray('0')) --> ",len(bytearray('0')),'\n')
# print("bytearray('A') --> ",bytearray('A'))
# print("type(bytearray('A')) --> ",type(bytearray('A')))
# print("len(bytearray('A')) --> ",len(bytearray('A')),'\n')
# print("bytearray('haider') --> ",bytearray('haider'))
# print("type(bytearray('haider')) --> ",type(bytearray('haider')))
# print("len(bytearray('haider')) --> ",len(bytearray('haider')),'\n')

""" using encoding parameter """
# remember element of the byte object are unicode values
print("bytearray('0',encoding='utf-8') --> ",bytearray('0',encoding='utf-8'))
print("type(bytearray('0',encoding='utf-8')) --> ",type(bytearray('0',encoding='utf-8')))
print("len(bytearray('0',encoding='utf-8')) --> ",len(bytearray('0',encoding='utf-8')))
print("elements of bytearray('0',encoding='utf-8'))",end=': ')
for i in bytearray('0',encoding='utf-8'): print(i,end=',')
print('\n')

print("bytearray('A',encoding='utf-8') --> ",bytearray('A',encoding='utf-8'))
print("type(bytearray('A',encoding='utf-8')) --> ",type(bytearray('A',encoding='utf-8')))
print("len(bytearray('A',encoding='utf-8')) --> ",len(bytearray('A',encoding='utf-8')))
print("elements of bytearray('A',encoding='utf-8'))",end=': ')
for i in bytearray('A',encoding='utf-8'): print(i,end=',')
print('\n')

print("bytearray('haider',encoding='utf-8') --> ",bytearray('haider',encoding='utf-8'))
print("type(bytearray('haider',encoding='utf-8')) --> ",type(bytearray('haider',encoding='utf-8')))
print("len(bytearray('haider',encoding='utf-8')) --> ",len(bytearray('haider',encoding='utf-8')))
print("elements of bytearray('haider',encoding='utf-8'))",end=': ')
for i in bytearray('haider',encoding='utf-8'): print(i,end=',')
print('\n')

print("bytearray('ABCDEFG',encoding='ascii') --> ",bytearray('ABCDEFG',encoding='ascii'))
print("type(bytearray('ABCDEFG',encoding='ascii')) --> ",type(bytearray('ABCDEFG',encoding='ascii')))
print("len(bytearray('ABCDEFG',encoding='ascii')) --> ",len(bytearray('ABCDEFG',encoding='ascii')))
print("elements of bytearray('ABCDEFG',encoding='ascii'))",end=': ')
for i in bytearray('ABCDEFG',encoding='ascii'): print(i,end=',')
print('\n')

print("bytearray('!@#$%^&*()_+',encoding='utf-8') --> ",bytearray('!@#$%^&*()_+',encoding='utf-8'))
print("type(bytearray('!@#$%^&*()_+',encoding='utf-8')) --> ",type(bytearray('!@#$%^&*()_+',encoding='utf-8')))
print("len(bytearray('!@#$%^&*()_+',encoding='utf-8')) --> ",len(bytearray('!@#$%^&*()_+',encoding='utf-8')))
print("elements of bytearray('!@#$%^&*()_+',encoding='utf-8'))",end=': ')
for i in bytearray('!@#$%^&*()_+',encoding='utf-8'): print(i,end=',')
print('\n')

""" using errors parameter """
# the foolowing will give run time error, because, the character 'ي' is not in 'ascii' encoding scheme
# print("bytearray('ABCDيEFG',encoding='ascii') --> ",bytearray('ABCDيEFG',encoding='ascii'))
# print("type(bytearray('ABCDيEFG',encoding='ascii')) --> ",type(bytearray('ABCDيEFG',encoding='ascii')))
# print("len(bytearray('ABCDيEFG',encoding='ascii')) --> ",len(bytearray('ABCDيEFG',encoding='ascii')))
# print("elements of bytearray('ABCDيEFG',encoding='ascii'))",end=': ')
# for i in bytearray('ABCDيEFG',encoding='ascii'): print(i,end=',')
# print('\n')

# errors = 'strict' --> it also gives the error. It is used when you don't know that there is an error
# print("bytearray('ABCDيEFG',encoding='ascii',errors='strict') --> ",bytearray('ABCDيEFG',encoding='ascii',errors='strict'))
# print("type(bytearray('ABCDيEFG',encoding='ascii',errors='strict')) --> ",type(bytearray('ABCDيEFG',encoding='ascii',errors='strict')))
# print("len(bytearray('ABCDيEFG',encoding='ascii',errors='strict')) --> ",len(bytearray('ABCDيEFG',encoding='ascii',errors='strict')))
# print("elements of bytearray('ABCDيEFG',encoding='ascii',errors='strict'))",end=': ')
# for i in bytearray('ABCDيEFG',encoding='ascii',errors='strict'): print(i,end=',')
# print('\n')

# errors = 'ignore' --> it ignores the character causing the error
print("bytearray('ABCDيEFG',encoding='ascii',errors='ignore') --> ",bytearray('ABCDيEFG',encoding='ascii',errors='ignore'))
print("type(bytearray('ABCDيEFG',encoding='ascii',errors='ignore')) --> ",type(bytearray('ABCDيEFG',encoding='ascii',errors='ignore')))
print("len(bytearray('ABCDيEFG',encoding='ascii',errors='ignore')) --> ",len(bytearray('ABCDيEFG',encoding='ascii',errors='ignore')))
print("elements of bytearray('ABCDيEFG',encoding='ascii',errors='ignore'))",end=': ')
for i in bytearray('ABCDيEFG',encoding='ascii',errors='ignore'): print(i,end=',')
print('\n')

# errors = 'replace' --> it replaces the character by ?
print("bytearray('ABCDيEFG',encoding='ascii',errors='replace') --> ",bytearray('ABCDيEFG',encoding='ascii',errors='replace'))
print("type(bytearray('ABCDيEFG',encoding='ascii',errors='replace')) --> ",type(bytearray('ABCDيEFG',encoding='ascii',errors='replace')))
print("len(bytearray('ABCDيEFG',encoding='ascii',errors='replace')) --> ",len(bytearray('ABCDيEFG',encoding='ascii',errors='replace')))
print("elements of bytearray('ABCDيEFG',encoding='ascii',errors='replace'))",end=': ')
for i in bytearray('ABCDيEFG',encoding='ascii',errors='replace'): print(i,end=',')
print('\n')

""" byte object is immutable but bytearray object is mutable """
# the following will give run time error, because, byte object is immutable it does not support item assignment
# b1 = bytes('ABCDEFG',encoding='ascii')
# b1[1] = 70
# b2 = bytes(10)
# b2[2] = 20

# the following will not give run time error, because, bytearray object is mutable it supports item assignment
ba1 = bytearray('ABCDEF',encoding='ascii')

print("elements of ba1, before changing",end=': ')
for i in ba1: print(i,end=',')
print()
ba1[1] = 70; ba1[4] = 80

print("elements of ba1, after changing",end=': ')
for i in ba1: print(i,end=',')
print('\n')


ba2 = bytearray(10)
print("elements of ba2, before changing",end=': ')
for i in ba2: print(i,end=',')
print()

ba2[2] = 20; ba2[5] = 100; ba2[9] = 255; 

print("elements of ba2, after changing",end=': ')
for i in ba2: print(i,end=',')
print('\n')




# for list
""" the list must contain only non -ve integers in range [0,256) """
# the following code will give run time error
lt1 = ['a','b','c','d']; lt2 = [1.2,32.3,93.34,]; lt3 = [1200,912.2,212]; lt4 = [283+8j,723-0j,-219+21j]
# print("bytearray(lt1) --> ",bytearray(lt1))
# print("type(bytearray(lt1)) --> ",type(bytearray(lt1)))
# print("len(bytearray(lt1)) --> ",len(bytearray(lt1)),'\n')
# print("bytearray(lt2) --> ",bytearray(lt2))
# print("type(bytearray(lt2)) --> ",type(bytearray(lt2)))
# print("len(bytearray(lt2)) --> ",len(bytearray(lt2)),'\n')
# print("bytearray(lt3) --> ",bytearray(lt3))
# print("type(bytearray(lt3)) --> ",type(bytearray(lt3)))
# print("len(bytearray(lt3)) --> ",len(bytearray(lt3)),'\n')
# print("bytearray(lt4) --> ",bytearray(lt4))
# print("type(bytearray(lt4)) --> ",type(bytearray(lt4)))
# print("len(bytearray(lt4)) --> ",len(bytearray(lt4)),'\n')


""" remember the byte object made by using a list is displayed in unicode values of its elements 
    but the unicode values do not be the elements of the byte object """
lt5 = [64,65,66,67,68]
print("elements of bytes(lt5)",end=': ')
for i in bytearray(lt5): print(i,end=',')
print()
for i in bytearray(lt5): print(i,"-->",chr(i),end=', ')
print()
print("bytearray(lt5) --> ",bytearray(lt5))
print("type(bytearray(lt5)) --> ",type(bytearray(lt5)))
print("len(bytearray(lt5)) --> ",len(bytearray(lt5)))
print("\n")

lt6 = [90,91,92,93,94,95]
print("elements of bytearray(lt6)",end=': ')
for i in bytearray(lt6): print(i,end=',')
print()
for i in bytearray(lt6): print(i,"-->",chr(i),end=', ')
print()
print("bytearray(lt6) --> ",bytearray(lt6))
print("type(bytearray(lt6)) --> ",type(bytearray(lt6)))
print("len(bytearray(lt6)) --> ",len(bytearray(lt6)))
print("\n")

lt7 = [48,49,50,51,52,54,55,56,57,58]
print("elements of bytes(lt7)",end=': ')
for i in bytearray(lt7): print(i,end=',')
print()
for i in bytearray(lt7): print(i,"-->",chr(i),end=', ')
print()
print("bytearray(lt7) --> ",bytearray(lt7))
print("type(bytearray(lt7)) --> ",type(bytearray(lt7)))
print("len(bytearray(lt7)) --> ",len(bytearray(lt7)))
print("\n")

""" byte object is immutable but bytaarray object is mutable """

# # the following will give run time error, because, byte object is immutable, it does not support item assignment
# b1 = bytes([64,65,66,67,68])
# b1[2] = 70

# the following will not give run time error, because, bytearray object is mutable, it supports item assignment
ba1 = bytearray([64,65,66,67,68])

print("elements of ba1, before changing",end=': ')
for i in ba1: print(i,end=',')
print()

ba1[1] = 70; ba1[4] = 80

print("elements of ba1, after changing",end=': ')
for i in ba1: print(i,end=',')
print('\n')

