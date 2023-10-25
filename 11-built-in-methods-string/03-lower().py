""" str.lower() --> to show all characters in lower case """
# remember it will not accept any argument


str1 = 'tHiS is The leCtUre tO knoW the in-Built fUNCtionS of strinG '
str2 = 'HANZALA'
str3 = 'Naeem'

print("str1.lower() --> ",str1.lower(),'\n')
print("str2.lower() --> ",str2.lower(),'\n')
print("str3.lower() --> ",str3.lower(),'\n')

# on using lower(), new object is formed, there is no change in main object
print("str2.lower() --> ",str2.lower())
print("str2 --> ",str2,'\n')

# without using (), it will not give run-time error
s1 = str3.lower
print("s1 --> ",s1,'\n')
print("str1.lower --> ",str1.lower,'\n')

# it can be used only with a tuple of one element that should be string
print("('HAIDER').lower() --> ",("HAIDER").lower(),'\n')

# the following will give run time error
# print("{'naeem'}.lower() --> ",{"naeem"}.lower())
# print("['naeem'].lower() --> ",["naeem"].lower())
# print("('naeem','haider').lower() --> ",("naeem",'haider').lower())

s2 = "@#$ABCDEFG*()".lower()
print("s2 --> ",s2,'\n')
s3 = "1ABCDEFG".lower()
print("s3 --> ",s3,'\n')
s4 = "\nHANZALA".lower()
print("s4 --> ",s4,'\n')
s5 = "  ABCDEFG".lower()
print("s5 --> ",s5,'\n')
s6 = '["A","B","C"]'.lower() 
print("s6 --> ",s6,'\n')
s7 = "('A','B','C')".lower()
print("s7 --> ",s7,'\n')