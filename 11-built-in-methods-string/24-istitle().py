"""
   str.istitle() --> it returns True if the str is in title case
   otherwise it returns False
"""

s1 = " This Is Hamid'    S Book "
print("s1.istitle() --> ",s1.istitle(),'\n')

s2 = " this is   hamid'  s book "
print("s2.istitle() --> ",s2.istitle(),'\n')

s3 = " This     Is Lambda_Finction"
print("s3.istitle() --> ",s3.istitle(),'\n')

s4 = " this is lambda_finction"
print("s4.istitle() --> ",s4.istitle(),'\n')

s5 = "String-Methods"
print("s5.istitle() --> ",s5.istitle(),'\n')

s6 = "string-methods"
print("s6.istitle() --> ",s6.istitle(),'\n')


s7 = "Xxxxxx@Gmail.Com"
print("s7.istitle() --> ",s7.istitle(),'\n')

s8 = "xxxxxx@gmail.com"
print("s8.istitle() --> ",s8.istitle(),'\n')

print("('my name is hanzala'.title()).istitle() --> ",("my name is hanzala".title()).istitle(),'\n')

print("'my name is hanzala'.istitle() --> ","my name is hanzala".istitle(),'\n')


# without using (), it will not give run time error
print("'My Name Is Hanzala'.istitle --> ","My Name Is Hanzala".istitle,'\n')
print("'my name is hanzala'.istitle --> ","my name is hanzala".istitle,'\n')


# it can be used only with a tuple of one element that should be string
print("('Hanzala  Naeem').istitle() --> ",("Hanzala  Naeem").istitle(),'\n')

# # the following will give run time error
# print("{'Hanzala Naeem'}.istitle() --> ",{'Hanzala Naeem'}.istitle())
# print("['Hanzala Naeem'].istitle() --> ",['Hanzala Naeem'].istitle())
# print("('Naeem','Haider').istitle() --> ",("Naeem",'Haider').istitle())


print('"62632Abcd".istitle() --> ',"62632Abcd".istitle(),'\n')
print('"".istitle() --> ',"".istitle(),'\n')
print('"  abcd".istitle() --> ',"  abcd".istitle(),'\n')
print('" ".istitle() --> '," ".istitle(),'\n')
print('"  Abcd".istitle() --> ',"  Abcd".istitle(),'\n')
print('"363-12J".istitle() --> ',"363-12J".istitle(),'\n')
print('"363+62j".istitle() --> ',"363+62j".istitle(),'\n')
print('"["a","b","c"]".istitle() --> ','["a","b","c"]'.istitle(),'\n')
print('"["A","B","C"]".istitle() --> ','["A","B","C"]'.istitle(),'\n')
print("'('A','B','C')' --> ","('A','B','C')".istitle(),'\n')
print('"["A","B","c"]".istitle() --> ','["A","B","c"]'.istitle(),'\n')
print('"1425363".istitle() --> ','1425363'.istitle(),'\n')

