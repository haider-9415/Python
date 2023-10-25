""" str.swapcase()  --> to show capital letters in lower case & small letters in upper case """
# remember it will not accept any argument


str1 = 'haider'
str2 = 'ThiS is tHe lECtUre tO knOW the In-BuIlt FUNCtions of sTrInG '
str3 = 'HANZALA'
str4 = 'Naeem'

print("str1.swapcase() --> ",str1.swapcase(),'\n')
print("str2.swapcase() --> ",str2.swapcase(),'\n')
print("str3.swapcase() --> ",str3.swapcase(),'\n')
print("str4.swapcase() --> ",str4.swapcase(),'\n')

# on using swapcase(), new object is formed, there is no change in main object
print("str3.swapcase() --> ",str3.swapcase())
print("str3 --> ",str3,'\n')

# without using (), it will not give run-time error
s1 = str3.swapcase
print("s1 --> ",s1,'\n')
print("str1.swapcase --> ",str1.swapcase,'\n')

# it can be used only with a tuple of one element that should be string
print("('HAIDER').swapcase() --> ",("HAIDER").swapcase(),'\n')
print("('this IS string NOT TUPLE').swapcase() --> ",("this IS string NOT TUPLE").swapcase(),'\n')

# the following will give run time error
# print("{'naeem'}.swapcase() --> ",{"naeem"}.swapcase())
# print("['naeem'].swapcase() --> ",["naeem"].swapcase())
# print("('naeem','haider').swapcase() --> ",("naeem",'haider').swapcase())

s2 = "@#$abcdEFGH*()".swapcase()
print("s2 --> ",s2,'\n')
s3 = "1aBcDeFg".swapcase()
print("s3 --> ",s3,'\n')
s4 = "\nHANZALA".swapcase()
print("s4 --> ",s4,'\n')
s5 = "  AbCdEfG".swapcase()
print("s5 --> ",s5,'\n')
s6 = '["a","b","c"]'.swapcase()
print("s6 --> ",s6,'\n')
s7 = "('A','B','C')".swapcase()
print("s7 --> ",s7,'\n')
s8 = "ß".swapcase()
print("s8 --> ",s8,'\n')
s9 = "ſ".swapcase()
print("s9 --> ",s9,'\n')

# if wu use two times swapcase() on a string then we get that string
s2 = "@#$abcdEFGH*()".swapcase().swapcase()
print("s2 --> ",s2,'\n')
s3 = "1aBcDeFg".swapcase().swapcase()
print("s3 --> ",s3,'\n')
s4 = "\nHANZALA".swapcase().swapcase()
print("s4 --> ",s4,'\n')
s5 = "  AbCdEfG".swapcase().swapcase()
print("s5 --> ",s5,'\n')
s6 = '["a","b","c"]'.swapcase().swapcase()
print("s6 --> ",s6,'\n')
s7 = "('A','B','C')".swapcase().swapcase()
print("s7 --> ",s7,'\n')
s8 = "ß".swapcase().swapcase()
print("s8 --> ",s8,'\n')
s9 = "ſ".swapcase().swapcase()
print("s9 --> ",s9,'\n')