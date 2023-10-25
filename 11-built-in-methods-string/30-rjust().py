"""
   str.rjust(width,fillchar) --> it pushes str to the right side at a given width 
   width --> it must be a +ve integer. To align the str of length 'n' to the right at width of 'x', width = 'x+n'
   fillchar --> to fill the empty bloks made after alignment. It must be a string, by default, it is space
   remember the fillchar must be the string of length one 
   because, width = 'x+n' , therefore, length occupyed by fillchar = 'width-n' = x 
""" 


s1 = "This Is Hamid'S Book "
print("s1 --> ",s1)
print("s1.rjust(3+len(s1)) --> ",s1.rjust(3+len(s1)),'\n')

s2 = "this is hamid's book "
print("s2 --> ",s2)
print("s2.rjust(5+len(s2),'$') --> ",s2.rjust(5+len(s2),'$'),'\n')

s3 = "this is lambda_finction"
print("s3 --> ",s3)
print("s3.rjust(10+len(s3),'*') --> ",s3.rjust(10+len(s3),'*'),'\n')

s4 = "THIS IS LAMBDA_FUNCTION"
print("s4 --> ",s4)
print("s4.rjust(3+len(s4),'\\') --> ",s4.rjust(3+len(s4),'\\'),'\n')

s5 = "string-methods"
print("s5 --> ",s5)
print("s5.rjust(15+len(s5),'@') --> ",s5.rjust(15+len(s5),'@'),'\n')

s6 = "string-methods"
print("s6 --> ",s6)
print("s6.rjust(15+len(s6),'r') --> ",s6.rjust(15+len(s6),'r'),'\n')

s7 = "string-methods"
print("s7 --> ",s7)
print("s7.rjust(15+len(s7),'3') --> ",s7.rjust(15+len(s7),'3'),'\n')

s8 = "string-methods"
print("s8 --> ",s8)
print("s8.rjust(15+len(s8),'Z') --> ",s8.rjust(15+len(s8),'Z'),'\n')

print("'My name is hanzala'.rjust(8+18,'!') --> ","My name is hanzala".rjust(8+18,'!'),'\n')
print(".........................................................................\n\n")


# without using (), it will not give run time error
print("'MYNAMEISHANZALA'.rjust --> ","MYNAMEISHANZALA".rjust,'\n')
print("'MY NAME IS HANZALA'.rjust --> ","MY NAME IS HANZALA".rjust,'\n')
print(".........................................................................\n\n")


# it can be used only with a tuple of one element that should be string
print("('haider').rjust(4+6,'%') --> ",("haider").rjust(4+6,'%'),'\n')
print("('123haider').rjust(4+9,'%') --> ",("123haider").rjust(13,'%'),'\n')

# # the following will give run time error
# print("{'haider'}.rjust(5+6,'+') --> ",{'haider'}.rjust(5+6,'+'))
# print("['haider'].rjust(5+6,'+') --> ",['haider'].rjust(5+6,'+'))
# print("('naeem','haider').rjust(4+2,',') --> ",("naeem",'haider').rjust(4+2,','))
print(".........................................................................\n\n")


# if we entered length of the string or less than it then it returns the whole string
print('"hanzala".rjust(7) --> ',"hanzala".rjust(7),'\n')
print('"hanzala".rjust(6,";") --> ',"hanzala".rjust(6,";"),'\n')
print('"hanzala".rjust(5,"$") --> ',"hanzala".rjust(5,"$"),'\n')
print('"hanzala".rjust(4) --> ',"hanzala".rjust(4),'\n')
print('"hanzala".rjust(3) --> ',"hanzala".rjust(3),'\n')
print('"hanzala".rjust(2) --> ',"hanzala".rjust(2),'\n')
print('"hanzala".rjust(1,"@") --> ',"hanzala".rjust(1,"@"),'\n')
print('"hanzala".rjust(0,"!") --> ',"hanzala".rjust(0,"!"),'\n')
print('"hanzala".rjust(-1,"$") --> ',"hanzala".rjust(-1,"$"),'\n')
print('"hanzala".rjust(-2) --> ',"hanzala".rjust(-2),'\n')
print('"hanzala".rjust(-5,"*") --> ',"hanzala".rjust(-5,"*"),'\n')
print('"hanzala".rjust(20,"*") --> ',"hanzala".rjust(20,"*"),'\n')
print('"hanzala".rjust(-20,"*") --> ',"hanzala".rjust(-20,"*"),'\n')
print(".........................................................................\n\n")

print('"".rjust(12,"⁴") --> ',"".rjust(12,"⁴"),'\n')
print('" ".rjust(12,"⁴") --> '," ".rjust(12,"⁴"),'\n')
print('"\\n".rjust(12,"⁴") --> ',"\n".rjust(12,"⁴"),'\n')
print('"[1,2,3,4,5]".rjust(20,"*") --> ',"[1,2,3,4,5]".rjust(20,"*"),'\n')
print('"1627.293".rjust(12,"z") --> ',"1627.293".rjust(12,"z"),'\n')
print('"hanzala".rjust(12,"⁴") --> ',"hanzala".rjust(12,"⁴"),'\n')
print('"hanzala".rjust(10,"₉") --> ',"hanzala".rjust(10,"₉"),'\n')
print('"hanzala".rjust(15,"ن") --> ',"hanzala".rjust(15,"ن"),'\n')
print('"hanzala".rjust(13,"غ") --> ',"hanzala".rjust(13,"غ"),'\n')
print('"hanzala".rjust(11,"प") --> ',"hanzala".rjust(11,"प"),'\n')
print('"hanzala".rjust(9,"ठ") --> ',"hanzala".rjust(9,"ठ"),'\n')
print(".........................................................................\n\n")

