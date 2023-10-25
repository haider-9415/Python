# sorted(iterable, key=None, reverse=False) --> to sort an iterable object 
""" elements are sorted according to their unicode value & dictionary order it returns a list """
""" remember in list,etc. elements must be of same class"""




# for string
str1 = 'haider'
str2 = 'this is the lecture to know the in-built functions of string '
str3 = 'HANZALA'
str4 = 'Naeem'

print("sorted(str3) --> ",sorted(str3),'\n')
print("sorted(str4) --> ",sorted(str4),'\n')
s1 = 'hanuwnd024351,.;"[]'
print("sorted(s1) --> ",sorted(s1),'\n')
s2 = '!@#$%^&*()_+'
print("sorted(s2) --> ",sorted(s2),'\n')

""" to sort in descending order, we use reverse=True """
print("sorted(str3,reverse=True) --> ",sorted(str3,reverse=True),'\n')
print("sorted(str4,reverse=True) --> ",sorted(str4,reverse=True),'\n')
print("sorted(s1,reverse=True) --> ",sorted(s1,reverse=True),'\n')
print("sorted(s2,reverse=True)) --> ",sorted(s2,reverse=True),'\n')

""" to sort according to our directions, we use key """
print("sorted(str1,key=len) --> ",sorted(str1,key=len),'\n')# it will sort str1 according to length of each element




# for list
lt1 = [1,2,53.665,'haider',34-42j,True]
lt2 = [43,5,4,6.5,6,5.6,433.67,0,-445,-344,1,-1]
lt3 = ['abc','wed','aaf','fd']

# print("sorted(lt1) --> ",sorted(lt1),'\n') # it will give run time error, because, elements are not from same class
print("sorted(lt3) --> ",sorted(lt3),'\n')
print("sorted(lt2) --> ",sorted(lt2),'\n')

l1 = [1,2,3,4,5,6,7,8,9,10]
print("sorted(l1) --> ",sorted(l1),'\n')
l2 = ['a','b','c','d']
print("sorted(l2) --> ",sorted(l2),'\n')

""" to sort in descending order, we use reverse=True """
print("sorted(lt3,reverse=True) --> ",sorted(lt3,reverse=True),'\n')
print("sorted(lt2,reverse=True) --> ",sorted(lt2,reverse=True),'\n')
print("sorted(l1,reverse=True) --> ",sorted(l1,reverse=True),'\n')
print("sorted(l2,reverse=True)) --> ",sorted(l2,reverse=True),'\n')

""" to sort according to our directions, we use key """
print("sorted(lt1,key=len) --> ",sorted(lt3,key=len),'\n')# it will sort lt3 according to length of elements




# for tuple
tp1 = (1,2,3,2,'haider','hanzala',9-45j,'haider')
tp2 = (34.34,123.0,232.565,789.433)
tp3 = ('wad','ajh','aafre','yakf')

# print("sorted(tp1) --> ",sorted(tp1),'\n') # it will give run time error, because, elements are not from same class
print("sorted(tp3) --> ",sorted(tp3),'\n')
print("sorted(tp2) --> ",sorted(tp2),'\n')

t1 = (1,2,3,4,5,6,7,8,9,10)
print("sorted(t1) --> ",sorted(t1),'\n')
t2 = ('a','b','c','d')
print("sorted(t2) --> ",sorted(t2),'\n')

""" to sort in descending order, we use reverse=True """
print("sorted(tp3,reverse=True) --> ",sorted(tp3,reverse=True),'\n')
print("sorted(tp2,reverse=True) --> ",sorted(tp2,reverse=True),'\n')
print("sorted(t1,reverse=True) --> ",sorted(t1,reverse=True),'\n')
print("sorted(t2,reverse=True)) --> ",sorted(t2,reverse=True),'\n')

""" to sort according to our directions, we use key """
print("sorted(tp3,key=len) --> ",sorted(tp3,key=len),'\n')# it will sort tp3 according to length of elements




# for set
st1 = {1,3,2,566,"haider",90+97j,3.655,'naeem',"hanzala"}
st2 = {1,45,344,90,-9049,393993}
st3 = {'tdf','cdfe','ahwde','aavk','ziwue','wyet'}

# print("sorted(s1) --> ",sorted(s1),'\n') # it will give run time error, because, elements are not from same class
print("st2 --> ",st2)
print("sorted(st2) --> ",sorted(st2),'\n')
print("st3 --> ",st3)
print("sorted(st3) --> ",sorted(st3),'\n')

s1 = {1,2,3,4,5,6,7,8,9,10}
print("s1 --> ",s1)
print("sorted(s1) --> ",sorted(s1),'\n')
s2 = {'a','b','c','d'}
print("s2 --> ",s2)
print("sorted(s2) --> ",sorted(s2),'\n')

""" to sort in descending order, we use reverse=True """
print("st3 --> ",st3)
print("sorted(st3,reverse=True) --> ",sorted(st3,reverse=True),'\n')
print("st2 --> ",st2)
print("sorted(st2,reverse=True) --> ",sorted(st2,reverse=True),'\n')
print("s1 --> ",s1)
print("sorted(s1,reverse=True) --> ",sorted(s1,reverse=True),'\n')
print("s2 --> ",s2)
print("sorted(s2,reverse=True)) --> ",sorted(s2,reverse=True),'\n')

""" to sort according to our directions, we use key """
print("st3 --> ",st3)
print("sorted(st3,key=len) --> ",sorted(st3,key=len),'\n')# it will sort st3 according to length of elements




# for dictionary , in this, it will sort only keys
dc1 = {'a':1,10:2,'c':3}
dc2 = {'ad':1,'abc':2,'z':3}
dc3 = {1:'a',2:'d',3:'c'}


# print("sorted(dc1) --> ",sorted(dc1),'\n') # it will give run time error, because, keys are not from same class
print("dc2 --> ",dc2)
print("sorted(dc2) --> ",sorted(dc2),'\n')
print("dc3 --> ",dc3)
print("sorted(dc3) --> ",sorted(dc3),'\n')

d1 = {1:'hanzala',2:'haider',3:'naeem'}
print("d1 --> ",d1)
print("sorted(d1) --> ",sorted(d1),'\n')
d2 = {"subject":"math","class":"math"}
print("d2 --> ",d2)
print("sorted(d2) --> ",sorted(d2),'\n')

""" to sort in descending order, we use reverse=True """
print("dc3 --> ",dc3)
print("sorted(dc3,reverse=True) --> ",sorted(dc3,reverse=True),'\n')
print("dc2 --> ",dc2)
print("sorted(dc2,reverse=True) --> ",sorted(dc2,reverse=True),'\n')
print("d1 --> ",d1)
print("sorted(d1,reverse=True) --> ",sorted(d1,reverse=True),'\n')
print("d2 --> ",d2)
print("sorted(d2,reverse=True)) --> ",sorted(d2,reverse=True),'\n')

""" to sort according to our directions, we use key """
print("dc2 --> ",dc2)
print("sorted(dc2,key=len) --> ",sorted(dc2,key=len),'\n')# it will sort dc2 according to length of elements