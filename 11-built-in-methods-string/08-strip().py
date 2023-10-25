""" str.strip(chars) --> it removes chars from left and right side of the string 
    chars --> it is the set of characters which are to be removed 
    chars is optional and its default value is space,i.e., by dafault it removes sapces from left and right 
    of the string """


a = 'hanzala'; b = '  hanzala  '
print("a == b --> ",a == b,'\n')

print("a == b.strip() --> ",a == b.strip(),'\n') # it is true, because, strip() has removed spaces from left and right by default

print("a == b.strip(' ') --> ",a == b.strip(' '),'\n') # it is true, because, strip() has removed spaces from left and right by manual


# without using (), it will not give run time error
s1 = '@@haider'.strip
print("s1 --> ",s1,'\n')
print("'#abcd#'.strip --> ",'#abcd#'.strip,'\n')


# it can be used only with a tuple of one element that should be string
print("('$$haider$').strip('$') --> ",('$$haider$').strip('$'),'\n')
print("('rhanzalarrr').strip('r') --> ",('rhanzalarrr').strip('r'),'\n')


# the following will give run time error
# print(['  haider  '].strip())
# print([  'h','a','i','d','e','r'  ].strip())
# print((  'h','a','i','d','e','r'  ).strip())
# print({'  haider  '}.strip())
# print({  'h','a','i','d','e','r'  }.strip())


# strip() removes all characters present in 'chars' from the string until any different character will come in left or right side
s2 = "@#@hanzala@#*#naemm####@*"

# it will remove '@' from left, because, after that different characters are coming '#' in left and '*' in right side
print("s2.strip('@') --> ",s2.strip("@"),'\n')
# it will remove all '@' & '#' from left, because, in right side, different character '*' is coming
print("s2.strip('@#') --> ",s2.strip("@#"),'\n')
# it will remove '*' from right, because, after that different character '@' is coming in left and right side
print("s2.strip('*') --> ",s2.strip("*"),'\n')
# it will remove '*' from right, because, after that different character '@' is coming in left and right side
print("s2.strip('#*') --> ",s2.strip("#*"),'\n')
# it will remove all '*', '@' & '#' from right and left sides but not remove this part '@#*#' from between , beacuse, different characters are coming 'h' in left and 'm' in right side
print("s2.strip('@#*') --> ",s2.strip("@#*"),'\n')
# similarly
s3 = '##@hai%$@#der%$@'
print("s3.strip('#') --> ",s3.strip('#'),'\n')    # '@hai%$@#der%$@'
print("s3.strip('@') --> ",s3.strip('@'),'\n')    # '##@hai%$@#der%$'
print("s3.strip('@#') --> ",s3.strip('@#'),'\n')  # 'hai%$@#der%$'
print("s3.strip('@$') --> ",s3.strip('@$'),'\n')  # '##@hai%$@#der%'
print("s3.strip('#%') --> ",s3.strip('#%'),'\n')  # '@hai%$@#der%$@'

