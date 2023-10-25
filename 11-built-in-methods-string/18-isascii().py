"""
   str.isascii() --> it returns True if all characters in str belong to ascii encoding scheme
   if there is only one character in str that does not belong to ascii encoding scheme
   so it returns boolean value
"""


s1 = 'a'
print("s1.isascii() --> ",s1.isascii(),'\n')

s2 = 'x'
print("s2.isascii() --> ",s2.isascii(),'\n')

s3 = "1"
print("s3.isascii() --> ",s3.isascii(),'\n')

s4 = '-3'
print("s4.isascii() --> ",s4.isascii(),'\n')

s5 = 'A'
print("s5.isascii() --> ",s5.isascii(),'\n')

s6 = " " # space is also an ascii character
print("s6.isascii() --> ",s6.isascii(),'\n')

s7 = "abcdABCD1234"
print("s7.isascii() --> ",s7.isascii(),'\n')

s8 = "\n"
print("s8.isascii() --> ",s8.isascii(),'\n')

s9 = "" # in case of empty string, it also returns True
print("s9.isascii() --> ",s9.isascii(),'\n')

s10 = 'ABCDefgh'
print("s10.isascii() --> ",s10.isascii(),'\n')

s11 = 'hanzala naeem'
print("s11.isascii() --> ",s11.isascii(),'\n') 

s12 = 'hanzalanaeem'
print("s12.isascii() --> ",s12.isascii(),'\n')

s13 = "@#$%^&*()"
print("s13.isascii() --> ",s13.isascii(),'\n')

# without using (), it will not give run time error
s14 = 'hanzala9415'
print("s14.isascii --> ",s14.isascii,'\n')


print("'Ɓ'.isascii() --> ",'Ɓ'.isascii(),'\n')
print("'Ƒ'.isascii() --> ",'Ƒ'.isascii(),'\n')
print("'Ɗ'.isascii() --> ",'Ɗ'.isascii(),'\n')
print("'Ʋ'.isascii() --> ",'Ʋ'.isascii(),'\n')
print("'Ƴ'.isascii() --> ",'Ƴ'.isascii(),'\n')
print("'Ɲ'.isascii() --> ",'Ɲ'.isascii(),'\n')
print("'ǒ'.isascii() --> ",'ǒ'.isascii(),'\n')
print("'ǟ'.isascii() --> ",'ǟ'.isascii(),'\n')
print("'Ǣ'.isascii() --> ",'Ǣ'.isascii(),'\n')
print("'Ǔ'.isascii() --> ",'Ǔ'.isascii(),'\n')
print("'ۆ'.isascii() --> ",'ۆ'.isascii(),'\n')
print("'ۃ'.isascii() --> ",'ۃ'.isascii(),'\n')
print("'ڲ'.isascii() --> ",'ڲ'.isascii(),'\n')
print("'ڱ'.isascii() --> ",'ڱ'.isascii(),'\n')
print("'ڹ'.isascii() --> ",'ڹ'.isascii(),'\n')
print("'ڡ'.isascii() --> ",'ڡ'.isascii(),'\n')
print("'∏'.isascii() --> ",'∏'.isascii(),'\n')
print("'∑'.isascii() --> ",'∑'.isascii(),'\n')
print("'∩'.isascii() --> ",'∩'.isascii(),'\n')
print("'Ꞷ'.isascii() --> ",'Ꞷ'.isascii(),'\n')
print("'ꝏ'.isascii() --> ",'ꝏ'.isascii(),'\n')
print("'ꞵ'.isascii() --> ",'ꞵ'.isascii(),'\n')
print("'ꞷ'.isascii() --> ",'ꞷ'.isascii(),'\n')


# it can be used only with a tuple of one element that should be string
print("('haider1hanzala1naeem').isascii() --> ",('haider1hanzala1naeem').isascii(),'\n')
print("('haiderhanzalanaeem').isascii() --> ",('haiderhanzalanaeem').isascii(),'\n')


# # the following will give run time error
# print(['haider1hanzala1naeem'].isascii())
# print(('haider1hanzala1naeem',).isascii())
# print({'haider1hanzala1naeem'}.isascii())
# print(['haider1','hanzala','1naeem'].isascii())
# print({'haider','1hanzala1','naeem'}.isascii())