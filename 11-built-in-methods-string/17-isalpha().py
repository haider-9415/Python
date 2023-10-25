"""
   str.isalpha() --> it returns True if all characters in str are alphabets
   if there is a character is not an alphabet then it returns Flase
   so it returns boolean value
"""

s1 = 'abcdefgh'
print("s1.isalpha() --> ",s1.isalpha(),'\n')

s2 = 'abcdef3gh'
print("s2.isalpha() --> ",s2.isalpha(),'\n')

s3 = 'AbCDefgH@'
print("s3.isalpha() --> ",s3.isalpha(),'\n')

s4 = 'abcdef+gh93740'
print("s4.isalpha() --> ",s4.isalpha(),'\n')

s5 = 'ABCedfV$Gg$h937$40'
print("s5.isalpha() --> ",s5.isalpha(),'\n')

s6 = ""
print("s6.isalpha() --> ",s6.isalpha(),'\n')

s7 = " "
print("s7.isalpha() --> ",s7.isalpha(),'\n')

s8 = "\n"
print("s8.isalpha() --> ",s8.isalpha(),'\n')

s9 = 'ABCDEFGH'
print("s9.isalpha() --> ",s9.isalpha(),'\n')

s10 = 'ABCDefgh'
print("s10.isalpha() --> ",s10.isalpha(),'\n')

s11 = 'hanzala naeem'
print("s11.isalpha() --> ",s11.isalpha(),'\n') # due to space, it gives false

s12 = 'hanzalanaeem'
print("s12.isalpha() --> ",s12.isalpha(),'\n')


# # use case of isalpha()
# password = input("Enter Password(only alphabets): ")
# while True:
#     if password.isalpha(): # if password is alphanumeric then it gives true and the condition will be satisfied
#         print("Successful. \n")
#         break # on avoiding this statement, your loop is unstopable
#     else: 
#         print("Wrong Password")
#         password = input("Enter New Password(only alphabets): ")



# without using (), it will not give run time error
s13 = 'hanzala9415'
print("s13.isalpha --> ",s13.isalpha,'\n')


print("'Ɓ'.isalpha() --> ",'Ɓ'.isalpha(),'\n')
print("'Ƒ'.isalpha() --> ",'Ƒ'.isalpha(),'\n')
print("'Ɗ'.isalpha() --> ",'Ɗ'.isalpha(),'\n')
print("'Ʋ'.isalpha() --> ",'Ʋ'.isalpha(),'\n')
print("'Ƴ'.isalpha() --> ",'Ƴ'.isalpha(),'\n')
print("'Ɲ'.isalpha() --> ",'Ɲ'.isalpha(),'\n')
print("'ǒ'.isalpha() --> ",'ǒ'.isalpha(),'\n')
print("'ǟ'.isalpha() --> ",'ǟ'.isalpha(),'\n')
print("'Ǣ'.isalpha() --> ",'Ǣ'.isalpha(),'\n')
print("'Ǔ'.isalpha() --> ",'Ǔ'.isalpha(),'\n')
print("'ۆ'.isalpha() --> ",'ۆ'.isalpha(),'\n')
print("'ۃ'.isalpha() --> ",'ۃ'.isalpha(),'\n')
print("'ڲ'.isalpha() --> ",'ڲ'.isalpha(),'\n')
print("'ڱ'.isalpha() --> ",'ڱ'.isalpha(),'\n')
print("'ڹ'.isalpha() --> ",'ڹ'.isalpha(),'\n')
print("'ڡ'.isalpha() --> ",'ڡ'.isalpha(),'\n')
print("'∏'.isalpha() --> ",'∏'.isalpha(),'\n')
print("'∑'.isalpha() --> ",'∑'.isalpha(),'\n')
print("'∩'.isalpha() --> ",'∩'.isalpha(),'\n')
print("'Ꞷ'.isalpha() --> ",'Ꞷ'.isalpha(),'\n')
print("'ꝏ'.isalpha() --> ",'ꝏ'.isalpha(),'\n')
print("'ꞵ'.isalpha() --> ",'ꞵ'.isalpha(),'\n')
print("'ꞷ'.isalpha() --> ",'ꞷ'.isalpha(),'\n')


# it can be used only with a tuple of one element that should be string
print("('haider1hanzala1naeem').isalpha() --> ",('haider1hanzala1naeem').isalpha(),'\n')
print("('haiderhanzalanaeem').isalpha() --> ",('haiderhanzalanaeem').isalpha(),'\n')

# # the following will give run time error
# print(['haider1hanzala1naeem'].isalpha())
# print(('haider1hanzala1naeem',).isalpha())
# print({'haider1hanzala1naeem'}.isalpha())
# print(['haider1','hanzala','1naeem'].isalpha())
# print({'haider','1hanzala1','naeem'}.isalpha())