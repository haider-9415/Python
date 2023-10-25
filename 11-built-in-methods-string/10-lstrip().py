""" str.lstrip(chars) --> it works like strip() but it removes characters only from left side   """


a = 'hanzala  '; b = '  hanzala  '
print("a == b --> ",a == b,'\n')

print("a == b.lstrip() --> ",a == b.lstrip(),'\n') # it is true, because, lstrip() has removed spaces from left side by default

print("a == b.lstrip(' ') --> ",a == b.lstrip(' '),'\n') # it is true, because, strip() has removed spaces from left side by manual


# without using (), it will not give run time error
s1 = '@@haider'.lstrip
print("s1 --> ",s1,'\n')
print("'#abcd#'.lstrip --> ",'#abcd#'.lstrip,'\n')


# it can be used only with a tuple of one element that should be string
print("('$$haider$').lstrip('$') --> ",('$$haider$').lstrip('$'),'\n')
print("('rhanzalarrr').lstrip('r') --> ",('rhanzalarrr').lstrip('r'),'\n')

# the following will give run time error
# print(['  haider  '].lstrip())
# print([  'h','a','i','d','e','r'  ].lstrip())
# print((  'h','a','i','d','e','r'  ).lstrip())
# print({'  haider  '}.lstrip())
# print({  'h','a','i','d','e','r'  }.lstrip())


# lstrip() removes all characters present in 'chars' from the string until any different character will come in left
s2 = "@#@hanzala@#*#naemm####@*"

# it will remove first '@' in left, because, after that, different character '#' is coming in left
print("s2.lstrip('@') --> ",s2.lstrip("@"),'\n')
# it will remove all '@' & '#' in left side until 'h' comes
print("s2.lstrip('@#') --> ",s2.lstrip("@#"),'\n')
# it will not remove '*', because, that is in right side 
print("s2.lstrip('*') --> ",s2.lstrip("*"),'\n')
# it will not remove '#' and '*', because,before '#', there is a '@' and * is in left side
print("s2.lstrip('#*') --> ",s2.lstrip("#*"),'\n')
# it will remove all '#' and '@' in left side but not '*', because, that is in right side
print("s2.lstrip('@#*') --> ",s2.lstrip("@#*"),'\n')
# similarly
s3 = '##@hai%$@#der%$@'
print("s3.lstrip('#') --> ",s3.lstrip('#'),'\n')    # '@hai%$@#der%$@'
print("s3.lstrip('@') --> ",s3.lstrip('@'),'\n')    # '##@hai%$@#der%$@'
print("s3.lstrip('@#') --> ",s3.lstrip('@#'),'\n')  # 'hai%$@#der%$@'
print("s3.lstrip('@$') --> ",s3.lstrip('@$'),'\n')  # '##@hai%$@#der%$@'
print("s3.lstrip('#%') --> ",s3.lstrip('#%'),'\n')  # '@hai%$@#der%$@'
print("s3.lstrip('%$@') --> ",s3.lstrip('%$@'),'\n')  # '##@hai%$@#der%$@'
s4 = '234abcd63efgh432'
print("s4.lstrip('3') --> ",s4.lstrip('3'),'\n')  # '234abcd63efgh432'
print("s4.lstrip('2') --> ",s4.lstrip('2'),'\n')  # '34abcd63efgh432'
print("s4.lstrip('43') --> ",s4.lstrip('43'),'\n')  # '234abcd63efgh432'
print("s4.lstrip('432') --> ",s4.lstrip('432'),'\n')  # 'abcd63efgh432'



# if we enter None in lstrip then it will work as it works with default value
s5 = '  haider  '
print("s5.lstrip() --> ",s5.lstrip(),'\n')
print("s5.lstrip(None) --> ",s5.lstrip(None),'\n')
print("s5.lstrip() == s5.lstrip(None) --> ",s5.lstrip() == s5.lstrip(None),'\n')