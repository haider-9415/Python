"""
   str.isprintable() --> it returns True if all characters in str are printable
   otherwise it returns False
   printable characters --> characters that occupy printing space on the screen like letters, symbols, space, etc.
   non-printable characters --> characters that do not occupy printing space on the screen like \n, \t, etc.
"""

s1 = " This Is Hamid'    S Book "
print("s1.isprintable() --> ",s1.isprintable(),'\n')

s2 = " this is hamid'    s book "
print("s2.isprintable() --> ",s2.isprintable(),'\n')

s3 = " this     is lambda_finction"
print("s3.isprintable() --> ",s3.isprintable(),'\n')

s4 = " THIS     IS LAMBDA_FUNCTION"
print("s4.isprintable() --> ",s4.isprintable(),'\n')

s5 = "string-methods"
print("s5.isprintable() --> ",s5.isprintable(),'\n')

s6 = "string-Meth$$od"
print("s6.isprintable() --> ",s6.isprintable(),'\n')

s7 = "Xxxxxx@Gmail.Com"
print("s7.isprintable() --> ",s7.isprintable(),'\n')

s8 = "xxxxxx@gmail.com"
print("s8.isprintable() --> ",s8.isprintable(),'\n')

s9 = "127122$$#$jebfj"
print("s9.isprintable() --> ",s9.isprintable(),'\n')

s10 = "127122$$#$"
print("s10.isprintable() --> ",s10.isprintable(),'\n')

s11 = "          "
print("s11.isprintable() --> ",s11.isprintable(),'\n')

print("'My name is hanzala'.isprintable() --> ","My name is hanzala".isprintable(),'\n')


# without using (), it will not give run time error
print("'MY NAME IS HANZALA'.isprintable --> ","MY NAME IS HANZALA".isprintable,'\n')
print("'my name is hanzala'.isprintable --> ","my name is hanzala".isprintable,'\n')


# it can be used only with a tuple of one element that should be string
print("('haider').isprintable() --> ",("haider").isprintable(),'\n')

# # the following will give run time error
# print("{'haider'}.isprintable() --> ",{'haider'}.isprintable())
# print("['haider'].isprintable() --> ",['haider'].isprintable())
# print("('naeem','haider').isprintable() --> ",("naeem",'haider').isprintable())



print('"".isprintable() --> ',"".isprintable(),'\n')
print('" ".isprintable() --> '," ".isprintable(),'\n')
print('"   ".isprintable() --> ',"   ".isprintable(),'\n')
print('"62632abcd".isprintable() --> ',"62632abcd".isprintable(),'\n')
print('"62632ABCD".isprintable() --> ',"62632ABCD".isprintable(),'\n')
print('"".isprintable() --> ',"".isprintable(),'\n')
print('"  abcd".isprintable() --> ',"  abcd".isprintable(),'\n')
print('"  Abcd".isprintable() --> ',"  Abcd".isprintable(),'\n')
print('" ".isprintable() --> '," ".isprintable(),'\n')
print('"363-12J".isprintable() --> ',"363-12J".isprintable(),'\n')
print('"363+62j".isprintable() --> ',"363+62j".isprintable(),'\n')
print('"["a","b","c"]".isprintable() --> ','["a","b","c"]'.isprintable(),'\n')
print('"["A","B","C"]".isprintable() --> ','["A","B","C"]'.isprintable(),'\n')
print("'('A','B','C')'.isprintable() --> ","('A','B','C')".isprintable(),'\n')
print('"["A","B","c"]".islprintable) --> ','["A","B","c"]'.isprintable(),'\n')
print('"1425363".isprintable() --> ','1425363'.isprintable(),'\n')
print('"1425Z63".isprintable() --> ','1425Z63'.isprintable(),'\n')
print('"1425z63".isprintable() --> ','1425z63'.isprintable(),'\n')


# non printable characters
print("'\\n'.isprintable() --> ","\n".isprintable(),'\n')
print("'\\f'.isprintable() --> ","\f".isprintable(),'\n')
print("'\\t'.isprintable() --> ","\t".isprintable(),'\n')
print("'\\v'.isprintable() --> ","\v".isprintable(),'\n')
print("'\\r'.isprintable() --> ","\r".isprintable(),'\n')
print("'\\n\\r'.isprintable() --> ","\n\r".isprintable(),'\n')
print("'\\n\\r\\t\\v\\f'.isprintable() --> ","\n\r\t\v\f".isprintable(),'\n')


print("'naeem\\nhanzala'.isprintable() --> ","naeem\nhanzala".isprintable(),'\n')
print("'36363naeemhanzala\\r'.isprintable() --> ",'36363naeemhanzala\r'.isprintable(),'\n')
print("'\\fnaeemhanz#$$$ala%$##'.isprintable() --> ",'\fnaeemhanz#$$$ala%$##'.isprintable(),'\n')
print("'#@$$^^&&\\n1625337'.isprintable() --> ",'#@$$^^&&\n1625337'.isprintable(),'\n')
print("'    \\t        '.isprintable() --> ",'    \t        '.isprintable(),'\n')

s12 = """
"""
print("s12.isprintable() --> ",s12.isprintable(),'\n')

s13 = """hanzala
naeem"""
print("s13.isprintable() --> ",s13.isprintable(),'\n')

