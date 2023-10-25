""" 
str.partition(separator) --> it separates a string 'str' at the separator
it returns a tuple containing three elements 1)part-before-separator 2)separator 3)part-after-separator
it starts spliting from left side
it separates at the first occurence of the separator from left
if the separator is not in str then the tuple will have the str and two empty strings 
"""


s1 = "hanzalaxxxxxxx420@gmail.com"
print("s1.partition('@') --> ",s1.partition('@'),'\n')

s2 = "hanzala naeem"
print("s2.partition(' ') --> ",s2.partition(' '),'\n')

s3 = "hanzalanaeem"
print("s3.partition(' ') --> ",s3.partition(' '),'\n')

s4 = "hanzalaxxxxxxx420gmail.com"
print("s4.partition('@') --> ",s4.partition('@'),'\n')

s5 = "hanzala"
print("s5.partition('a') --> ",s5.partition('a'),'\n')

s6 = "abcd1abcd1abcd1"
print("s6.partition('1') --> ",s6.partition('1'),'\n')


# without using (), it will not give run time error
s7 = "hanzala"
print("s7.partition --> ",s7.partition,'\n')


# it can be used only with a tuple of one element that should be string
print("('haider hanzala naeem').partition('e') --> ",('haider hanzala naeem').partition("n"),'\n')

# # the following will give run time error
# print(['haider hanzala naeem'].partition("n"))
# print(['haider hanzala naeem'].partition("n"))
# print(('haider hanzala naeem',).partition("n"))
# print({'haider hanzala naeem'}.partition("n"))
# print({'haider hanzala naeem'}.partition("n"))


# it splits a string in three parts, so, we can assign those three parts in three variables
s8 = "abcd1abcd1abcd1"
print("s8.partition('1') --> ",s8.partition('1'))
before_sep,sep,after_sep = s8.partition('1')
print("before_sep --> ",before_sep);print("sep --> ",sep);print("after_sep --> ",after_sep,'\n')

s9 = "hanzalaxxxxxxx420@gmail.com"
print("s9.partition('@') --> ",s9.partition('@'))
before_sep,sep,after_sep = s9.partition('@')
print("before_sep --> ",before_sep);print("sep --> ",sep);print("after_sep --> ",after_sep,'\n')


# we can pass a tuple of one element that must be string as separator
s10 = "abcdefghijklm"
print("s10.partition(('f')) --> ",s10.partition(('f')))

