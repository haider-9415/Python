"""
   str.isalnum() --> it returns True if all characters in string str are alphanumeric(alphabets or numbers)
   if there is only one non-alphanumeric character in the string then it will return False
   so it returns boolean value
"""

s1 = 'abcdefgh'
print("s1.isalnum() --> ",s1.isalnum(),'\n')

s2 = 'abcdefgh93740'
print("s2.isalnum() --> ",s2.isalnum(),'\n')

s3 = 'AbCDefgH93740'
print("s3.isalnum() --> ",s3.isalnum(),'\n')

s4 = 'abcdef+gh93740'
print("s4.isalnum() --> ",s4.isalnum(),'\n')

s5 = 'ABCedfV$Gg$h937$40'
print("s5.isalnum() --> ",s5.isalnum(),'\n')

s6 = ""
print("s6.isalnum() --> ",s6.isalnum(),'\n')

s7 = ""
print("s7.isalnum() --> ",s7.isalnum(),'\n')

s8 = "\n"
print("s8.isalnum() --> ",s8.isalnum(),'\n')



# # use case of isalnum()
password = input("Enter Password(in alphanumeric): ")
while True:
    if password.isalnum(): # if password is alphanumeric then it gives true and the condition will be satisfied
        print("Successful. \n")
        break # on avoiding this statement, your loop is unstopable
    else: 
        print("Wrong Password")
        password = input("Enter New Password(in alphanumeric): ")



# without using (), it will not give run time error
s9 = 'hanzala9415'
print("s9.isalnum --> ",s9.isalnum,'\n')


s10 = 'hanzala naeem'
print("s10.isalnum() --> ",s10.isalnum(),'\n') # due to space, it gives false



print("'Ɓ'.isalnum() --> ",'Ɓ'.isalnum(),'\n')
print("'Ƒ'.isalnum() --> ",'Ƒ'.isalnum(),'\n')
print("'Ɗ'.isalnum() --> ",'Ɗ'.isalnum(),'\n')
print("'Ʋ'.isalnum() --> ",'Ʋ'.isalnum(),'\n')
print("'Ƴ'.isalnum() --> ",'Ƴ'.isalnum(),'\n')
print("'Ɲ'.isalnum() --> ",'Ɲ'.isalnum(),'\n')
print("'ǒ'.isalnum() --> ",'ǒ'.isalnum(),'\n')
print("'ǟ'.isalnum() --> ",'ǟ'.isalnum(),'\n')
print("'Ǣ'.isalnum() --> ",'Ǣ'.isalnum(),'\n')
print("'Ǔ'.isalnum() --> ",'Ǔ'.isalnum(),'\n')
print("'ۆ'.isalnum() --> ",'ۆ'.isalnum(),'\n')
print("'ۃ'.isalnum() --> ",'ۃ'.isalnum(),'\n')
print("'ڲ'.isalnum() --> ",'ڲ'.isalnum(),'\n')
print("'ڱ'.isalnum() --> ",'ڱ'.isalnum(),'\n')
print("'ڹ'.isalnum() --> ",'ڹ'.isalnum(),'\n')
print("'ڡ'.isalnum() --> ",'ڡ'.isalnum(),'\n')
print("'∏'.isalnum() --> ",'∏'.isalnum(),'\n')
print("'∑'.isalnum() --> ",'∑'.isalnum(),'\n')
print("'∩'.isalnum() --> ",'∩'.isalnum(),'\n')
print("'Ꞷ'.isalnum() --> ",'Ꞷ'.isalnum(),'\n')
print("'ꝏ'.isalnum() --> ",'ꝏ'.isalnum(),'\n')
print("'ꞵ'.isalnum() --> ",'ꞵ'.isalnum(),'\n')
print("'ꞷ'.isalnum() --> ",'ꞷ'.isalnum(),'\n')


# it can be used only with a tuple of one element that should be string
print("('haider1hanzala1naeem').isalnum() --> ",('haider1hanzala1naeem').isalnum(),'\n')

# # the following will give run time error
# print(['haider1hanzala1naeem'].isalnum())
# print(('haider1hanzala1naeem',).isalnum())
# print({'haider1hanzala1naeem'}.isalnum())
# print(['haider1','hanzala','1naeem'].isalnum())
# print({'haider','1hanzala1','naeem'}.isalnum())