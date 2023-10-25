# String interpolation
""" syntax --> print(format_string % (values)) """

# format_string contains placeholders
""" general syntax for a format place holder --> %flag width precision type """

# width --> it is the no. of blocks that a value can contain including decimal point
# precision --> it is the no. of blocks that the decimal part of the value can contain
""" remember, values are filled in the blocks from right side and empty blocks
    are shown in the form of spaces"""
# type --> it is the data type of the value
""" the types are 
    'd','i' or 'u' --> integer
    'f' or 'F' --> decimal float 
    'c' --> single character
    'r' or 's' --> string
    'o' --> octal
    'x' --> lowercase hexadecimal
    'X' --> uppercase hexadecimal
    'e' --> exponential float (lowercase)
    'E' --> exponential float (uppercase)
"""
print('viewers:%5d, subscribers:%8.2f'%(453,9.058))
print('we have %3d apples and %5d oranges'%(300,45433))
print('milk:%1.1fl, bread:%1dpec. and butter:%2dpec.'%(2.5,5,10))

print("%6.2f"%(23.789))
print("%6.2f"%(0.02225))
print("%6.2f"%(1992.02))
print("%6.2f"%(32223))
print("%6.2f"%(231.9002))



