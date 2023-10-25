""" str.startswith(prefix,start,end) -->  it checks the string is starting from the given prefix or not 
    if the string starts from the prefix then it returns 'True' and otherwise returns 'False'   
    so it returns a boolean value """

s1 = 'hanzala'
print("s1.startswith('h') --> ",s1.startswith('h'),'\n')
print("s1.startswith('ha') --> ",s1.startswith('ha'),'\n')
print("s1.startswith('han') --> ",s1.startswith('han'),'\n')
print("s1.startswith('hanz') --> ",s1.startswith('hanz'),'\n')
print("s1.startswith('hanza') --> ",s1.startswith('hanza'),'\n')
print("s1.startswith('hanzal') --> ",s1.startswith('hanzal'),'\n')
print("s1.startswith('a') --> ",s1.startswith('a'),'\n')
print("s1.startswith('an') --> ",s1.startswith('an'),'\n')
print("s1.startswith('anz') --> ",s1.startswith('anz'),'\n')

# it is case sensitive 
# the following will give false
print("s1.startswith('H') --> ",s1.startswith('H'),'\n')
print("s1.startswith('Ha') --> ",s1.startswith('Ha'),'\n')
print("s1.startswith('hAn') --> ",s1.startswith('hAn'),'\n')
print("s1.startswith('haNz') --> ",s1.startswith('haNz'),'\n')
print("s1.startswith('hanZa') --> ",s1.startswith('hanZa'),'\n')
print("s1.startswith('hanzaL') --> ",s1.startswith('hanzaL'),'\n')


# it can be used only with a tuple of one element that should be string
print("('haider').startswith('h') --> ",('haider').startswith('h'),'\n')
print("('haider').startswith('hai') --> ",('haider').startswith('hai'),'\n')
print("('haider').startswith('H') --> ",('haider').startswith('H'),'\n')
print("('haider').startswith('haI') --> ",('haider').startswith('haI'),'\n')

# the following will give run time error
# print(['haider'].startswith('hai'))
# print(['h','a','i','d','e','r'].startswith('h'))
# print(('h','a','i','d','e','r').startswith('h'))
# print({'haider'}.startswith('hai'))
# print({'h','a','i','d','e','r'}.startswith('h'))


# if there is str.endswith(a,x) then it will search that 'a' is in the starting of that part of 'str' which is starting from 'x'
s2 = 'This Is The Class of Computer Science'
print("s2.startswith('T',8) --> ",s2.startswith('T',8),'\n')
print("s2.startswith('C',12) --> ",s2.startswith('C',12),'\n')
print("s2.startswith('s',3) --> ",s2.startswith('s',3),'\n')
print("s2.startswith('o',18) --> ",s2.startswith('o',18),'\n')
print("s2.startswith('Is',5) --> ",s2.startswith('Is',5),'\n')
print("s2.startswith('Class',12) --> ",s2.startswith('Class',12),'\n')
print("s2.startswith('Scien',30) --> ",s2.startswith('Scien',30),'\n')

# the following will give false due to be case sensitive 
print("s2.startswith('t',8) --> ",s2.startswith('t',8),'\n') 
print("s2.startswith('c',8) --> ",s2.startswith('c',8),'\n')
print("s2.startswith('S',8) --> ",s2.startswith('S',8),'\n')
print("s2.startswith('is',5) --> ",s2.startswith('is',5),'\n')
print("s2.startswith('ClaSs',12) --> ",s2.startswith('ClaSs',12),'\n')
print("s2.startswith('ScIen',30) --> ",s2.startswith('ScIen',30),'\n')


# using start and end attributes we can check that the given word is in the starting of the given string or not
# remember if end=x then 'x' excludes, so, to include 'x', we will have to entered 'x+1'
print("s2.startswith('This',0,20) --> ",s2.startswith('This',0,20),'\n')
print("s2.startswith('Clas',12,25) --> ",s2.startswith('Clas',12,25),'\n')
print("s2.startswith('ss of Compu',15,30) --> ",s2.startswith('ss of Compu',15,30),'\n')
print("s2.startswith('Science',30,37) --> ",s2.startswith('Science',30,37),'\n')
print("s2.startswith('Is The Class',5,17) --> ",s2.startswith('Is The Class',5,17),'\n')
print("s2.startswith('Is Class',5,17) --> ",s2.startswith('Is Class',5,17),'\n')
print("s2.startswith('is Is The',2,15) --> ",s2.startswith('is Is The',2,15),'\n')
print("s2.startswith('is Is the',2,15) --> ",s2.startswith('is Is the',2,15),'\n')
print("s2.startswith('T',0,None) --> ",s2.startswith('T',0,None),'\n')
print("s2.startswith('T',None,None) --> ",s2.startswith('T',None,None),'\n')

# we can use -ve marking
s3 = 'Hanzala Naeem'
print("s3.startswith('e',-2) --> ",s3.startswith('e',-2),'\n')
print("s3.startswith('E',-2) --> ",s3.startswith('E',-2),'\n')
print("s3.startswith(' ',-6) --> ",s3.startswith(' ',-6),'\n')
print("s3.startswith('Naee',-5) --> ",s3.startswith('Naee',-5),'\n')
print("s3.startswith('a Na',-7) --> ",s3.startswith('a Na',-7),'\n')
print("s3.startswith(' a Na',-7) --> ",s3.startswith(' a Na',-7),'\n')
print("s3.startswith('Nae',-5,-2) --> ",s3.startswith('Nae',-5,-2),'\n')
print("s3.startswith('Nae',-2,-5) --> ",s3.startswith('Nae',-2,-5),'\n')
print("s3.startswith('eeaN',-2,-6) --> ",s3.startswith('eeaN',-2,-6),'\n')
print("s3.startswith('Hanzal',-13,-8) --> ",s3.startswith('Hanzal',-13,-8),'\n')
print("s3.startswith('Hanzal',-13,-7) --> ",s3.startswith('Hanzal',-13,-7),'\n')
print("s3.startswith('HanzaL',-13,-7) --> ",s3.startswith('HanzaL',-13,-7),'\n')
print("s3.startswith('H',-1,None) --> ",s3.startswith('H',-1,None),'\n')


# if we give possibilities to check that from which the string is starting then we use tuple like startswith(tuple)
s4 = "Magnet Brains Is The Best Educational Platform"
# it will give true, because, we have given some possibilities and one possibility is true that is 'M'
print("s4.startswith(('m','ma','b','B','Mab','M') --> ",s4.startswith(('m','ma','b','B','Mab','M')),'\n')
# it will give false, because, we have given some possibilities and any possibility is not true
print("s4.startswith(('m','ma','b','B','Mab','M') --> ",s4.startswith(('m','ma','b','B','Mab','maa')),'\n')
# it will give true, because, we have given some possibilities and one possibility is true that is 'B' ,because we used start=7
print("s4.startswith(('m','ma','b','B','mab'),7) --> ",s4.startswith(('m','ma','b','B','mab'),7),'\n')
# similarly
print("s4.startswith(('m','ma','b','Is','mab'),14) --> ",s4.startswith(('m','ma','b','Is','mab'),14),'\n')
print("s4.startswith(('m','ma',' Th','B','mab'),16) --> ",s4.startswith(('m','ma',' Th','B','mab'),16),'\n')
print("s4.startswith(('m','best','b','B','mab'),20) --> ",s4.startswith(('m','best','b','B','mab'),20),'\n')
print("s4.startswith(('m','ma','b','B','MaG'),0) --> ",s4.startswith(('m','ma','b','B','MaG'),0),'\n')
print("s4.startswith(('m','ma','b','B','mab'),7) --> ",s4.startswith(('m','ma','b','B','mab'),7),'\n')
print("s4.startswith(('m','ma','b','Educational','mab'),26,37) --> ",s4.startswith(('m','ma','b','Educational','mab'),26,37),'\n')
print("s4.startswith(('m','ma','b','Brains','mab'),7,13) --> ",s4.startswith(('m','ma','b','Brains','mab'),7,13),'\n')
print("s4.startswith(('m','ma','b','Is The Be','mab'),14,23) --> ",s4.startswith(('m','ma','b','Is The Be','mab'),14,23),'\n')
print("s4.startswith(('m','ma','b','Is The Best','mab'),14,23) --> ",s4.startswith(('m','ma','b','Is The Best','mab'),14,23),'\n')


# on passing empty string, the answer is always true
s5 = "abcdefg"
print("for empty string:  s5.startswith('') --> ",s5.startswith(''),'\n')
# on passing space, the answer will be false if the first character is not the space
print("on passing space:  s5.startswith(' ') --> ",s5.startswith(' '),'\n')
# if first character is space then the the result will be true
s6 = ' abcd'
print("s6.startswith(' ') --> ",s6.startswith(' '),'\n')
# similarly
s7 = '\nabcdefg'
print("s7.startswith('\\n') --> ",s7.startswith('\n'),'\n')
print("s7.startswith(' ') --> ",s7.startswith(' '),'\n')
print("s7.startswith('') --> ",s7.startswith(''),'\n')

s8 = """
it is a string"""
print("s8.startswith('\\n') --> ",s8.startswith('\n'),'\n') # it is true, because, in 's8', first character is '\n' 

