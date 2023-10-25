"""
   str.zfill(width) --> it works like zfill(), but, in zfill(), we can use characters according to us and in zfill()
   we can not do this
   if str starts with '+' or '-' then 0s are filled after it
"""

s1 = "This Is Hamid'S Book "
print("s1 --> ",s1)
print("s1.zfill(3+len(s1)) --> ",s1.zfill(3+len(s1)),'\n')

s2 = "this is hamid's book "
print("s2 --> ",s2)
print("s2.zfill(5+len(s2)) --> ",s2.zfill(5+len(s2)),'\n')

s3 = "this is lambda_finction"
print("s3 --> ",s3)
print("s3.zfill(10+len(s3)) --> ",s3.zfill(10+len(s3)),'\n')

s4 = "THIS IS LAMBDA_FUNCTION"
print("s4 --> ",s4)
print("s4.zfill(3+len(s4)) --> ",s4.zfill(3+len(s4)),'\n')

s5 = "string-methods"
print("s5 --> ",s5)
print("s5.zfill(15+len(s5)) --> ",s5.zfill(15+len(s5)),'\n')

s6 = "string-methods"
print("s6 --> ",s6)
print("s6.zfill(15+len(s6)) --> ",s6.zfill(15+len(s6)),'\n')

s7 = "string-methods"
print("s7 --> ",s7)
print("s7.zfill(15+len(s7)) --> ",s7.zfill(15+len(s7)),'\n')

s8 = "string-methods"
print("s8 --> ",s8)
print("s8.zfill(15+len(s8)) --> ",s8.zfill(15+len(s8)),'\n')

s9 = "12345678910"
print("s9 --> ",s9)
print("s9.zfill(15+len(s9)) --> ",s9.zfill(15+len(s9)),'\n')

s10 = "+678910"
print("s10 --> ",s10)
print("s10.zfill(15+len(s10)) --> ",s10.zfill(15+len(s10)),'\n')

s11 = "-12345"
print("s11 --> ",s11)
print("s11.zfill(15+len(s11)) --> ",s11.zfill(15+len(s11)),'\n')

s12 = "+abcd"
print("s12 --> ",s12)
print("s12.zfill(15+len(s12)) --> ",s12.zfill(15+len(s12)),'\n')

s13 = "-efgh"
print("s13 --> ",s13)
print("s13.zfill(15+len(s13)) --> ",s13.zfill(15+len(s13)),'\n')

print("'My name is hanzala'.zfill(8+18) --> ","My name is hanzala".zfill(8+18),'\n')
print(".........................................................................\n\n")


# without using (), it will not give run time error
print("'102030405060708090'.zfill --> ","102030405060708090".zfill,'\n')
print("'MY NAME IS HANZALA'.zfill --> ","MY NAME IS HANZALA".zfill,'\n')
print(".........................................................................\n\n")



# it can be used only with a tuple of one element that should be string
print("('haider').zfill(4+6) --> ",("haider").zfill(4+6),'\n')
print("('123haider').zfill(4+9) --> ",("123haider").zfill(13),'\n')

# # the following will give run time error
# print("{'haider'}.zfill(5+6) --> ",{'haider'}.zfill(5+6))
# print("['haider'].zfill(5+6) --> ",['haider'].zfill(5+6))
# print("('naeem','haider').zfill(4+2) --> ",("naeem",'haider').zfill(4+2))
print(".........................................................................\n\n")


print('"".zfill(12) --> ',"".zfill(12),'\n')
print('" ".zfill(12) --> '," ".zfill(12),'\n')
print('"\\n".zfill(12) --> ',"\n".zfill(12),'\n')
print('"[1,2,3,4,5]".zfill(20) --> ',"[1,2,3,4,5]".zfill(20),'\n')
print('"1627.293".zfill(12) --> ',"1627.293".zfill(12),'\n')
print('"hanzala".zfill(12) --> ',"hanzala".zfill(12),'\n')
print('"@#$%&*()".zfill(10) --> ',"@#$%&*()".zfill(10),'\n')
print('"123&^&*".zfill(10) --> ',"123&^&*".zfill(10),'\n')
print('"abcd&^%!@#".zfill(20) --> ',"abcd&^%!@#".zfill(20),'\n')
print('"han827#$$-923239j".zfill(20) --> ',"han827#$$-923239j".zfill(20),'\n')
print('"++++abcd$#$$837".zfill(25) --> ',"++++abcd$#$$837".zfill(25),'\n')
print('"-----abcd$#$$837".zfill(25) --> ',"-----abcd$#$$837".zfill(25),'\n')
print('"-+++abcd$#$$837".zfill(25) --> ',"-+++abcd$#$$837".zfill(25),'\n')
print('"+----abcd$#$$837".zfill(25) --> ',"+----abcd$#$$837".zfill(25),'\n')



# if we entered length of the string or less than it then it returns the whole string
print('"hanzala".zfill(7) --> ',"hanzala".zfill(7),'\n')
print('"hanzala".zfill(6) --> ',"hanzala".zfill(6),'\n')
print('"hanzala".zfill(5) --> ',"hanzala".zfill(5),'\n')
print('"hanzala".zfill(4) --> ',"hanzala".zfill(4),'\n')
print('"hanzala".zfill(3) --> ',"hanzala".zfill(3),'\n')
print('"hanzala".zfill(2) --> ',"hanzala".zfill(2),'\n')
print('"hanzala".zfill(1) --> ',"hanzala".zfill(1),'\n')
print('"hanzala".zfill(0) --> ',"hanzala".zfill(0),'\n')
print('"hanzala".zfill(-1) --> ',"hanzala".zfill(-1),'\n')
print('"hanzala".zfill(-2) --> ',"hanzala".zfill(-2),'\n')
print('"hanzala".zfill(-5) --> ',"hanzala".zfill(-5),'\n')
print('"hanzala".zfill(20) --> ',"hanzala".zfill(20),'\n')
print('"hanzala".zfill(-20) --> ',"hanzala".zfill(-20),'\n')
print(".........................................................................\n\n")