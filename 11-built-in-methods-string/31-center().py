"""
   str.center(width,fillchar) --> it creates a string 's' of width 'x' and sligns the 'str' in center of 's'
   and it fills other empty blocks using fillchar
"""

s1 = "This Is Hamid'S Book "
print("s1 --> ",s1)
print("s1.center(3+len(s1)) --> ",s1.center(3+len(s1)),'\n')

s2 = "this is hamid's book "
print("s2 --> ",s2)
print("s2.center(5+len(s2),'$') --> ",s2.center(5+len(s2),'$'),'\n')

s3 = "this is lambda_finction"
print("s3 --> ",s3)
print("s3.center(10+len(s3),'*') --> ",s3.center(10+len(s3),'*'),'\n')

s4 = "THIS IS LAMBDA_FUNCTION"
print("s4 --> ",s4)
print("s4.center(3+len(s4),'\\') --> ",s4.center(3+len(s4),'\\'),'\n')

s5 = "string-methods"
print("s5 --> ",s5)
print("s5.center(15+len(s5),'@') --> ",s5.center(15+len(s5),'@'),'\n')

s6 = "string-methods"
print("s6 --> ",s6)
print("s6.center(15+len(s6),'r') --> ",s6.center(15+len(s6),'r'),'\n')

s7 = "string-methods"
print("s7 --> ",s7)
print("s7.center(15+len(s7),'3') --> ",s7.center(15+len(s7),'3'),'\n')

s8 = "string-methods"
print("s8 --> ",s8)
print("s8.center(15+len(s8),'Z') --> ",s8.center(15+len(s8),'Z'),'\n')

print("'My name is hanzala'.center(8+18,'!') --> ","My name is hanzala".center(8+18,'!'),'\n')
print(".........................................................................\n\n")


# without using (), it will not give run time error
print("'MYNAMEISHANZALA'.center --> ","MYNAMEISHANZALA".center,'\n')
print("'MY NAME IS HANZALA'.center --> ","MY NAME IS HANZALA".center,'\n')
print(".........................................................................\n\n")


# it can be used only with a tuple of one element that should be string
print("('haider').center(4+6,'%') --> ",("haider").center(4+6,'%'),'\n')
print("('123haider').center(13,'%') --> ",("123haider").center(13,'%'),'\n')

# # the following will give run time error
# print("{'haider'}.center(5+6,'+') --> ",{'haider'}.center(5+6,'+'))
# print("['haider'].center(5+6,'+') --> ",['haider'].center(5+6,'+'))
# print("('naeem','haider').center(4+2,',') --> ",("naeem",'haider').center(4+2,','))
print(".........................................................................\n\n")


# if we entered length of the string or less than it then it returns the whole string
print('"hanzala".center(7) --> ',"hanzala".center(7),'\n')
print('"hanzala".center(6,";") --> ',"hanzala".center(6,";"),'\n')
print('"hanzala".center(5,"$") --> ',"hanzala".center(5,"$"),'\n')
print('"hanzala".center(4) --> ',"hanzala".center(4),'\n')
print('"hanzala".center(3) --> ',"hanzala".center(3),'\n')
print('"hanzala".center(2) --> ',"hanzala".center(2),'\n')
print('"hanzala".center(1,"@") --> ',"hanzala".center(1,"@"),'\n')
print('"hanzala".center(0,"!") --> ',"hanzala".center(0,"!"),'\n')
print('"hanzala".center(-1,"$") --> ',"hanzala".center(-1,"$"),'\n')
print('"hanzala".center(-2) --> ',"hanzala".center(-2),'\n')
print('"hanzala".center(-5,"*") --> ',"hanzala".center(-5,"*"),'\n')
print('"hanzala".center(20,"*") --> ',"hanzala".center(20,"*"),'\n')
print('"hanzala".center(-20,"*") --> ',"hanzala".center(-20,"*"),'\n')
print(".........................................................................\n\n")

print('"".center(12,"⁴") --> ',"".center(12,"⁴"),'\n')
print('" ".center(12,"⁴") --> '," ".center(12,"⁴"),'\n')
print('"\\n".center(12,"⁴") --> ',"\n".center(12,"⁴"),'\n')
print('"[1,2,3,4,5]".center(20,"*") --> ',"[1,2,3,4,5]".center(20,"*"),'\n')
print('"1627.293".center(12,"z") --> ',"1627.293".center(12,"z"),'\n')
print('"hanzala".center(12,"⁴") --> ',"hanzala".center(12,"⁴"),'\n')
print('"hanzala".center(10,"₉") --> ',"hanzala".center(10,"₉"),'\n')
print('"hanzala".center(15,"ن") --> ',"hanzala".center(15,"ن"),'\n')
print('"hanzala".center(13,"غ") --> ',"hanzala".center(13,"غ"),'\n')
print('"hanzala".center(11,"प") --> ',"hanzala".center(11,"प"),'\n')
print('"hanzala".center(9,"ठ") --> ',"hanzala".center(9,"ठ"),'\n')
print(".........................................................................\n\n")
