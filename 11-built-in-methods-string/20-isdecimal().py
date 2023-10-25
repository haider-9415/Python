"""
   str.isdecimal() --> it returns True if all characters in str belong to decimal number
   otherwise it gives False
"""

s1 = '1'
print("s1.isdecimal() --> ",s1.isdecimal(),'\n')

s2 = '10000'
print("s2.isdecimal() --> ",s2.isdecimal(),'\n')

s3 = "928272"
print("s3.isdecimal() --> ",s3.isdecimal(),'\n')

s4 = '0'
print("s4.isdecimal() --> ",s4.isdecimal(),'\n')

s5 = '-39192i19'
print("s5.isdecimal() --> ",s5.isdecimal(),'\n')

s6 = "-192"
print("s6.isdecimal() --> ",s6.isdecimal(),'\n')

s7 = "abcdABCD1234"
print("s7.isdecimal() --> ",s7.isdecimal(),'\n')

s8 = "\n"
print("s8.isdecimal() --> ",s8.isdecimal(),'\n')

s9 = "" # in case of empty string, it also returns False
print("s9.isdecimal() --> ",s9.isdecimal(),'\n')

s10 = 'ABCDefgh'
print("s10.isdecimal() --> ",s10.isdecimal(),'\n')

s11 = '1234 5678'
print("s11.isdecimal() --> ",s11.isdecimal(),'\n') # due to space, it will give False 

s12 = '612&%54'
print("s12.isdecimal() --> ",s12.isdecimal(),'\n')

s13 = "@#$%^&*()"
print("s13.isdecimal() --> ",s13.isdecimal(),'\n')

s14 = "2819.21902"
print("s14.isdecimal() --> ",s14.isdecimal(),'\n')

s15 = "-2819.21902"
print("s15.isdecimal() --> ",s15.isdecimal(),'\n')


# in case of subscripts, it gives False
print("₂.isdecimal() --> ",'₂'.isdecimal(),'\n')
print("2₂.isdecimal() --> ",'2₂'.isdecimal(),'\n')
print("₂123.isdecimal() --> ",'₂123'.isdecimal(),'\n')
print("1₂0.isdecimal() --> ",'1₂0'.isdecimal(),'\n')


# in case of superscripts, it gives False
print("'²'.isdecimal() --> ",'²'.isdecimal(),'\n')
print("'2²'.isdecimal() --> ",'2²'.isdecimal(),'\n')
print("'²123'.isdecimal() --> ",'²123'.isdecimal(),'\n')
print("'1²0'.isdecimal() --> ",'1²0'.isdecimal(),'\n')


# in case of roman numerals, it gives False
print("'Ⅹ'.isdecimal() --> ",'Ⅹ'.isdecimal(),'\n')
print("'Ⅰ'.isdecimal() --> ",'Ⅰ'.isdecimal(),'\n')
print("'ⅠⅠ'.isdecimal() --> ",'ⅠⅠ'.isdecimal(),'\n')
print("'ⅠⅩ'.isdecimal() --> ",'ⅠⅩ'.isdecimal(),'\n')
print("'Ⅵ'.isdecimal() --> ",'Ⅵ'.isdecimal(),'\n')
print("'Ⅾ'.isdecimal() --> ",'Ⅾ'.isdecimal(),'\n')
print("'ⅥⅠⅠ'.isdecimal() --> ",'ⅥⅠⅠ'.isdecimal(),'\n')
print("'ⅮⅩ'.isdecimal() --> ",'ⅮⅩ'.isdecimal(),'\n')
print("'ⅻ'.isdecimal() --> ",'ⅻ'.isdecimal(),'\n')
print("'ⅽⅼ'.isdecimal() --> ",'ⅽⅼ'.isdecimal(),'\n')
print("'ⅿⅹ'.isdecimal() --> ",'ⅿⅹ'.isdecimal(),'\n')


# in case of fraction, it gives False
# without using 'Fast Unicode Math Characters' extension
print("'1/2'.isdecimal() --> ",'1/2'.isdecimal(),'\n')
print("'2/3'.isdecimal() --> ",'2/3'.isdecimal(),'\n')
# using 'Fast Unicode Math Characters' extension
print("'½'.isdecimal() --> ",'½'.isdecimal(),'\n')
print("'⅔'.isdecimal() --> ",'⅔'.isdecimal(),'\n')


# without using (), it will not give run time error
print("'12345'.isdecimal --> ",'12345'.isdecimal,'\n')
print("'⅔'.isdecimal --> ",'⅔'.isdecimal,'\n')


# it can be used only with a tuple of one element that should be string
print("('123456').isdecimal() --> ",('123456').isdecimal(),'\n')

# # the following will give run time error
# print(['123456'].isdecimal())
# print(('123456',).isdecimal())
# print({'123456'}.isdecimal())
# print(['123','343'].isdecimal())
# print({'123','343'}.isdecimal())


# a number made by one or more digits having a unicode value is not considered as a decimal number
print("'①'.isdecimal() --> ","①".isdecimal(),'\n')
print("'②'.isdecimal() --> ","②".isdecimal(),'\n')
print("'⑤'.isdecimal() --> ","⑤".isdecimal(),'\n')
print("'⑤'.isdecimal() --> ","⑤".isdecimal(),'\n')
print("'④'.isdecimal() --> ","④".isdecimal(),'\n')
print("'⓫'.isdecimal() --> ","⓫".isdecimal(),'\n')
print("'⓬'.isdecimal() --> ","⓬".isdecimal(),'\n')
print("'⓯'.isdecimal() --> ","⓯".isdecimal(),'\n')
print("'⓰'.isdecimal() --> ","⓰".isdecimal(),'\n')
