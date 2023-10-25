"""
   str.isdigit() --> it returns True if each character in str is digit
   otherwise it returns False
"""


s1 = '1'
print("s1.isdigit() --> ",s1.isdigit(),'\n')

s2 = '10000'
print("s2.isdigit() --> ",s2.isdigit(),'\n')

s3 = "928272"
print("s3.isdigit() --> ",s3.isdigit(),'\n')

s4 = '0'
print("s4.isdigit() --> ",s4.isdigit(),'\n')

s5 = '-39192i19' # '-' is not digit
print("s5.isdigit() --> ",s5.isdigit(),'\n')

s6 = "-192"
print("s6.isdigit() --> ",s6.isdigit(),'\n')

s7 = "abcdABCD1234"
print("s7.isdigit() --> ",s7.isdigit(),'\n')

s8 = "\n"
print("s8.isdigit() --> ",s8.isdigit(),'\n')

s9 = "" # in case of empty string, it also returns False
print("s9.isdigit() --> ",s9.isdigit(),'\n')

s10 = 'ABCDefgh'
print("s10.isdigit() --> ",s10.isdigit(),'\n')

s11 = '1234 5678'
print("s11.isdigit() --> ",s11.isdigit(),'\n') # due to space, it will give False 

s12 = '612&%54'
print("s12.isdigit() --> ",s12.isdigit(),'\n')

s13 = "@#$%^&*()"
print("s13.isdigit() --> ",s13.isdigit(),'\n')

s14 = "2819.21902" # '.' is not digit
print("s14.isdigit() --> ",s14.isdigit(),'\n')

s15 = "-2819.21902"
print("s15.isdigit() --> ",s15.isdigit(),'\n')


# in case of subscripts, it gives True
print("₂.isdigit() --> ",'₂'.isdigit(),'\n')
print("2₂.isdigit() --> ",'2₂'.isdigit(),'\n')
print("₂123.isdigit() --> ",'₂123'.isdigit(),'\n')
print("1₂0.isdigit() --> ",'1₂0'.isdigit(),'\n')


# in case of superscripts, it gives True
print("'²'.isdigit() --> ",'²'.isdigit(),'\n')
print("'2²'.isdigit() --> ",'2²'.isdigit(),'\n')
print("'²123'.isdigit() --> ",'²123'.isdigit(),'\n')
print("'1²0'.isdigit() --> ",'1²0'.isdigit(),'\n')


# in case of roman numerals, it gives False , because thses are not considered as digits
print("'Ⅹ'.isdigit() --> ",'Ⅹ'.isdigit(),'\n')
print("'Ⅰ'.isdigit() --> ",'Ⅰ'.isdigit(),'\n')
print("'ⅠⅠ'.isdigit() --> ",'ⅠⅠ'.isdigit(),'\n')
print("'ⅠⅩ'.isdigit() --> ",'ⅠⅩ'.isdigit(),'\n')
print("'Ⅵ'.isdigit() --> ",'Ⅵ'.isdigit(),'\n')
print("'Ⅾ'.isdigit() --> ",'Ⅾ'.isdigit(),'\n')
print("'ⅥⅠⅠ'.isdigit() --> ",'ⅥⅠⅠ'.isdigit(),'\n')
print("'ⅮⅩ'.isdigit() --> ",'ⅮⅩ'.isdigit(),'\n')
print("'ⅻ'.isdigit() --> ",'ⅻ'.isdigit(),'\n')
print("'ⅽⅼ'.isdigit() --> ",'ⅽⅼ'.isdigit(),'\n')
print("'ⅿⅹ'.isdigit() --> ",'ⅿⅹ'.isdigit(),'\n')


# in case of fraction, it gives False, because, fraction is not a digit
# without using 'Fast Unicode Math Characters' extension
print("'1/2'.isdigit() --> ",'1/2'.isdigit(),'\n')
print("'2/3'.isdigit() --> ",'2/3'.isdigit(),'\n')
# using 'Fast Unicode Math Characters' extension
print("'½'.isdigit() --> ",'½'.isdigit(),'\n')
print("'⅔'.isdigit() --> ",'⅔'.isdigit(),'\n')


# without using (), it will not give run time error
print("'12345'.isdigit --> ",'12345'.isdigit,'\n')
print("'⅔'.isdigit --> ",'⅔'.isdigit,'\n')

# it can be used only with a tuple of one element that should be string
print("('123456').isdecimal() --> ",('123456').isdecimal(),'\n')

# # the following will give run time error
# print(['123456'].isdigit())
# print(('123456',).isdigit())
# print({'123456'}.isdigit())
# print(['123','343'].isdigit())
# print({'123','343'}.isdigit())


# a number made by one digit having a unicode value is considered as a digit
print("'①'.isdigit() --> ","①".isdigit(),'\n')
print("'②'.isdigit() --> ","②".isdigit(),'\n')
print("'⑤'.isdigit() --> ","⑤".isdigit(),'\n')
print("'⑤'.isdigit() --> ","⑤".isdigit(),'\n')
print("'④'.isdigit() --> ","④".isdigit(),'\n')


# a number made by two or more digits having a unicode value is not considered as a digit
print("'⓫'.isdigit() --> ","⓫".isdigit(),'\n')
print("'⓬'.isdigit() --> ","⓬".isdigit(),'\n')
print("'⓯'.isdigit() --> ","⓯".isdigit(),'\n')
print("'⓰'.isdigit() --> ","⓰".isdigit(),'\n')
