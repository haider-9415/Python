""" str.capitalize() --> it converts only first letter of a string in upper case and 
    other capital letters in lower case """
# remember it will not accept any argument

str1 = 'haider'
str2 = 'this is the lecture to know the in-built functions of string '
str3 = 'HANZALA'
print("str1.capitalize() --> ",str1.capitalize(),'\n')
print("str2.capitalize() --> ",str2.capitalize(),'\n')
print("str3.capitalize() --> ",str3.capitalize(),'\n')

s1 = str1.capitalize()
print("s1.capitalize() --> ",s1.capitalize(),'\n')

# on using capitalize(), new object is formed, there is no change in main object
print("str3.capitalize() --> ",str3.capitalize())
print("str3 --> ",str3,'\n')

# without using (), it will not give run-time error
s2 = str3.capitalize
print("s2 --> ",s2,'\n')
print("str1.capitalize --> ",str1.capitalize,'\n')

# if capital letter of the first letter does not exist then it will show the string as it is
s3 = "@#$%^&*()".capitalize()
print("s3 --> ",s3,'\n')
s4 = "1abcd".capitalize()
print("s4 --> ",s4,'\n')
s5 = "\nhanzala".capitalize()
print("s5 --> ",s5,'\n')
s6 = "  abcd".capitalize()
print("s6 --> ",s6,'\n')

# it can be used only with a tuple of one element that should be string
print("('naeem').capitalize() --> ",("naeem").capitalize())

# the following will give run time error
# print("{'naeem'}.capitalize() --> ",{"naeem"}.capitalize())
# print("['naeem'].capitalize() --> ",["naeem"].capitalize())
# print("('naeem','haider').capitalize() --> ",("naeem",'haider').capitalize())

