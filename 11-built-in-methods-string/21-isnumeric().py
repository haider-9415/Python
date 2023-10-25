"""
   str.isnumeric() --> it returns True is all characters in str are numbers
   otherwise it returns False
   in other words, it returns True if and only if the str has non -ve integers
"""

s1 = '1'
print("s1.isnumeric() --> ",s1.isnumeric(),'\n')

s2 = '10000'
print("s2.isnumeric() --> ",s2.isnumeric(),'\n')

s3 = "928272"
print("s3.isnumeric() --> ",s3.isnumeric(),'\n')

s4 = '0'
print("s4.isnumeric() --> ",s4.isnumeric(),'\n')

s5 = '-39192i19'
print("s5.isnumeric() --> ",s5.isnumeric(),'\n')

s6 = "-192"
print("s6.isnumeric() --> ",s6.isnumeric(),'\n')

s7 = "abcdABCD1234"
print("s7.isnumeric() --> ",s7.isnumeric(),'\n')

s8 = "\n"
print("s8.isnumeric() --> ",s8.isnumeric(),'\n')

s9 = "" # in case of empty string, it also returns False
print("s9.isnumeric() --> ",s9.isnumeric(),'\n')

s10 = 'ABCDefgh'
print("s10.isnumeric() --> ",s10.isnumeric(),'\n')

s11 = '1234 5678'
print("s11.isnumeric() --> ",s11.isnumeric(),'\n') # due to space, it will give False 

s12 = '612&%54'
print("s12.isnumeric() --> ",s12.isnumeric(),'\n')

s13 = "@#$%^&*()"
print("s13.isnumeric() --> ",s13.isnumeric(),'\n')

s14 = "2819.21902"
print("s14.isnumeric() --> ",s14.isnumeric(),'\n')

s15 = "-2819.21902"
print("s15.isnumeric() --> ",s15.isnumeric(),'\n')


# in case of subscripts, it gives True
# for subscript --> "\_number" and press'tab'

print("₂.isnumeric() --> ",'₂'.isnumeric(),'\n')
print("2₂.isnumeric() --> ",'2₂'.isnumeric(),'\n')
print("₂123.isnumeric() --> ",'₂123'.isnumeric(),'\n')
print("1₂0.isnumeric() --> ",'1₂0'.isnumeric(),'\n')


# in case of superscripts, it gives True
# for superscript --> "\^number" and press'tab'
print("'²'.isnumeric() --> ",'²'.isnumeric(),'\n')
print("'2²'.isnumeric() --> ",'2²'.isnumeric(),'\n')
print("'²123'.isnumeric() --> ",'²123'.isnumeric(),'\n')
print("'1²0'.isnumeric() --> ",'1²0'.isnumeric(),'\n')


# in case of roman numerals, it gives True
print("'Ⅹ'.isnumeric() --> ",'Ⅹ'.isnumeric(),'\n')
print("'Ⅰ'.isnumeric() --> ",'Ⅰ'.isnumeric(),'\n')
print("'ⅠⅠ'.isnumeric() --> ",'ⅠⅠ'.isnumeric(),'\n')
print("'ⅠⅩ'.isnumeric() --> ",'ⅠⅩ'.isnumeric(),'\n')
print("'Ⅵ'.isnumeric() --> ",'Ⅵ'.isnumeric(),'\n')
print("'Ⅾ'.isnumeric() --> ",'Ⅾ'.isnumeric(),'\n')
print("'ⅥⅠⅠ'.isnumeric() --> ",'ⅥⅠⅠ'.isnumeric(),'\n')
print("'ⅮⅩ'.isnumeric() --> ",'ⅮⅩ'.isnumeric(),'\n')
print("'ⅻ'.isnumeric() --> ",'ⅻ'.isnumeric(),'\n')
print("'ⅽⅼ'.isnumeric() --> ",'ⅽⅼ'.isnumeric(),'\n')
print("'ⅿⅹ'.isnumeric() --> ",'ⅿⅹ'.isnumeric(),'\n')


# in case of fraction, it gives True if the fraction is made by using 'Fast Unicode Math Characters' extension
# for fraction x\y --> "\x/y" and then press "tab" 

# without using 'Fast Unicode Math Characters' extension
print("'1/2'.isnumeric() --> ",'1/2'.isnumeric(),'\n')
print("'2/3'.isnumeric() --> ",'2/3'.isnumeric(),'\n')

# using 'Fast Unicode Math Characters' extension
print("'½'.isnumeric() --> ",'½'.isnumeric(),'\n')
print("'⅔'.isnumeric() --> ",'⅔'.isnumeric(),'\n')


# without using (), it will not give run time error
print("1₂0.isnumeric --> ",'1₂0'.isnumeric,'\n')
print("'⅔'.isnumeric --> ",'⅔'.isnumeric,'\n')


# it can be used only with a tuple of one element that should be string
print("('123456').isnumeric() --> ",('123456').isnumeric(),'\n')

# # the following will give run time error
# print(['123456'].isnumeric())
# print(('123456',).isnumeric())
# print({'123456'}.isnumeric())
# print(['123','343'].isnumeric())
# print({'123','343'}.isnumeric())


# a number made by one or more digits having a unicode value is considered as a number
print("'①'.isnumeric() --> ","①".isnumeric(),'\n')
print("'②'.isnumeric() --> ","②".isnumeric(),'\n')
print("'⑤'.isnumeric() --> ","⑤".isnumeric(),'\n')
print("'⑤'.isnumeric() --> ","⑤".isnumeric(),'\n')
print("'④'.isnumeric() --> ","④".isnumeric(),'\n')
print("'⓫'.isnumeric() --> ","⓫".isnumeric(),'\n')
print("'⓬'.isnumeric() --> ","⓬".isnumeric(),'\n')
print("'⓯'.isnumeric() --> ","⓯".isnumeric(),'\n')
print("'⓰'.isnumeric() --> ","⓰".isnumeric(),'\n')
