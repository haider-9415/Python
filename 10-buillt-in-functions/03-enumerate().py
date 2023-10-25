#  enumerate(iterable, start=0) --> to get each element of a string with its index
""" it is an iterable-object like string,etc. but its elements are in the form of tuple like (x,y)
    where 'x' is the index and 'y' is the element at 'x' """
""" It does not printed directely. We have to convert it into list, dict, tuple, set """


# for string
str1 = 'haider'
str3 = 'HANZALA'

print('enumerated --> list')
l1 = enumerate(str1)
print("    l1 --> ",list(l1))
print("    PWskills --> ",list(enumerate('PWskills')),'\n')
print('enumerated --> tuple')
t1 = enumerate(str1)
print("    t1 --> ",tuple(t1))
print("    PWskills --> ",tuple(enumerate('PWskills')),'\n')
print('enumerated --> dict')
d1 = enumerate(str1)
print("    d1 --> ",dict(d1))
print("    PWskills --> ",dict(enumerate('PWskills')),'\n')
print('enumerated --> set')
s1 = enumerate(str1)
print("    s1 --> ",set(s1))
print("    PWskills --> ",set(enumerate('PWskills')),'\n')

""" we can show the different indexing using 'start' attribute """
l2 = list(enumerate(str1,start= -10))
print("l2 --> ",l2)
print("l2[1] -->",l2[1]);print("l2[2] -->",l2[2]);print("l2[3] -->",l2[3])
print("l2[4] -->",l2[4]);print("l2[5] -->",l2[5],'\n')
d2 = dict(enumerate(str1,start=100))
print("d2 --> ",d2)
print("d2[100] -->",d2[100]);print("d2[101] -->",d2[101]);print("d2[102] -->",d2[102])
print("d2[103] -->",d2[103]);print("d2[104] -->",d2[104],'\n')

""" we can use loops to print it """
j = 0
print("\nusing loop")
for i in enumerate(str3):
    print("at index",j,": ",i)
    j += 1

print("\nusing loop")
j = 0
for i,k in enumerate(str3): # i for index and k for element
    print("at index",j,": ",i, k)
    j += 1

print("\nusing loop")
j = 0

for i,k in enumerate(str3,100): # i for index and k for element
    print("at index",j,": ",i," --> ",k)
    j += 1

print("\nusing loop")
j = 0
for i,k in enumerate(str3,-4): # i for index and k for element
    print("at index",j,": ",i," --> ",k)
    j += 1
print()



# for list
lt1 = [1,2,53.665,'haider',34-42j,True]
lt2 = [23,43,65,90,776,6,54,333,45,-1,337343,-292383]
lt3 = ['pwskills','coolege wallah','sudh','python']

print('enumerated --> list')
l3 = enumerate(lt1)
print("    l3 --> ",list(l3))
print("    ['a','b','c'] --> ",list(enumerate(['a','b','c'])),'\n')
print('enumerated --> tuple')
t2 = enumerate(lt2)
print("    t2 --> ",tuple(t2))
print("    ['a','b','c'] --> ",tuple(enumerate(['a','b','c'])),'\n')
print('enumerated --> dict')
d3 = enumerate(lt3)
print("    d3 --> ",dict(d3))
print("    ['a','b','c'] --> ",dict(enumerate(['a','b','c'])),'\n')
print('enumerated --> set')
s2 = enumerate(lt1)
print("    s2 --> ",set(s2))
print("    ['a','b','c'] --> ",set(enumerate(['a','b','c'])),'\n')

""" we can show the different indexing using 'start' attribute """
l4 = list(enumerate(lt1,start= -10))
print("l4 --> ",l4)
print("l4[1] -->",l4[1]);print("l4[2] -->",l4[2]);print("l4[3] -->",l4[3])
print("l4[4] -->",l4[4]);print("l4[5] -->",l4[5],'\n')
d4 = dict(enumerate(lt2,start=100))
print("d4 --> ",d4)
print("d4[100] -->",d4[100]);print("d4[101] -->",d4[101]);print("d4[102] -->",d4[102])
print("d4[103] -->",d4[103]);print("d4[104] -->",d4[104],'\n')

""" we can use loops to print it """
j = 0
print("\nusing loop")
for i in enumerate(lt3):
    print("at index",j,": ",i)
    j += 1

print("\nusing loop")
j = 0
for i,k in enumerate(lt2,-4): # i for index and k for element
    print("at index",j,": ",i," --> ",k)
    j += 1
print()




# for tuple
tp1 = (1,2,3,2,'haider','hanzala',9-45j,'haider')
tp2 = (34.34,123.0,232.565,789.433)
tp3 = ('wad','ajh','aafre','yakf')

print('enumerated --> list')
l5 = enumerate(tp1)
print("    l5 --> ",list(l5))
print("    ('a','b','c','d') --> ",list(enumerate(('a','b','c','d'))),'\n')
print('enumerated --> tuple')
t3 = enumerate(tp2)
print("    t3 --> ",tuple(t3))
print("    ('a','b','c','d') --> ",tuple(enumerate(('a','b','c','d'))),'\n')
print('enumerated --> dict')
d5 = enumerate(tp3)
print("    d5 --> ",dict(d5))
print("    ('a','b','c','d') --> ",dict(enumerate(('a','b','c','d'))),'\n')

""" we can show the different indexing using 'start' attribute """
l6 = list(enumerate(tp1,start= -10))
print("l6 --> ",l6)
print("l6[1] -->",l6[1]);print("l6[2] -->",l6[2]);print("l6[3] -->",l6[3])
print("l6[4] -->",l6[4]);print("l6[5] -->",l6[5],'\n')
d6 = dict(enumerate(tp2,start=100))
print("d6 --> ",d6)
print("d6[100] -->",d6[100]);print("d6[101] -->",d6[101]);print("d6[102] -->",d6[102])
print("d6[103] -->",d6[103])

""" we can use loops to print it """
j = 0
print("\nusing loop")
for i in enumerate(tp3):
    print("at index",j,": ",i)
    j += 1

print("\nusing loop")
j = 0
for i,k in enumerate(tp2,-4): # i for index and k for element
    print("at index",j,": ",i," --> ",k)
    j += 1
print()




# for set
st1 = {1,3,2,566,"haider",90+97j,3.655,'naeem',"hanzala"}
st2 = {1,45,344,90,-9049,393993}
st3 = {'tdf','cdfe','ahde','aavk','ziue','wyet'}

print('enumerated --> list')
l6 = enumerate(st1)
print("    l6 --> ",list(l6))
print("    {'a','b','c','d'} --> ",list(enumerate({'a','b','c','d'})),'\n')
print('enumerated --> tuple')
t3 = enumerate(st2)
print("    t3 --> ",tuple(t3))
print("    {'a','b','c','d'} --> ",tuple(enumerate({'a','b','c','d'})),'\n')
print('enumerated --> dict')
d6 = enumerate(st3)
print("    d6 --> ",dict(d6))
print("    {'a','b','c','d'} --> ",dict(enumerate({'a','b','c','d'})),'\n')

""" we can show the different indexing using 'start' attribute """
l7 = list(enumerate(st1,start= -10))
print("l7 --> ",l7)
print("l7[1] -->",l7[1]);print("l7[2] -->",l7[2]);print("l7[3] -->",l7[3])
print("l7[4] -->",l7[4]);print("l7[5] -->",l7[5],'\n')
d7 = dict(enumerate(st3,start=100))
print("d7 --> ",d7)
print("d7[100] -->",d7[100]);print("d7[101] -->",d7[101]);print("d7[102] -->",d7[102])
print("d7[103] -->",d7[103]);print("d7[104] -->",d7[104],'\n')

""" we can use loops to print it """
j = 0
print("\nusing loop")
for i in enumerate(st3):
    print("at index",j,": ",i)
    j += 1

print("\nusing loop")
j = 0
for i,k in enumerate(st2,-4): # i for index and k for element
    print("at index",j,": ",i," --> ",k)
    j += 1
print()





