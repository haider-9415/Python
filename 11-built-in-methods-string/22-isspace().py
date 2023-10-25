"""
   str.isspace() --> it returns True if all characters in str are spaces
   otherwise it returns False
"""

s1 = ' '
print("s1.isspace() --> ",s1.isspace(),'\n')

s2 = '      '
print("s2.isspace() --> ",s2.isspace(),'\n')

s3 = ""  # in case of empty string, it returns False
print("s3.isspace() --> ",s3.isspace(),'\n')

s4 = ' 0'
print("s4.isspace() --> ",s4.isspace(),'\n')

s5 = '391  92 19  '  
print("s5.isspace() --> ",s5.isspace(),'\n')

s6 = ' -3 9192  19'
print("s6.isspace() --> ",s6.isspace(),'\n')

s7 = "ab  cdAB CD"
print("s7.isspace() --> ",s7.isspace(),'\n')

s8 = "\n"
print("s8.isspace() --> ",s8.isspace(),'\n')

s9 = 'ABCDefgh'
print("s9.isspace() --> ",s9.isspace(),'\n')

s10 = '12345678'
print("s10.isspace() --> ",s10.isspace(),'\n') 

s11 = "@ # $ % ^ & * ( ) "
print("s11.isspace() --> ",s11.isspace(),'\n')

s12 = " 2819.21902  "
print("s12.isspace() --> ",s12.isspace(),'\n')

s13 = "   -28 19.219 02"
print("s13.isspace() --> ",s13.isspace(),'\n')


# without using (), it will not give run time error
s14 = "   "
print("s14.isspace --> ",s14.isspace,'\n')


# it can be used only with a tuple of one element that should be string
print("('   ').isspace() --> ",('   ').isspace(),'\n')

# # the following will give run time error
# print(['   '].isspace())
# print(('   ',).isspace())
# print({'   '}.isspace())
# print(['   ','   '].isspace())
# print({'   ','   '}.isspace())