""" str.split(separator,maxsplit) --> it breaks up the 'str' at the specified separator 
    it returns a list of the separated strings
    by default, the separator is 'space' and maxsplit is '-1' 
    using maxsplit, we can define that how many times the 'str' will be breaked  """
# remember if maxsplit is 'x' then the elements of the returned list = x+1


s1 = "hanzala naeem"
print("s1.split() --> ",s1.split(),'\n')
print("s1.split(' ') --> ",s1.split(' '),'\n')
print("s1.split('a') --> ",s1.split('a'),'\n')
print("s1.split('n') --> ",s1.split('n'),'\n')
print("s1.split('e') --> ",s1.split('e'),'\n')

s2 = "abcdabcdabcdaaadd"
print("s2.split('b') --> ",s2.split('b'),'\n')
print("s2.split('d') --> ",s2.split('d'),'\n')
print("s2.split('a') --> ",s2.split('a'),'\n')
print("s2.split('b',2) --> ",s2.split('b',2),'\n')
print("s2.split('d',3) --> ",s2.split('d',3),'\n')
print("s2.split('a',4) --> ",s2.split('a',4),'\n')

s3 = '1 2 3 4 5 6 7 8 9 10'
print("s3.split() --> ",s3.split(),'\n')
print("s3.split(' ',4) --> ",s3.split(' ',4),'\n')
print("s3.split(" ",7) --> ",s3.split(" ",7),'\n')


# remember separator can be string or None but maxsplit must be an integer
# if separator is None then it works as it works by default
s4 = 'a b d c d'
print("s4.split() --> ",s4.split(),'\n')
print("s4.split(None) --> ",s4.split(None),'\n')
print("s4.split() == s4.split(None) --> ",s4.split() == s4.split(None),'\n')
print("s4.split(None,3) --> ",s4.split(None,3),'\n')
print("s4.split(None,2) --> ",s4.split(None,2),'\n')


# we can use loop
print("using loop: ")
for i in "my name is hanzala naeem".split():
    print(i)
print("\n")


# without using (), it will not give run time error
s5 = 'h@nz@l@'.split
print("s1 --> ",s5,'\n')
print("'a#b#c#d#e'.rsplit --> ",'a#b#c#d#e'.split,'\n')


# it can be used only with a tuple of one element that should be string
print("('h$ai$de$r').split('$',2) --> ",('h$ai$de$r').split('$',2),'\n')
print("('rhRanRzaRlaR').split('R',3) --> ",('rhRanRzaRlaR').split('R',3),'\n')


# # the following will give run time error
# print(['h a i d e r'].split())
# print(['h' , 'a' , 'i', 'd','e' ,'r'].split())
# print(('h' , 'a', 'i', 'd','e' ,'r').split())
# print({'h a i d er '}.split())
# print({'h' , 'a' , 'i' ,'d' ,'e', 'r'}.split())


# consider the difference
s6 = "a  b  c  d  e  f  g  h"
print("s6.split() --> ",s6.split(),'\n')
print("s6.split(None) --> ",s6.split(None),'\n')
print("s6.split(' ') --> ",s6.split(' '),'\n')
print("s6.split('  ') --> ",s6.split('  '),'\n')


# in split(), sequence of separator matters
s7 = "@my#@name##@is@#haider#"
print("s7.split('@') --> ",s7.split('@'),'\n')
print("s7.split('#') --> ",s7.split('#'),'\n')
print("s7.split('#@') --> ",s7.split('#@'),'\n')
print("s7.split('@#') --> ",s7.split('@#'),'\n')


# it splits a string in 'x+1' strings, therefore, we can assigne 'x+1' variables for 'x+1' strings
s8 = "my name is hanzala naeem"
a,b,c,d,e = s8.split()
print("s8 --> ",s8)
print("a -> ",a);print("b -> ",b);print("c -> ",c);print("d -> ",d);print("e -> ",e,'\n')

s9 = "my#name#is#hanzala#naeem"
f,g,h = s9.split('#',2)
print("s9 --> ",s9)
print("f -> ",f);print("g -> ",g);print("h -> ",h,'\n')

full_name = input("Enter Your Name: ")
first_name,last_name = full_name.split()
print("\nfull_name --> ",full_name)
print("first_name --> ",first_name)
print("last_name --> ",last_name,'\n')


# it can split at \n
long_string = """ i am
learning computer
science"""
print("long_string.split() --> ",long_string.split(),'\n') # it will split at spaces
print("long_string.split(' ') --> ",long_string.split(' '),'\n') # it will split at spaces
print("long_string.split('\\n') --> ",long_string.split('\n'),'\n') # it will split at \n



