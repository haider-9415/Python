""" str.rsplit(separator,maxsplit) --> it works as split() works but it breaks the string from right side
    and split() breaks the string from left side """


s1 = "hanzala naeem"
print("s1.rsplit() --> ",s1.rsplit(),'\n')
print("s1.rsplit(' ') --> ",s1.rsplit(' '),'\n')
print("s1.rsplit('a') --> ",s1.rsplit('a'),'\n')
print("s1.rsplit('n') --> ",s1.rsplit('n'),'\n')
print("s1.rsplit('e') --> ",s1.rsplit('e'),'\n')

s2 = "abcdabcdabcdaaadd"
print("s2.rsplit('b') --> ",s2.rsplit('b'),'\n')
print("s2.rsplit('d') --> ",s2.rsplit('d'),'\n')
print("s2.rsplit('a') --> ",s2.rsplit('a'),'\n')
print("s2.rsplit('b',2) --> ",s2.rsplit('b',2),'\n')
print("s2.rsplit('d',3) --> ",s2.rsplit('d',3),'\n')
print("s2.rsplit('a',4) --> ",s2.rsplit('a',4),'\n')

s3 = '1 2 3 4 5 6 7 8 9 10'
print("s3.rsplit() --> ",s3.rsplit(),'\n')
print("s3.rsplit(' ',4) --> ",s3.rsplit(' ',4),'\n')
print("s3.rsplit(" ",7) --> ",s3.rsplit(" ",7),'\n')


# remember separator can be string or None but maxsplit must be an integer
# if separator is None then it works as it works by default
s4 = 'a b d c d'
print("s4.rsplit() --> ",s4.rsplit(),'\n')
print("s4.rsplit(None) --> ",s4.rsplit(None),'\n')
print("s4.rsplit() == s4.rsplit(None) --> ",s4.rsplit() == s4.rsplit(None),'\n')
print("s4.rsplit(None,3) --> ",s4.rsplit(None,3),'\n')
print("s4.rsplit(None,2) --> ",s4.rsplit(None,2),'\n')


# we can use loop
print("using loop: ")
for i in "my name is hanzala naeem".rsplit():
    print(i)
print("\n")


# without using (), it will not give run time error
s5 = 'h@nz@l@'.rsplit
print("s1 --> ",s5,'\n')
print("'a#b#c#d#e'.rsplit --> ",'a#b#c#d#e'.rsplit,'\n')


# it can be used only with a tuple of one element that should be string
print("('h$ai$de$r').rsplit('$',2) --> ",('h$ai$de$r').rsplit('$',2),'\n')
print("('rhRanRzaRlaR').rsplit('R',3) --> ",('rhRanRzaRlaR').rsplit('R',3),'\n')

# # the following will give run time error
# print(['h a i d e r'].rsplit())
# print(['h' , 'a' , 'i', 'd','e' ,'r'].rsplit())
# print(('h' , 'a', 'i', 'd','e' ,'r').rsplit())
# print({'h a i d er '}.rsplit())
# print({'h' , 'a' , 'i' ,'d' ,'e', 'r'}.rsplit())


# consider the difference
s6 = "a  b  c  d  e  f  g  h"
print("s6.rsplit() --> ",s6.rsplit(),'\n')
print("s6.rsplit(None) --> ",s6.rsplit(None),'\n')
print("s6.rsplit(' ') --> ",s6.rsplit(' '),'\n')
print("s6.rsplit('  ') --> ",s6.rsplit('  '),'\n')


# in rsplit(), sequence of separator matters
s7 = "@my#@name##@is@#haider#"
print("s7.rsplit('@') --> ",s7.rsplit('@'),'\n')
print("s7.rsplit('#') --> ",s7.rsplit('#'),'\n')
print("s7.rsplit('#@') --> ",s7.rsplit('#@'),'\n')
print("s7.rsplit('@#') --> ",s7.rsplit('@#'),'\n')


# it splits a string in 'x+1' strings, therefore, we can assigne 'x+1' variables for 'x+1' strings
s8 = "my name is hanzala naeem"
a,b,c,d,e = s8.rsplit()
print("s8 --> ",s8)
print("a -> ",a);print("b -> ",b);print("c -> ",c);print("d -> ",d);print("e -> ",e,'\n')

s9 = "my#name#is#hanzala#naeem"
f,g,h = s9.rsplit('#',2)
print("s9 --> ",s9)
print("f -> ",f);print("g -> ",g);print("h -> ",h,'\n')

full_name = input("Enter Your Name: ")
first_name,last_name = full_name.rsplit()
print("\nfull_name --> ",full_name)
print("first_name --> ",first_name)
print("last_name --> ",last_name,'\n')


# it can split at \n
long_string = """ i am
learning computer
science"""
print("long_string.rsplit() --> ",long_string.rsplit(),'\n') # it will split at spaces
print("long_string.rsplit(' ') --> ",long_string.rsplit(' '),'\n') # it will split at spaces
print("long_string.rsplit('\\n') --> ",long_string.rsplit('\n'),'\n') # it will split at \n
