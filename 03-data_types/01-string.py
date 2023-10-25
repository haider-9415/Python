# type-6 --> string
srg1 = 'hanzala'
srg2 = "haider"
srg3 = """naeem""" # to make a multiline string, we use triple qoutes
srg4 = '';srg5 = "";srg6 = """""";srg7 = str() # these are empty strings
print("srg1  --> ",srg1)
print(srg1[0]);print(srg1[1]);print(srg1[2]);print(srg1[3]);print(srg1[4]);print(srg1[5]);print(srg1[6])

print("srg2  --> ",srg2)
print(srg2[0]);print(srg2[1]);print(srg2[2]);print(srg2[3]);print(srg2[4]);print(srg2[5])

print("srg3  --> ",srg3)
print(srg3[0]);print(srg3[1]);print(srg3[2]);print(srg3[3]);print(srg3[4])

print(type(srg1))
print(type(srg2))
print(type(srg2))

print(isinstance(srg1,str))
print(isinstance(srg2,str))
print(isinstance(srg2,str))


""" if we multiply a string by 'x',where x is integer then the data in 
    the string repeats 'x' times """

str = 'haider '
print("after 'str' mult. by 2")
print(str*2)
print("after 'str' mult. by 3")
print(str*3)
print("after 'str' mult. by 5")
print(str*5)


""" we can add two or more strings """
str1 = 'haider'
str2 = '98765 '
str3 = 'naeem'
print("str1+str3 -->",str1+str3)
print("str2+str1 -->",str2+str1)
print('str1+str3+str2 -->',str1+str3+str2)
print("str1+str2+str3 -->",str1+str2+str3)

# we can add two or more parts of different strings
print("str1[0]+str2[0]+str2[3]+str1[5] -->",str1[0]+str2[0]+str2[3]+str1[5])
print("str3[4]+str2[2]+str1[0]+str2[3] -->",str3[4]+str2[2]+str1[0]+str2[3])
print("str2[5]+str2[2]+str3[3]+str1[1] -->",str2[5]+str2[2]+str3[3]+str1[1]) # str[5] = ' '

# we can not add tow or more string with a string obtained by print(), because, print() returns in nonetype
# s = print("hanzala")
# print(s + ' naeem') # this will give runtime error
str4 = 'hanzala' + ' naeem'
print(str4) # this ois not give run time rror






""" we can compare two strings using operators --> <, >, ==, <= and >=
    but it compares them in 'lexicographical-order' ,i.e., dictionary-order """

s1 = 'aai'; s2 = 'aaowy'
print("s1 --> ",s1); print("s2 --> ",s2)
print("max(s2,s1) --> ",max(s2,s1)); """ max is a built in function to find string-1 is greater 
                   than string-2 or not ,i,e., string-1 is after string-2 or before it in dictionary-order.
                   In this, aaowy > aai ,because, 'o' comes after 'i' """


""" an empty string is equivalent to 0 or False """
if "": # if "" is equivalent to True then if-statement will  execute otherwise else-statement will execute
    print('you can see that "" is not eqivalent to False')
else:
    print('you can see that "" is eqivalent to False','\n')
if """""": # if """""" is equivalent to True then if-statement will  execute otherwise else-statement will execute
    print('you can see that """""" is not eqivalent to False')
else:
    print('you can see that """""" is eqivalent to False','\n')
if '': # if '' is equivalent to True then if-statement will  execute otherwise else-statement will execute
    print("you can see that '' is not eqivalent to False")
else:
    print("you can see that '' is eqivalent to False",'\n')
if '''''': # if '''''' is equivalent to True then if-statement will  execute otherwise else-statement will execute
    print("you can see that '''''' is not eqivalent to False")
else:
    print("you can see that '''''' is eqivalent to False",'\n')