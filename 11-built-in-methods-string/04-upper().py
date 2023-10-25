""" str.upper() --> it converts all characters in a string in upper case 
    those characters which upper case does not exist, it shows them as it is """
# remember it will not accept any argument


str1 = 'haider'
str2 = 'this is the lecture to know the in-built functions of string '
str3 = 'Naeem'
str4 = 'HAnZalA'

print("str1.upper() --> ",str1.upper(),'\n')
print("str2.upper() --> ",str2.upper(),'\n')
print("str3.upper() --> ",str3.upper(),'\n')
print("str4.upper() --> ",str4.upper(),'\n')

# on using upper(), new object is formed, there is no change in main object
print("str3.upper() --> ",str3.upper())
print("str3 --> ",str3,'\n')

# without using (), it will not give run-time error
s1 = str3.upper
print("s1 --> ",s1,'\n')
print("str1.upper --> ",str1.upper,'\n')

# it can be used only with a tuple of one element that should be string
print("('naeem').upper() --> ",("naeem").upper(),'\n')

# the following will give run time error
# print("{'naeem'}.upper() --> ",{"naeem"}.upper())
# print("['naeem'].upper() --> ",["naeem"].upper())
# print("('naeem','haider').upper() --> ",("naeem",'haider').upper())


s2 = "@#$abcd*()".upper()
print("s2 --> ",s2,'\n')
s3 = "1abcd".upper()
print("s3 --> ",s3,'\n')
s4 = "\nhanzala".upper()
print("s4 --> ",s4,'\n')
s5 = "  abcd".upper()
print("s5 --> ",s5,'\n')
s6 = '["a","b","c"]'.title() 
print("s6 --> ",s6,'\n')
s7 = "('a','b','c')".title()
print("s7 --> ",s7,'\n')