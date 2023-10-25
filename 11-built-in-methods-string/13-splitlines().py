""" str.splitlines(keepends) --> it splits the string 'str' at line breaker 
    it returns a list of splitted strings 
    if keepends is 'true' or any integer except '0' then the line breaker also includes in the element of the list but 
    by default it is false and '0' stands for false
"""
# the line breakers --> \n, \r, \r\n, \v, \x0b, \f ,\x0c, \x1c, \x1d, \x1e, \x85, \u2028 or \u2029


s1 = """ I am a student.
I am learning computer science at magnet brains.
The respected teacher is Vardan Garg."""
print("s1.splitlines() --> ",s1.splitlines(),'\n')


s2 = " I am a student.\nI am learning computer science at magnet brains.\nThe respected teacher is Vardan Garg."
print("s2.splitlines() --> ",s2.splitlines(),'\n')

print("s1.splitlines() == s2.splitlines() --> ",s1.splitlines() == s2.splitlines(),'\n')


# without using (), it will not give run time error
s3 = " I am a student.\nI am learning computer science at magnet brains.\nThe respected teacher is Vardan Garg."
print("s3.splitlines --> ",s3.splitlines,'\n')


# it can be used only with a tuple of one element that should be string
print("('haider\\nhanzala\\nnaeem\\n    ').splitlines() --> ",('haider\nhanzala\nnaeem\n    ').splitlines(),'\n')

# # the following will give run time error
# print(['haider\\nhanzala\\nnaeem\\n    '].splitlines())
# print(['haider\\nhanzala\\nnaeem\\n    '].splitlines())
# print(('haider\\nhanzala\\nnaeem\\n    ',).splitlines())
# print({'haider\\nhanzala\\nnaeem\\n    '}.splitlines())
# print({'haider\\nhanzala\\nnaeem\\n    '}.splitlines())


# if it splits a string in a list of 'n' string elements then we can assigne 'n' variables for 'n' strings
s4 = "my\nname\nis\nhanzala\nnaeem"
a,b,c,d,e = s4.splitlines()
print("s4 --> my\\nname\\nis\\nhanzala\\nnaeem")
print("a -> ",a);print("b -> ",b);print("c -> ",c);print("d -> ",d);print("e -> ",e,'\n')

s5 = "my\nname\nis\nhanzala\nnaeem"
f,g,h,i,j = s5.splitlines()
print("s5 --> my\\nname\\nis\\nhanzala\\nnaeem")
print("f -> ",f);print("g -> ",g);print("h -> ",h);print("i -> ",i);print("j -> ",j,'\n')


# using \r
s6 = "magnet\rbarins\reducation\rplatform"
print("s6.splitlines() --> ",s6.splitlines(),'\n')


# using \r\n
s7 = "magnet\r\nbarins\r\neducation\r\nplatform"
print("s7.splitlines() --> ",s7.splitlines(),'\n')


# using \v
s8 = "magnet\vbarins\veducation\vplatform"
print("s8.splitlines() --> ",s8.splitlines(),'\n')


# using \x0b
s9 = "magnet\x0bbarins\x0beducation\x0bplatform"
print("s9.splitlines() --> ",s9.splitlines(),'\n')


# using \f
s10 = "magnet\fbarins\feducation\fplatform"
print("s10.splitlines() --> ",s10.splitlines(),'\n')


# using \x0c
s11 = "magnet\x0cbarins\x0ceducation\x0cplatform"
print("s11.splitlines() --> ",s11.splitlines(),'\n')


# using \x1c
s12 = "magnet\x1cbarins\x1ceducation\x1cplatform"
print("s12.splitlines() --> ",s12.splitlines(),'\n')


# using \x1d
s13 = "magnet\x1dbarins\x1deducation\x1dplatform"
print("s13.splitlines() --> ",s13.splitlines(),'\n')


# using \x1e
s14 = "magnet\x1ebarins\x1eeducation\x1eplatform"
print("s14.splitlines() --> ",s14.splitlines(),'\n')


# using \x85
s15 = "magnet\x85barins\x85education\x85platform"
print("s15.splitlines() --> ",s15.splitlines(),'\n')


# using \u2028
s16 = "magnet\u2028barins\u2028education\u2028platform"
print("s16.splitlines() --> ",s16.splitlines(),'\n')


# using \u2029
s17 = "magnet\u2029barins\u2029education\u2029platform"
print("s17.splitlines() --> ",s17.splitlines(),'\n')


# we can use them in a asingle string
s18 = "hanzala\nnaeem\rhaider\fmagnet\x0cbrains\u2029education\x85platform"
print("s18.splitlines() --> ",s18.splitlines(),'\n')


# using True or integer except 0
s19 = "hanzala\nnaeem\rhaider\fmagnet\x0cbrains\u2029education\x85platform"
print("s19.splitlines(True) --> ",s19.splitlines(True),'\n')

s20 = "my\nname\nis\nhanzala\nnaeem"
print("s20.splitlines(97) --> ",s20.splitlines(97),'\n')

s21 = "my\nname\nis\nhanzala\nnaeem"
print("s21.splitlines(-28129) --> ",s21.splitlines(-28129),'\n')

s22 = """ I am a student.
I am learning computer science at magnet brains.
The respected teacher is Vardan Garg.
"""
print("s22.splitlines(True) --> ",s22.splitlines(True),'\n')


# using False or 0
s23 = "my\nname\nis\nhanzala\nnaeem"
print("s23.splitlines(0) --> ",s23.splitlines(0),'\n')

s24 = "my\nname\nis\nhanzala\nnaeem"
print("s24.splitlines(False) --> ",s24.splitlines(False),'\n')



