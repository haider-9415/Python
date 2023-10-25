""" str.casefold() --> it works as well as str.lower() works, it also converts those 
    characters in lower case that are not converted in lower case by str.lower() """
# remember it will not accept any argument

str1 = 'tHiS is The leCtUre tO knoW the in-Built fUNCtionS of strinG '
str2 = 'HANZALA'
str3 = 'Naeem'

print("str1.casefold() --> ",str1.casefold(),'\n')
print("str2.casefold() --> ",str2.casefold(),'\n')
print("str3.casefold() --> ",str3.casefold(),'\n')

# on using casefold(), new object is formed, there is no change in main object
print("str2.casefold() --> ",str2.casefold())
print("str2 --> ",str2,'\n')

# without using (), it will not give run-time error
s1 = str3.casefold
print("s1 --> ",s1,'\n')
print("str1.casefold --> ",str1.casefold,'\n')

# it can be used only with a tuple of one element that should be string
print("('HAIDER').casefold() --> ",("HAIDER").casefold(),'\n')

# the following will give run time error
# print("{'naeem'}.casefold() --> ",{"naeem"}.casefold())
# print("['naeem'].casefold() --> ",["naeem"].casefold())
# print("('naeem','haider').casefold() --> ",("naeem",'haider').casefold())

s2 = "@#$ABCDEFG*()".casefold()
print("s2 --> ",s2,'\n')
s3 = "1ABCDEFG".casefold()
print("s3 --> ",s3,'\n')
s4 = "\nHANZALA".casefold()
print("s4 --> ",s4,'\n')
s5 = "  ABCDEFG".casefold()
print("s5 --> ",s5,'\n')
s6 = '["A","B","C"]'.casefold() 
print("s6 --> ",s6,'\n')
s7 = "('A','B','C')".casefold()
print("s7 --> ",s7,'\n')


# difference between lower() & casefold()
# lower() can not be applied on all characters but casefold() can be
s8 = "ß"
print("s8 --> ",s8)
print("s8.lower() --> ",s8.lower())
print("s8.casefold() --> ",s8.casefold(),'\n')

s9 = "ſ"
print("s9 --> ",s9)
print("s9.lower() --> ",s9.lower())
print("s9.casefold() --> ",s9.casefold(),'\n')