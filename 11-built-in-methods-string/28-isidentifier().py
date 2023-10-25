"""
   str.isidentifier() --> it returns True if the string follows RI(rules for identifier)
   otherwise it returns False
"""

s1 = 'hanzala'
print("s1.isidentifier() --> ",s1.isidentifier(),'\n') # it will give true, because, 'hanzala' follows RI
s2 = "_"
print("s2.isidentifier() --> ",s2.isidentifier(),'\n') # it will give true, because, '_' follows RI
s3 = "abcd1234"
print("s3.isidentifier() --> ",s3.isidentifier(),'\n') # it will give true, because, 'abcd1234' follows RI
s4 = "_abcd"
print("s4.isidentifier() --> ",s4.isidentifier(),'\n') # it will give true, because, '_abcd' follows RI
s5 = "abc_5127"
print("s5.isidentifier() --> ",s5.isidentifier(),'\n') # it will give true, because, 'abc_5127' follows RI
s6 = "625abcd"
print("s6.isidentifier() --> ",s6.isidentifier(),'\n') # it will give false, because, '625abcd' does not follow RI
s7 = "string@12"
print("s7.isidentifier() --> ",s7.isidentifier(),'\n') # it will give false, because, 'string@12' does not follow RI
s8 = "_1325$%^"
print("s8.isidentifier() --> ",s8.isidentifier(),'\n') # it will give false, because, '_1325$%^' does not follow RI
s9 = "1234"
print("s9.isidentifier() --> ",s9.isidentifier(),'\n') # it will give false, because, '1234' does not follow RI
s10 = "_1234"
print("s10.isidentifier() --> ",s10.isidentifier(),'\n') # it will give true, because, '_1234' follows RI
s10 = "abcd efgh"
print("s10.isidentifier() --> ",s10.isidentifier(),'\n') # it will give false, because, 'abcd efgh' does not follow RI
# similarly
print("'haider'.isidentifier() --> ","haider".isidentifier(),'\n')
print("'_'.isidentifier() --> ","_".isidentifier(),'\n')
print("'26363haider'.isidentifier() --> ","26363haider".isidentifier(),'\n')
print("'hai#$%!der'.isidentifier() --> ","hai#$%!der".isidentifier(),'\n')



# without using (), it will not give run time error
print("'MYNAMEISHANZALA'.isidentifier --> ","MYNAMEISHANZALA".isidentifier,'\n')
print("'MY NAME IS HANZALA'.isidentifier --> ","MY NAME IS HANZALA".isidentifier,'\n')



# it can be used only with a tuple of one element that should be string
print("('haider').isidentifier() --> ",("haider").isidentifier(),'\n')
print("('123haider').isidentifier() --> ",("123haider").isidentifier(),'\n')

# # the following will give run time error
# print("{'haider'}.isidentifier() --> ",{'haider'}.isidentifier())
# print("['haider'].isidentifier() --> ",['haider'].isidentifier())
# print("('naeem','haider').isidentifier() --> ",("naeem",'haider').isidentifier())



print("''.isidentifier() --> ","".isidentifier(),'\n')
print("' '.isidentifier() --> "," ".isidentifier(),'\n')
print("'\\n'.isidentifier() --> ","\n".isidentifier(),'\n')
print("'\\r'.isidentifier() --> ","\r".isidentifier(),'\n')
print("'22.2873'.isidentifier() --> ","22.2873".isidentifier(),'\n')
print("'-1827'.isidentifier() --> ","-1827".isidentifier(),'\n')
print("'-192.282'.isidentifier() --> ","-192.282".isidentifier(),'\n')
print("'252-82j'.isidentifier() --> ","252-82j".isidentifier(),'\n')
print("'182+82J'.isidentifier() --> ","182+82J".isidentifier(),'\n')
print("'hanzala naeem'.isidentifier() --> ","hanzala naeem".isidentifier(),'\n')
print("'hanzala_naeem'.isidentifier() --> ","hanzala_naeem".isidentifier(),'\n')
print("'  hanzalanaeem'.isidentifier() --> ","  hanzalanaeem".isidentifier(),'\n')
print("'hanzalanaeem  '.isidentifier() --> ","hanzalanaeem  ".isidentifier(),'\n')
print("'hanzala\\nnaeem'.isidentifier() --> ","hanzala\nnaeem".isidentifier(),'\n')
print("'abcd²'.isidentifier() --> ","abcd²".isidentifier(),'\n')
print("'_26⁸'.isidentifier() --> ","_26⁸".isidentifier(),'\n')
print("'¹²₁₂'.isidentifier() --> ","¹²₁₂".isidentifier(),'\n')
print("'10¹²'.isidentifier() --> ","10¹²".isidentifier(),'\n')
print("'n₁₂'.isidentifier() --> ","n₁₂".isidentifier(),'\n')

