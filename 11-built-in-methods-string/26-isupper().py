"""
   str.isupper() --> it returns True if str is in upper case
   otherwise it returns False
"""



s1 = " This Is Hamid'    S Book "
print("s1.isupper() --> ",s1.isupper(),'\n')

s2 = " THIS IS HAMID'    S BOOK "
print("s2.isupper() --> ",s2.isupper(),'\n')

s3 = " this     is lambda_finction"
print("s3.isupper() --> ",s3.isupper(),'\n')

s4 = " THIS     IS LAMBDA_FUNCTION"
print("s4.isupper() --> ",s4.isupper(),'\n')

s5 = "String-methods"
print("s5.isupper() --> ",s5.isupper(),'\n')

s6 = "STRING-METHODS"
print("s6.isupper() --> ",s6.isupper(),'\n')


s7 = "xxxxxx@Gmail.Com"
print("s7.isupper() --> ",s7.isupper(),'\n')

s8 = "XXXXXX@GMAIL.COM"
print("s8.isupper() --> ",s8.isupper(),'\n')

print("('my name is hanzala'.upper()).isupper() --> ",("my name is hanzala".upper()).isupper(),'\n')

print("'my name is hanzala'.isupper() --> ","my name is hanzala".isupper(),'\n')


# without using (), it will not give run time error
print("'MY NAME IS HANZALA'.isupper --> ","MY NAME IS HANZALA".isupper,'\n')
print("'my name is hanzala'.isupper --> ","my name is hanzala".isupper,'\n')


# it can be used only with a tuple of one element that should be string
print("('HANZALA NAEEM').istitle() --> ",("HANZALA NAEEM").isupper(),'\n')

# # # the following will give run time error
# print("{'HANZALA NAEEM'}.isupper() --> ",{'HANZALA NAEEM'}.isupper())
# print("['HANZALA NAEEM'].isupper() --> ",['HANZALA NAEEM'].isupper())
# print("('NAEEM','HAIDER').isupper() --> ",("NAEEM",'HAIDER').isupper())


print('"62632Abcd".isupper() --> ',"62632Abcd".isupper(),'\n')
print('"62632ABCD".isupper() --> ',"62632ABCD".isupper(),'\n')
print('"".isupper() --> ',"".isupper(),'\n')
print('"  abcd".isupper() --> ',"  abcd".isupper(),'\n')
print('"  ABCD".isupper() --> ',"  ABCD".isupper(),'\n')
print('" ".isupper() --> '," ".isupper(),'\n')
print('"363-12J".isupper() --> ',"363-12J".isupper(),'\n')
print('"363+62j".isupper() --> ',"363+62j".isupper(),'\n')
print('"["a","b","c"]".isupper() --> ','["a","b","c"]'.isupper(),'\n')
print('"["A","B","C"]".isupper() --> ','["A","B","C"]'.isupper(),'\n')
print("'('A','B','C')'.isupper() --> ","('A','B','C')".isupper(),'\n')
print('"["A","B","c"]".isupper() --> ','["A","B","c"]'.isupper(),'\n')
print('"1425363".isupper() --> ','1425363'.isupper(),'\n')
print('"1425Z63".isupper() --> ','1425Z63'.isupper(),'\n')

