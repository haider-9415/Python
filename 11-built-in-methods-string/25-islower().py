"""
   str.islower() --> it returns True if str is in lower case
   otherwise it returns False
"""

s1 = " This Is Hamid'    S Book "
print("s1.islower() --> ",s1.islower(),'\n')

s2 = " this is hamid'    s book "
print("s2.islower() --> ",s2.islower(),'\n')

s3 = " this     is lambda_finction"
print("s3.islower() --> ",s3.islower(),'\n')

s4 = " THIS     IS LAMBDA_FUNCTION"
print("s4.islower() --> ",s4.islower(),'\n')

s5 = "string-methods"
print("s5.islower() --> ",s5.islower(),'\n')

s6 = "string-Method"
print("s6.islower() --> ",s6.islower(),'\n')

s7 = "Xxxxxx@Gmail.Com"
print("s7.islower() --> ",s7.islower(),'\n')

s8 = "xxxxxx@gmail.com"
print("s8.islower() --> ",s8.islower(),'\n')

print("('my name is hanzala'.lower()).islower() --> ",("my name is hanzala".lower()).islower(),'\n')

print("'My name is hanzala'.islower() --> ","My name is hanzala".islower(),'\n')


# without using (), it will not give run time error
print("'MY NAME IS HANZALA'.islower --> ","MY NAME IS HANZALA".islower,'\n')
print("'my name is hanzala'.islower --> ","my name is hanzala".islower,'\n')


# it can be used only with a tuple of one element that should be string
print("('haider').islower() --> ",("haider").islower(),'\n')

# # the following will give run time error
# print("{'haider'}.islower() --> ",{'haider'}.islower())
# print("['haider'].islower() --> ",['haider'].islower())
# print("('naeem','haider').islower() --> ",("naeem",'haider').islower())



print('"62632abcd".islower() --> ',"62632abcd".islower(),'\n')
print('"62632ABCD".islower() --> ',"62632ABCD".islower(),'\n')
print('"".islower() --> ',"".islower(),'\n')
print('"  abcd".islower() --> ',"  abcd".islower(),'\n')
print('"  Abcd".islower() --> ',"  Abcd".islower(),'\n')
print('" ".islower() --> '," ".islower(),'\n')
print('"363-12J".islower() --> ',"363-12J".islower(),'\n')
print('"363+62j".islower() --> ',"363+62j".islower(),'\n')
print('"["a","b","c"]".islower() --> ','["a","b","c"]'.islower(),'\n')
print('"["A","B","C"]".islower() --> ','["A","B","C"]'.islower(),'\n')
print("'('A','B','C')'.islower() --> ","('A','B','C')".islower(),'\n')
print('"["A","B","c"]".islower() --> ','["A","B","c"]'.islower(),'\n')
print('"1425363".islower() --> ','1425363'.islower(),'\n')
print('"1425Z63".islower() --> ','1425Z63'.islower(),'\n')
print('"1425z63".islower() --> ','1425z63'.islower(),'\n')

