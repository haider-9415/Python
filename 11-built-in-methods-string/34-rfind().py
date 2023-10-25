"""
   str.rrfind() --> it works as rfind() works but it starts searching from right and rfind() starts searching from left
"""

s1 = "hanzala"
print("s1.rfind('a') --> ",s1.rfind('a'),'\n')
s2 = "123123123"
print("s2.rfind('1') --> ",s2.rfind('1'),'\n')
s3 = "abcd@1234#ef@dh#"
print("s3.rfind('#') --> ",s3.rfind('#'),'\n')
s4 = "hanzala naeem 9415 860"
print("s4.rfind(' ') --> ",s4.rfind(' '),'\n')
s5 = "hanzala"
print("s5.rfind('m') --> ",s5.rfind('m'),'\n')
s6 = "hanzala"
print("s6.rfind('2') --> ",s6.rfind('2'),'\n')
s7 = "hanzala"
print("s7.rfind('%') --> ",s7.rfind('%'),'\n')
s8 = "my name is hanzala naeem"
print("s8.rfind('hanzala') --> ",s8.rfind('hanzala'),'\n')
s9 = "i am a student of class 12th"
print("s9.rfind('class') --> ",s9.rfind('class'),'\n')
s10 = "hanzala"
print("s10.rfind('zala') --> ",s10.rfind('zala'),'\n')
print(".........................................................................\n\n")


# without using (), it will not give run time error
print("'102030405060708090'.rfind --> ","102030405060708090".rfind,'\n')
print("'MY NAME IS HANZALA'.rfind --> ","MY NAME IS HANZALA".rfind,'\n')
print(".........................................................................\n\n")



# it can be used only with a tuple of one element that should be string
print("('iamhaider').rfind('i') --> ",("ianhaider").rfind('i'),'\n')
print("('123haid3er').rfind('3') --> ",("123haid3er").rfind('3'),'\n')

# # the following will give run time error
# print("{'haider'}.rfind(5+6) --> ",{'haider'}.rfind(5+6))
# print("['haider'].rfind(5+6) --> ",['haider'].rfind(5+6))
# print("('naeem','haider').rfind(4+2) --> ",("naeem",'haider').rfind(4+2))
print(".........................................................................\n\n")



print("''.rfind('') --> ","".rfind(''),'\n')
# on searching empty string, it returns index 'x+1' if the last index in the string str is 'x'
print("'abcdefaghijak123456789'.rfind('') --> ","abcdefaghijak123456789".rfind(''),'\n')
print("'abcdefaghijak123456789'.rfind(' ') --> ","abcdefaghijak123456789".rfind(' '),'\n')
print("'abcdefaghijak1 23  456789'.rfind(' ') --> ","abcdefaghijak1 23  456789".rfind(' '),'\n')
print("'abcdefaghijak123456789'.rfind('a',1) --> ","abcdefaghijak123456789".rfind('a',1),'\n') # after index 1, first occurence of 'a' is at index 6
print("'abcdefaghijak123456789'.rfind('a',5) --> ","abcdefaghijak123456789".rfind('a',5),'\n') # after index 5, first occurence of 'a' is at index 6
print("'abcdefaghijak123456789'.rfind('a',10) --> ","abcdefaghijak123456789".rfind('a',10),'\n') # after index 10, first occurence of 'a' is at index 11
print("'abcdefaghijak123456789'.rfind('a',12) --> ","abcdefaghijak123456789".rfind('a',12),'\n') # after index 12, there is no 'a'
print("'abcdefaghijak123456789'.rfind('a',4,10) --> ","abcdefaghijak123456789".rfind('a',4,10),'\n') # in range 4 to 10, fisrt 'a' is at index 6 
print("'abcdefabcdghijbcdak123456789'.rfind('bcd',4,10) --> ","abcdefabcdghijbcdak123456789".rfind('bcd',4,10),'\n')

# end parameter exludes
print("'my name is hanzala'.rfind('a',6,12) --> ","my name is hanzala".rfind('a',6,12),'\n') # there is no 'a' in range 6 to 9
# start parameter includes
print("'my name is hanzala'.rfind('a',12,20) --> ","my name is hanzala".rfind('a',12,20),'\n')



# we can use -ve indexnig
print("'my name is hanzala'.rfind('a',-9,-3) --> ","my name is hanzala".rfind('a',-9,-3),'\n') # in range -9 to -3, first 'a' is at 12
print("'my name is hanzala'.rfind('a',-5,-3) --> ","my name is hanzala".rfind('a',-5,-3),'\n') # there is no 'a' in range -5 to -3
print("'my name is hanzala'.rfind('n',-40,-3) --> ","my name is hanzala".rfind('n',-40,-3),'\n') # in range -40 to -3, first 'n' is at 3
print("'my name is hanzala'.rfind('n',-10,-1) --> ","my name is hanzala".rfind('n',-10,-1),'\n') # in range -10 to -1, first 'n' is at 13
