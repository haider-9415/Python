"""
   bytes(object,encoding,errors) --> it returns an immutable byte object
   1byte = 8bits & 1bit has 2 possiblities --> 1byte has 2^8 possiblities = 256 possiblities
   byte object is an iterable object so we can use loop to print it6
"""



# for string
""" we can creat empty bite object """
print("bytes() --> ",bytes())
print("type(bytes()) --> ",type(bytes()),'\n')

""" if the object is an integer 'n' then it will return an empty byte object of length 'n' 
    remember the integer must be non -ve """
print("bytes(0) --> ",bytes(0))
print("type(bytes(0)) --> ",type(bytes(0)))
print("len(bytes(0)) --> ",len(bytes(0)),'\n')
print("bytes(1) --> ",bytes(1))
print("type(bytes(1)) --> ",type(bytes(1)))
print("len(bytes(1)) --> ",len(bytes(1)),'\n')
print("bytes(2) --> ",bytes(2))
print("type(bytes(2)) --> ",type(bytes(2)))
print("len(bytes(2)) --> ",len(bytes(2)),'\n')
print("bytes(3) --> ",bytes(3))
print("type(bytes(3)) --> ",type(bytes(3)))
print("len(bytes(3)) --> ",len(bytes(3)),'\n')
print("bytes(10) --> ",bytes(10))
print("type(bytes(10)) --> ",type(bytes(10)))
print("len(bytes(10)) --> ",len(bytes(10)),'\n')
print("bytes(15) --> ",bytes(15))
print("type(bytes(15)) --> ",type(bytes(15)))
print("len(bytes(15)) --> ",len(bytes(15)),'\n')

""" the object must not be float and complex ,therefore
    the following code will give run time error """
# print("bytes(15.45) --> ",bytes(15.45))
# print("type(bytes(15.45)) --> ",type(bytes(15.45)))
# print("len(bytes(15.45)) --> ",len(bytes(15.45)),'\n')
# print("bytes(1.0) --> ",bytes(1.0))
# print("type(bytes(1.0)) --> ",type(bytes(1.0)))
# print("len(bytes(1.0)) --> ",len(bytes(1.0)),'\n')
# print("bytes(0.0) --> ",bytes(0.0))
# print("type(bytes(0.0)) --> ",type(bytes(0.0)))
# print("len(bytes(0.0)) --> ",len(bytes(0.0)),'\n')
# print("bytes(15-83j) --> ",bytes(15-83j))
# print("type(bytes(15-83j)) --> ",type(bytes(15-83j)))
# print("len(bytes(15-83j)) --> ",len(bytes(15-83j)),'\n')
# print("bytes(15+0j) --> ",bytes(15+0j))
# print("type(bytes(15+0j)) --> ",type(bytes(15+0j)))
# print("len(bytes(15+0j)) --> ",len(bytes(15+0j)),'\n')

""" if the object is string then the parameters 'encoding' & 'errors' are necessary 
    otherwise it will give run time error """

# # the following will give run time error
# print("bytes('0') --> ",bytes('0'))
# print("type(bytes('0')) --> ",type(bytes('0')))
# print("len(bytes('0')) --> ",len(bytes('0')),'\n')
# print("bytes('A') --> ",bytes('A'))
# print("type(bytes('A')) --> ",type(bytes('A')))
# print("len(bytes('A')) --> ",len(bytes('A')),'\n')
# print("bytes('haider') --> ",bytes('haider'))
# print("type(bytes('haider')) --> ",type(bytes('haider')))
# print("len(bytes('haider')) --> ",len(bytes('haider')),'\n')

""" using encoding parameter """
# remember element of the byte object are unicode values
print("bytes('0',encoding='utf-8') --> ",bytes('0',encoding='utf-8'))
print("type(bytes('0',encoding='utf-8')) --> ",type(bytes('0',encoding='utf-8')))
print("len(bytes('0',encoding='utf-8')) --> ",len(bytes('0',encoding='utf-8')))
print("elements of bytes('0',encoding='utf-8'))",end=': ')
for i in bytes('0',encoding='utf-8'): print(i,end=',')
print('\n')

print("bytes('A',encoding='utf-8') --> ",bytes('A',encoding='utf-8'))
print("type(bytes('A',encoding='utf-8')) --> ",type(bytes('A',encoding='utf-8')))
print("len(bytes('A',encoding='utf-8')) --> ",len(bytes('A',encoding='utf-8')))
print("elements of bytes('A',encoding='utf-8'))",end=': ')
for i in bytes('A',encoding='utf-8'): print(i,end=',')
print('\n')

print("bytes('haider',encoding='utf-8') --> ",bytes('haider',encoding='utf-8'))
print("type(bytes('haider',encoding='utf-8')) --> ",type(bytes('haider',encoding='utf-8')))
print("len(bytes('haider',encoding='utf-8')) --> ",len(bytes('haider',encoding='utf-8')))
print("elements of bytes('haider',encoding='utf-8'))",end=': ')
for i in bytes('haider',encoding='utf-8'): print(i,end=',')
print('\n')

print("bytes('ABCDEFG',encoding='ascii') --> ",bytes('ABCDEFG',encoding='ascii'))
print("type(bytes('ABCDEFG',encoding='ascii')) --> ",type(bytes('ABCDEFG',encoding='ascii')))
print("len(bytes('ABCDEFG',encoding='ascii')) --> ",len(bytes('ABCDEFG',encoding='ascii')))
print("elements of bytes('ABCDEFG',encoding='ascii'))",end=': ')
for i in bytes('ABCDEFG',encoding='ascii'): print(i,end=',')
print('\n')

print("bytes('!@#$%^&*()_+',encoding='utf-8') --> ",bytes('!@#$%^&*()_+',encoding='utf-8'))
print("type(bytes('!@#$%^&*()_+',encoding='utf-8')) --> ",type(bytes('!@#$%^&*()_+',encoding='utf-8')))
print("len(bytes('!@#$%^&*()_+',encoding='utf-8')) --> ",len(bytes('!@#$%^&*()_+',encoding='utf-8')))
print("elements of bytes('!@#$%^&*()_+',encoding='utf-8'))",end=': ')
for i in bytes('!@#$%^&*()_+',encoding='utf-8'): print(i,end=',')
print('\n')

""" using errors parameter """

# # the foolowing will give run time error, because, the character 'ي' is not in 'ascii' encoding scheme
# print("bytes('ABCDيEFG',encoding='ascii') --> ",bytes('ABCDيEFG',encoding='ascii'))
# print("type(bytes('ABCDيEFG',encoding='ascii')) --> ",type(bytes('ABCDيEFG',encoding='ascii')))
# print("len(bytes('ABCDيEFG',encoding='ascii')) --> ",len(bytes('ABCDيEFG',encoding='ascii')))
# print("elements of bytes('ABCDيEFG',encoding='ascii'))",end=': ')
# for i in bytes('ABCDيEFG',encoding='ascii'): print(i,end=',')
# print('\n')

# # errors = 'strict' --> it also gives the error. It is used when you don't know that there is an error
# print("bytes('ABCDيEFG',encoding='ascii',errors='strict') --> ",bytes('ABCDيEFG',encoding='ascii',errors='strict'))
# print("type(bytes('ABCDيEFG',encoding='ascii',errors='strict')) --> ",type(bytes('ABCDيEFG',encoding='ascii',errors='strict')))
# print("len(bytes('ABCDيEFG',encoding='ascii',errors='strict')) --> ",len(bytes('ABCDيEFG',encoding='ascii',errors='strict')))
# print("elements of bytes('ABCDيEFG',encoding='ascii',errors='strict'))",end=': ')
# for i in bytes('ABCDيEFG',encoding='ascii',errors='strict'): print(i,end=',')
# print('\n')

# errors = 'ignore' --> it ignores the character causing the error
print("bytes('ABCDيEFG',encoding='ascii',errors='ignore') --> ",bytes('ABCDيEFG',encoding='ascii',errors='ignore'))
print("type(bytes('ABCDيEFG',encoding='ascii',errors='ignore')) --> ",type(bytes('ABCDيEFG',encoding='ascii',errors='ignore')))
print("len(bytes('ABCDيEFG',encoding='ascii',errors='ignore')) --> ",len(bytes('ABCDيEFG',encoding='ascii',errors='ignore')))
print("elements of bytes('ABCDيEFG',encoding='ascii',errors='ignore'))",end=': ')
for i in bytes('ABCDيEFG',encoding='ascii',errors='ignore'): print(i,end=',')
print('\n')

# errors = 'replace' --> it replaces the character by ?
print("bytes('ABCDيEFG',encoding='ascii',errors='replace') --> ",bytes('ABCDيEFG',encoding='ascii',errors='replace'))
print("type(bytes('ABCDيEFG',encoding='ascii',errors='replace')) --> ",type(bytes('ABCDيEFG',encoding='ascii',errors='replace')))
print("len(bytes('ABCDيEFG',encoding='ascii',errors='replace')) --> ",len(bytes('ABCDيEFG',encoding='ascii',errors='replace')))
print("elements of bytes('ABCDيEFG',encoding='ascii',errors='replace'))",end=': ')
for i in bytes('ABCDيEFG',encoding='ascii',errors='replace'): print(i,end=',')
print('\n')




# for list
""" the list must contain only non -ve integers in range [0,256) """

# the following code will give run time error
lt1 = ['a','b','c','d']; lt2 = [1.2,32.3,93.34,]; lt3 = ['as','be',120,912.2,212]; lt4 = [283+8j,723-0j,-219+21j]
# print("bytes(lt1) --> ",bytes(lt1))
# print("type(bytes(lt1)) --> ",type(bytes(lt1)))
# print("len(bytes(lt1)) --> ",len(bytes(lt1)),'\n')
# print("bytes(lt2) --> ",bytes(lt2))
# print("type(bytes(lt2)) --> ",type(bytes(lt2)))
# print("len(bytes(lt2)) --> ",len(bytes(lt2)),'\n')
# print("bytes(lt3) --> ",bytes(lt3))
# print("type(bytes(lt3)) --> ",type(bytes(lt3)))
# print("len(bytes(lt3)) --> ",len(bytes(lt3)),'\n')
# print("bytes(lt4) --> ",bytes(lt4))
# print("type(bytes(lt4)) --> ",type(bytes(lt4)))
# print("len(bytes(lt4)) --> ",len(bytes(lt4)),'\n')

""" remember the byte object made by using a list is displayed in unicode values of its elements 
    but the unicode values do not be the elements of the byte object """
lt5 = [64,65,66,67,68]
print("elements of bytes(lt5)",end=': ')
for i in bytes(lt5): print(i,end=',')
print()
for i in bytes(lt5): print(i,"-->",chr(i),end=', ')
print()
print("bytes(lt5) --> ",bytes(lt5))
print("type(bytes(lt5)) --> ",type(bytes(lt5)))
print("len(bytes(lt5)) --> ",len(bytes(lt5)))
print("\n")

lt6 = [90,91,92,93,94,95]
print("elements of bytes(lt6)",end=': ')
for i in bytes(lt6): print(i,end=',')
print()
for i in bytes(lt6): print(i,"-->",chr(i),end=', ')
print()
print("bytes(lt6) --> ",bytes(lt6))
print("type(bytes(lt6)) --> ",type(bytes(lt6)))
print("len(bytes(lt6)) --> ",len(bytes(lt6)))
print("\n")

lt7 = [48,49,50,51,52,54,55,56,57,58]
print("elements of bytes(lt7)",end=': ')
for i in bytes(lt7): print(i,end=',')
print()
for i in bytes(lt7): print(i,"-->",chr(i),end=', ')
print()
print("bytes(lt7) --> ",bytes(lt7))
print("type(bytes(lt7)) --> ",type(bytes(lt7)))
print("len(bytes(lt7)) --> ",len(bytes(lt7)))
print("\n")
