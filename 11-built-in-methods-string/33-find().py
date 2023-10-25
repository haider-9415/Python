"""
   str.find(substring,start,end) --> it returns the index of the substring if it is a single character and if the 
   substring is a string then it returns the index of the first letter of the subsring
   a string then it returns the index of first letter of the 
   using start & end parameters, we can find a substring in the specific region
   if substring is not in str then it returns -1
"""

s1 = "hanzala"
print("s1.find('a') --> ",s1.find('a'),'\n')
s2 = "123123123"
print("s2.find('1') --> ",s2.find('1'),'\n')
s3 = "abcd@1234#ef@dh#"
print("s3.find('#') --> ",s3.find('#'),'\n')
s4 = "hanzala naeem 9415 860"
print("s4.find(' ') --> ",s4.find(' '),'\n')
s5 = "hanzala"
print("s5.find('m') --> ",s5.find('m'),'\n')
s6 = "hanzala"
print("s6.find('2') --> ",s6.find('2'),'\n')
s7 = "hanzala"
print("s7.find('%') --> ",s7.find('%'),'\n')
s8 = "my name is hanzala naeem"
print("s8.find('hanzala') --> ",s8.find('hanzala'),'\n')
s9 = "i am a student of class 12th"
print("s9.find('class') --> ",s9.find('class'),'\n')
s10 = "hanzala"
print("s10.find('zala') --> ",s10.find('zala'),'\n')
print(".........................................................................\n\n")


# without using (), it will not give run time error
print("'102030405060708090'.find --> ","102030405060708090".find,'\n')
print("'MY NAME IS HANZALA'.find --> ","MY NAME IS HANZALA".find,'\n')
print(".........................................................................\n\n")



# it can be used only with a tuple of one element that should be string
print("('iamhaider').find('i') --> ",("ianhaider").find('i'),'\n')
print("('123haid3er').find('3') --> ",("123haid3er").find('3'),'\n')

# # the following will give run time error
# print("{'haider'}.find(5+6) --> ",{'haider'}.find(5+6))
# print("['haider'].find(5+6) --> ",['haider'].find(5+6))
# print("('naeem','haider').find(4+2) --> ",("naeem",'haider').find(4+2))
print(".........................................................................\n\n")



print("''.find('') --> ","".find(''),'\n')
print("'abcdefaghijak123456789'.find('') --> ","abcdefaghijak123456789".find(''),'\n')
print("'abcdefaghijak123456789'.find(' ') --> ","abcdefaghijak123456789".find(' '),'\n')
print("'abcdefaghijak1 23  456789'.find(' ') --> ","abcdefaghijak1 23  456789".find(' '),'\n')
print("'abcdefaghijak123456789'.find('a',1) --> ","abcdefaghijak123456789".find('a',1),'\n') # after index 1, first occurence of 'a' is at index 6
print("'abcdefaghijak123456789'.find('a',5) --> ","abcdefaghijak123456789".find('a',5),'\n') # after index 5, first occurence of 'a' is at index 6
print("'abcdefaghijak123456789'.find('a',10) --> ","abcdefaghijak123456789".find('a',10),'\n') # after index 10, first occurence of 'a' is at index 11
print("'abcdefaghijak123456789'.find('a',12) --> ","abcdefaghijak123456789".find('a',12),'\n') # after index 12, there is no 'a'
print("'abcdefaghijak123456789'.find('a',4,10) --> ","abcdefaghijak123456789".find('a',4,10),'\n') # in range 4 to 10, fisrt 'a' is at index 6 
print("'abcdefabcdghijbcdak123456789'.find('bcd',4,10) --> ","abcdefabcdghijbcdak123456789".find('bcd',4,10),'\n')

# end parameter exludes
print("'my name is hanzala'.find('a',6,12) --> ","my name is hanzala".find('a',6,12),'\n') # there is no 'a' in range 6 to 9
# start parameter includes
print("'my name is hanzala'.find('a',12,20) --> ","my name is hanzala".find('a',12,20),'\n')



# we can use -ve indexnig
print("'my name is hanzala'.find('a',-9,-3) --> ","my name is hanzala".find('a',-9,-3),'\n') # in range -9 to -3, first 'a' is at 12
print("'my name is hanzala'.find('a',-5,-3) --> ","my name is hanzala".find('a',-5,-3),'\n') # there is no 'a' in range -5 to -3
print("'my name is hanzala'.find('n',-40,-3) --> ","my name is hanzala".find('n',-40,-3),'\n') # in range -40 to -3, first 'n' is at 3
print("'my name is hanzala'.find('n',-10,-1) --> ","my name is hanzala".find('n',-10,-1),'\n') # in range -10 to -1, first 'n' is at 13
