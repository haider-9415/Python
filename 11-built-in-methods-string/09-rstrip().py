""" str.rstrip(chars) --> it works like strip() but it removes characters only from right side   """


a = '  hanzala'; b = '  hanzala  '
print("a == b --> ",a == b,'\n')

print("a == b.rstrip() --> ",a == b.rstrip(),'\n') # it is true, because, rstrip() has removed spaces from right side by default

print("a == b.rstrip(" ") --> ",a == b.rstrip(' '),'\n')  # it is true, because, rstrip() has removed spaces from right side by manual


# without using (), it will not give run time error
s1 = '@@haider'.rstrip
print("s1 --> ",s1,'\n')
print("'#abcd#'.rstrip --> ",'#abcd#'.rstrip,'\n')


# it can be used only with a tuple of one element that should be string
print("('$$haider$').rstrip('$') --> ",('$$haider$').rstrip('$'),'\n')
print("('rhanzalarrr').rstrip('r') --> ",('rhanzalarrr').rstrip('r'),'\n')

# the following will give run time error
# print(['  haider  '].rstrip())
# print([  'h','a','i','d','e','r'  ].rstrip())
# print((  'h','a','i','d','e','r'  ).rstrip())
# print({'  haider  '}.rstrip())
# print({  'h','a','i','d','e','r'  }.rstrip())


# rstrip() removes all characters present in 'chars' from the string until any different character will come in right
s2 = "@#@hanzala@#*#naemm####@*"

# it will not remove '@' in right, because, before that, different character '*' is coming in right
print("s2.rstrip('@') --> ",s2.rstrip("@"),'\n')
# it will remove '@' & '*' in right side until '#' comes
print("s2.rstrip('@*') --> ",s2.rstrip("@*"),'\n')
# it will remove '*' in right side 
print("s2.rstrip('*') --> ",s2.rstrip("*"),'\n')
# it will not remove '#' but remove '*' in right side, because, before '#', there is a '@'
print("s2.rstrip('#*') --> ",s2.rstrip("#*"),'\n')
# it will remove all '#', '@' & '*' in right side until 'm' comes
print("s2.rstrip('@#*') --> ",s2.rstrip("@#*"),'\n')
# similarly
s3 = '##@hai%$@#der%$@'
print("s3.rstrip('#') --> ",s3.rstrip('#'),'\n')    # '##@hai%$@#der%$@'
print("s3.rstrip('@') --> ",s3.rstrip('@'),'\n')    # '##@hai%$@#der%$'
print("s3.rstrip('@#') --> ",s3.rstrip('@#'),'\n')  # '##@hai%$@#der%$'
print("s3.rstrip('@$') --> ",s3.rstrip('@$'),'\n')  # '##@hai%$@#der%'
print("s3.rstrip('#%') --> ",s3.rstrip('#%'),'\n')  # '##@hai%$@#der%$@'
print("s3.rstrip('%$@') --> ",s3.rstrip('%$@'),'\n')  # '##@hai%$@#der'
s4 = '234abcd63efgh432'
print("s4.rstrip('3') --> ",s4.rstrip('3'),'\n')  # '234abcd63efgh432'
print("s4.rstrip('2') --> ",s4.rstrip('2'),'\n')  # '234abcd63efgh43'
print("s4.rstrip('43') --> ",s4.rstrip('43'),'\n')  # '234abcd63efgh432'
print("s4.rstrip('234') --> ",s4.rstrip('234'),'\n')  # '234abcd63efgh'
print("s4.rstrip('23') --> ",s4.rstrip('23'),'\n')  # '234abcd63efgh4'


# if we enter None in lstrip then it will work as it works with default value
s5 = '  haider  '
print("s5.rstrip() --> ",s5.rstrip(),'\n')
print("s5.rstrip(None) --> ",s5.rstrip(None),'\n')
print("s5.rstrip() == s5.rstrip(None) --> ",s5.rstrip() == s5.rstrip(None),'\n')