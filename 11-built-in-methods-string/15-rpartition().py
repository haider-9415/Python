"""
   str.rpartition(separator) --> it works as well as partition() works
   it splits the string str at the first occurence of the separator from right
"""


s1 = "hanzalaxxxxxxx420@gmail.com"
print("s1.rpartition('@') --> ",s1.rpartition('@'),'\n')

s2 = "hanzala naeem"
print("s2.rpartition(' ') --> ",s2.rpartition(' '),'\n')

s3 = "hanzalanaeem"
print("s3.rpartition(' ') --> ",s3.rpartition(' '),'\n')

s4 = "hanzalaxxxxxxx420gmail.com"
print("s4.rpartition('@') --> ",s4.rpartition('@'),'\n')

s5 = "hanzala"
print("s5.rpartition('a') --> ",s5.rpartition('a'),'\n')

s6 = "abcd1abcd1abcd"
print("s6.rpartition('1') --> ",s6.rpartition('1'),'\n')


# without using (), it will not give run time error
s7 = "hanzala"
print("s7.rpartition --> ",s7.rpartition,'\n')


# it can be used only with a tuple of one element that should be string
print("('haider hanzala naeem').rpartition('n') --> ",('haider hanzala naeem').rpartition("n"),'\n')

# # the following will give run time error
# print(['haider hanzala naeem'].rpartition("n"))
# print(['haider hanzala naeem'].rpartition("n"))
# print(('haider hanzala naeem',).rpartition("n"))
# print({'haider hanzala naeem'}.rpartition("n"))
# print({'haider hanzala naeem'}.rpartition("n"))


# it splits a string in three parts, so, we can assign those three parts in three variables
s8 = "abcd1abcd1abcd"
print("s8.rpartition('1') --> ",s8.rpartition('1'))
before_sep,sep,after_sep = s8.rpartition('1')
print("before_sep --> ",before_sep);print("sep --> ",sep);print("after_sep --> ",after_sep,'\n')

s9 = "hanzalaxxxxxxx420@gmail.com"
print("s9.rpartition('@') --> ",s9.rpartition('@'))
before_sep,sep,after_sep = s9.rpartition('@')
print("before_sep --> ",before_sep);print("sep --> ",sep);print("after_sep --> ",after_sep,'\n')


# we can pass a tuple of one element that must be string as separator
s10 = "abcdefghijklm"
print("s10.rpartition(('f')) --> ",s10.rpartition(('f')),'\n')

