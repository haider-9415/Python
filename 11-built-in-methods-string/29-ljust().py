"""
    str.ljust(width,fillchar) --> it works like rjust() but it creates width of 'x' to the right side of the str
"""


s1 = "This Is Hamid'S Book "
print("s1 --> ",s1)
print("s1.ljust(3+len(s1)) --> ",s1.ljust(3+len(s1)),'\n')

s2 = "this is hamid's book "
print("s2 --> ",s2)
print("s2.ljust(5+len(s2),'$') --> ",s2.ljust(5+len(s2),'$'),'\n')

s3 = "this is lambda_finction"
print("s3 --> ",s3)
print("s3.ljust(10+len(s3),'*') --> ",s3.ljust(10+len(s3),'*'),'\n')

s4 = "THIS IS LAMBDA_FUNCTION"
print("s4 --> ",s4)
print("s4.ljust(3+len(s4),'\\') --> ",s4.ljust(3+len(s4),'\\'),'\n')

s5 = "string-methods"
print("s5 --> ",s5)
print("s5.ljust(15+len(s5),'@') --> ",s5.ljust(15+len(s5),'@'),'\n')

s6 = "string-methods"
print("s6 --> ",s6)
print("s6.ljust(15+len(s6),'r') --> ",s6.ljust(15+len(s6),'r'),'\n')

s7 = "string-methods"
print("s7 --> ",s7)
print("s7.ljust(15+len(s7),'3') --> ",s7.ljust(15+len(s7),'3'),'\n')

s8 = "string-methods"
print("s8 --> ",s8)
print("s8.ljust(15+len(s8),'Z') --> ",s8.ljust(15+len(s8),'Z'),'\n')

print("'My name is hanzala'.ljust(8+18,'!') --> ","My name is hanzala".ljust(8+18,'!'),'\n')
print(".........................................................................\n\n")


# without using (), it will not give run time error
print("'MYNAMEISHANZALA'.ljust --> ","MYNAMEISHANZALA".ljust,'\n')
print("'MY NAME IS HANZALA'.ljust --> ","MY NAME IS HANZALA".ljust,'\n')
print(".........................................................................\n\n")


# it can be used only with a tuple of one element that should be string
print("('haider').ljust(4+6,'%') --> ",("haider").ljust(4+6,'%'),'\n')
print("('123haider').ljust(4+9,'%') --> ",("123haider").ljust(13,'%'),'\n')

# # the following will give run time error
# print("{'haider'}.ljust(5+6,'+') --> ",{'haider'}.ljust(5+6,'+'))
# print("['haider'].ljust(5+6,'+') --> ",['haider'].ljust(5+6,'+'))
# print("('naeem','haider').ljust(4+2,',') --> ",("naeem",'haider').ljust(4+2,','))
print(".........................................................................\n\n")


# if we entered length of the string or less than it then it returns the whole string
print('"hanzala".ljust(7) --> ',"hanzala".ljust(7),'\n')
print('"hanzala".ljust(6,";") --> ',"hanzala".ljust(6,";"),'\n')
print('"hanzala".ljust(5,"$") --> ',"hanzala".ljust(5,"$"),'\n')
print('"hanzala".ljust(4) --> ',"hanzala".ljust(4),'\n')
print('"hanzala".ljust(3) --> ',"hanzala".ljust(3),'\n')
print('"hanzala".ljust(2) --> ',"hanzala".ljust(2),'\n')
print('"hanzala".ljust(1,"@") --> ',"hanzala".ljust(1,"@"),'\n')
print('"hanzala".ljust(0,"!") --> ',"hanzala".ljust(0,"!"),'\n')
print('"hanzala".ljust(-1,"$") --> ',"hanzala".ljust(-1,"$"),'\n')
print('"hanzala".ljust(-2) --> ',"hanzala".ljust(-2),'\n')
print('"hanzala".ljust(-5,"*") --> ',"hanzala".ljust(-5,"*"),'\n')
print('"hanzala".ljust(20,"*") --> ',"hanzala".ljust(20,"*"),'\n')
print('"hanzala".ljust(-20,"*") --> ',"hanzala".ljust(-20,"*"),'\n')
print(".........................................................................\n\n")

print('"".ljust(12,"⁴") --> ',"".ljust(12,"⁴"),'\n')
print('" ".ljust(12,"⁴") --> '," ".ljust(12,"⁴"),'\n')
print('"\\n".ljust(12,"⁴") --> ',"\n".ljust(12,"⁴"),'\n')
print('"[1,2,3,4,5]".ljust(20,"*") --> ',"[1,2,3,4,5]".ljust(20,"*"),'\n')
print('"1627.293".ljust(12,"z") --> ',"1627.293".ljust(12,"z"),'\n')
print('"hanzala".ljust(12,"⁴") --> ',"hanzala".ljust(12,"⁴"),'\n')
print('"hanzala".ljust(10,"₉") --> ',"hanzala".ljust(10,"₉"),'\n')
print('"hanzala".ljust(15,"ن") --> ',"hanzala".ljust(15,"ن"),'\n')
print('"hanzala".ljust(13,"غ") --> ',"hanzala".ljust(13,"غ"),'\n')
print('"hanzala".ljust(11,"प") --> ',"hanzala".ljust(11,"प"),'\n')
print('"hanzala".ljust(9,"ठ") --> ',"hanzala".ljust(9,"ठ"),'\n')
print(".........................................................................\n\n")
