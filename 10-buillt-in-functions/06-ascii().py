""" ascii() function --> it returns the characters that are in ascii encodind scheme as it is, but
    the characters that are not in ascii encoding scheme, it returns their escape value """
# it returns in string class and print also non printable charactrs like escape sequences



# for string

s1 = 'haider'
print("s1 --> ",s1)
print("ascii(s1) --> ",ascii(s1),'\n')

s2 = '283+92j'
print("s2 --> ",s2)
print("ascii(s2) --> ",ascii(s2),'\n')

s3 = '[1,2,3,4,5,6]'
print("s3 --> ",s3)
print("ascii(s3) --> ",ascii(s3),'\n')

s4 = '(82,2923,skd)'
print("s4 --> ",s4)
print("ascii(s4) --> ",ascii(s4),'\n')

s5 = ''
print("s5 --> ",s5)
print("ascii(s5) --> ",ascii(s5),'\n')

s6 = ' '
print("s6 --> ",s6)
print("ascii(s6) --> ",ascii(s6),'\n')

s7 = '\n'
print("s7 --> ",s7)
print("ascii(s7) --> ",ascii(s7),'\n')

s8 = """ my name is hanzala,
          i am a class 12th student and
          i am learning C.S.
          """
print("s8 --> ",s8)
print("ascii(s8) --> ",ascii(s8),'\n')

""" the following are not in ascii encoding scheme """
s9 = 'خ'
print("s9 --> ",s9)
print("ascii(s9) --> ",ascii(s9),'\n')

s10 = 'ض ص ش س'
print("s10 --> ",s10)
print("ascii(s10) --> ",ascii(s10),'\n')

s11 = 'क'
print("s11 --> ",s11)
print("ascii(s11) --> ",ascii(s11),'\n')

s12 = 'ग ह ब '
print("s12 --> ",s12)
print("ascii(s12) --> ",ascii(s12),'\n')

s13 = 'ी'
print("s13 --> ",s13)
print("ascii(s13) --> ",ascii(s13),'\n')

s14 = 'बाहर'
print("s14 --> ",s14)
print("ascii(s14) --> ",ascii(s14),'\n')

s15 = 'الف'
print("s15 --> ",s15)
print("ascii(s15) --> ",ascii(s15),'\n')

s16 = ' ً  ْ  ٍ  ِ'
print("s16 --> ",s16)
print("ascii(s16) --> ",ascii(s16),'\n')
