""" str.title() --> it converts first letter of each word and the letters lying after \n,number,space,hyphen,
    apostrophe,underscore,at-the-rate,dot,single-qoutes,double-qoutes,etc. in a string in upper case 
    and other capital letters in lower case """
# remember it will not accept any argument

str1 = 'haider'
str2 = 'thiS is the lecTure to knoW the in-built functiONs of stRing '
str3 = 'HANZALA'
print("str1.title() --> ",str1.title(),'\n')
print("str2.title() --> ",str2.title(),'\n')
print("str3.title() --> ",str3.title(),'\n')

s1 = " this is hamid's book "
print("s1.title() --> ",s1.title(),'\n')

s2 = " this is lambda_finction"
print("s2.title() --> ",s2.title(),'\n')

s3 = "string-methods"
print("s3.title() --> ",s3.title(),'\n')

s4 = "xxxxxx@gmail.com"
print("s4.title() --> ",s4.title(),'\n')

s5 = "money$money$money"
print("s5.title() --> ",s5.title(),'\n')

# it can be used only with a tuple of one element that should be string
print("('hanzala naeem').title() --> ",("hanzala naeem").title(),'\n')

# # the following will give run time error
# print("{'naeem'}.title() --> ",{"naeem"}.title())
# print("['naeem'].title() --> ",["naeem"].title())
# print("('naeem','haider').title() --> ",("naeem",'haider').title())

# without using (), it will not give run-time error
s6 = str3.title
print("s6 --> ",s6,'\n')
print("str2.title --> ",str2.title,'\n')


s7 = "@#$%^abcd".title() # it converts a in upper case, because it is after the character ^
print("s7 --> ",s7,'\n')
s8 = "1abcd".title() # it converts a in upper case, because it is after the number
print("s8 --> ",s8,'\n')
s9 = "\nhanzala".title() # it converts h in upper case, because it is after \n
print("s9 --> ",s9,'\n')
s10 = "   abcdefg".title() # it converts a in upper case, because it is after the space
print("s10 --> ",s10,'\n')
s11 = '["a","b","c"]'.title() # it converts a, b and c in upper case, because they are after double qoutes
print("s11 --> ",s11,'\n')
s12 = "('a','b','c')".title() # it converts a, b and c in upper case, because they are after single qoutes
print("s12 --> ",s12,'\n')


