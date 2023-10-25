""" str.endswith(prefix,start,end) --> it checks the string is ending at the given prefix or not
    if the string ends at the prefix then it returns 'True' and otherwise returns 'False'   
    so it returns a boolean value   """

s1 = 'hanzala'
print("s1.endswith('a') --> ",s1.endswith('a'),'\n')
print("s1.endswith('la') --> ",s1.endswith('la'),'\n')
print("s1.endswith('ala') --> ",s1.endswith('ala'),'\n')
print("s1.endswith('zala') --> ",s1.endswith('zala'),'\n')
print("s1.endswith('nzala') --> ",s1.endswith('nzala'),'\n')
print("s1.endswith('anzala') --> ",s1.endswith('anzala'),'\n')
print("s1.endswith('h') --> ",s1.endswith('h'),'\n')
print("s1.endswith('an') --> ",s1.endswith('an'),'\n')
print("s1.endswith('han') --> ",s1.endswith('han'),'\n')
print("s1.endswith('al') --> ",s1.endswith('al'),'\n')


# it is case sensitive, therefore, the following will give false
print("s1.endswith('A') --> ",s1.endswith('A'),'\n')
print("s1.endswith('La') --> ",s1.endswith('La'),'\n')
print("s1.endswith('aLa') --> ",s1.endswith('aLa'),'\n')
print("s1.endswith('zalA') --> ",s1.endswith('zalA'),'\n')
print("s1.endswith('anzalA') --> ",s1.endswith('anzalA'),'\n')


# it can be used only with a tuple of one element that should be string
print("('haider').endswith('r') --> ",('haider').endswith('r'),'\n')
print("('haider').endswith('der') --> ",('haider').endswith('der'),'\n')
print("('haider').endswith('R') --> ",('haider').endswith('R'),'\n')
print("('haider').endswith('dEr') --> ",('haider').endswith('dEr'),'\n')

# the following will give run time error
# print(['haider'].endswith('r'))
# print(['h','a','i','d','e','r'].endswith('r'))
# print(('h','a','i','d','e','r').endswith('r'))
# print({'haider'}.endswith('r'))
# print({'h','a','i','d','e','r'}.endswith('r'))


# if there is str.endswith(a,x) then it will search that 'a' is in the ending of that part of 'str' which is starting from 'x'
s2 = 'This Is The Class of Computer Science'
print("s2.endswith('e',30) --> ",s2.endswith('e',30),'\n') # 'e' is in the ending of that part which is starting from 30th index
print("s2.endswith('ence',12) --> ",s2.endswith('ence',12),'\n') # 'ence is in the ending of that part which is starting from 12th index
# similarly
print("s2.endswith('e',0) --> ",s2.endswith('e',0),'\n')
print("s2.endswith('ience',18) --> ",s2.endswith('ience',18),'\n')
print("s2.endswith('er Science',5) --> ",s2.endswith('er Science',5),'\n')
# the following will give false
print("s2.endswith(' Scie',12) --> ",s2.endswith(' Scie',12),'\n')
print("s2.endswith('c',30) --> ",s2.endswith('c',30),'\n')
# the following will give false due to be case sensitive
print("s2.endswith('E',30) --> ",s2.endswith('E',30),'\n') 
print("s2.endswith('enCe',12) --> ",s2.endswith('enCe',12),'\n') 
print("s2.endswith('E',0) --> ",s2.endswith('E',0),'\n')
print("s2.endswith('ieNcE',18) --> ",s2.endswith('ieNcE',18),'\n')
print("s2.endswith('er science',5) --> ",s2.endswith('er science',5),'\n')
print("s2.endswith(' SCie',12) --> ",s2.endswith(' SCie',12),'\n')
print("s2.endswith('C',30) --> ",s2.endswith('C',30),'\n')


# using start and end attributes we can check that the given word is in the ending of the given string or not
# remember if end=x then 'x' excludes, so, to include 'x', we will have to entered 'x+1'
print("s2.endswith('This',0,4) --> ",s2.endswith('This',0,4),'\n')
print("s2.endswith('Clas',0,16) --> ",s2.endswith('Clas',0,16),'\n') # 'clas' is in the ending of the string from 0th index to 15th index
print("s2.endswith('S',5,31) --> ",s2.endswith('S',5,31),'\n') # 'S' is in the ending of the string from 5th index to 30th index
print("s2.endswith('Science',0,None) --> ",s2.endswith('Science',0,None),'\n') # 'Science' is in the ending of the string from 0th index to last index
print("s2.endswith('of C',12,22) --> ",s2.endswith('of C',12,22),'\n') # 'of C' is in the ending of the string from 12th index to 21th index
# similarly
print("s2.endswith('er S',10,31) --> ",s2.endswith('er S',10,31),'\n')
print("s2.endswith(' The',2,11) --> ",s2.endswith(' The',2,11),'\n')
print("s2.endswith(' Is',1,7) --> ",s2.endswith(' Is',1,7),'\n')


# we can use -ve marking
s3 = 'Hanzala Naeem'
print("s3.endswith('em',-5) --> ",s3.endswith('em',-5),'\n')
print("s3.endswith('Naeem',-9) --> ",s3.endswith('Naeem',-9),'\n')
print("s3.endswith('eem',-6) --> ",s3.endswith('eem',-6),'\n')
print("s3.endswith('naeem',-9) --> ",s3.endswith('naeem',-9),'\n')
print("s3.endswith('H',-10) --> ",s3.endswith('H',-10),'\n')
print("s3.endswith('Nae',-8,-2) --> ",s3.endswith('Nae',-8,-2),'\n')
print("s3.endswith('Nae',-8,-3) --> ",s3.endswith('Nae',-8,-3),'\n')
print("s3.endswith('ala',-13,-6) --> ",s3.endswith('ala',-13,-6),'\n')
print("s3.endswith('Hanzal',-13,-7) --> ",s3.endswith('Hanzal',-13,-7),'\n')
print("s3.endswith('Hanzal',-13,-8) --> ",s3.endswith('Hanzal',-13,-8),'\n')
print("s3.endswith('HanzaL',-13,-7) --> ",s3.endswith('HanzaL',-13,-7),'\n')
print("s3.endswith('m',-1,None) --> ",s3.endswith('m',-1,None),'\n')


# if we give possibilities to check that at which the string is ending then we use tuple like endswith(tuple)
s4 = "Magnet Brains Is The Best Educational Platform"
# it will give true, because, we have given some possibilities and one possibility is true that is 'm'
print("s4.endswith(('m','ma','b','B','Mab','M') --> ",s4.endswith(('m','ma','b','B','Mab','M')),'\n')
# it will give false, because, we have given some possibilities and any possibility is not true
print("s4.endswith(('ma','b','B','Mab','M') --> ",s4.endswith(('m','ma','b','B','Mab','maa')),'\n')
# it will give true, because, we have given some possibilities and one possibility is true that is 'The' ,because we used start=7 & end=20
print("s4.endswith(('m','ma','b','B','The'),7,20) --> ",s4.endswith(('m','ma','b','B','The'),7,20),'\n')
# it will give false, because, we have given some possibilities and the possibility 'The' is also not true, because we used start=7 & end=19
print("s4.endswith(('m','ma','b','B','The'),7,19) --> ",s4.endswith(('m','ma','b','B','The'),7,19),'\n')


# on passing empty string, the answer is always true
s5 = "abcdefg"
print("for empty string:  s5.endswith('') --> ",s5.endswith(''),'\n')
# on passing space, the answer will be false if the first character is not the space
print("on passing space:  s5.endswith(' ') --> ",s5.endswith(' '),'\n')
# if first character is space then the the result will be true
s6 = ' abcd '
print("s6.endswith(' ') --> ",s6.endswith(' '),'\n')
# similarly
s7 = 'abcdefg\n'
print("s7.endswith('\\n') --> ",s7.endswith('\n'),'\n')
print("s7.endswith(' ') --> ",s7.endswith(' '),'\n')
print("s7.endswith('') --> ",s7.endswith(''),'\n')

s8 = """
it is a string
"""
print("s8.endswith('\\n') --> ",s8.endswith('\n'),'\n') # it is true, because, in 's8', last character is '\n' 
