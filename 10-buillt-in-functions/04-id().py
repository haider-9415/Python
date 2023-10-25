# id() --> to get memory address

# for string
print("id('haider') --> ",id("haider"),'\n')
a='haider';print("a --> ",a,'\n');print("id(a) --> ",id(a),'\n')
b = a; print("id(b) --> ",id(b),'\n')

a = 'naeem';print("a --> ",a,'\n'); print("id(a) --> ",id(a),'\n')

""" two different variables pointing same literal have same 
    id(memory address) """
str5 = 'hanzala'; print("id(str5) --> ",id(str5),'\n')
str6 = 'hanzala'; print("id(str6) --> ",id(str6),'\n')
print("id(str5) == id(str6) --> ",id(str5) == id(str6),'\n')
a = id(str5); print("a == id(str5) --> ",a == id(str5),'\n')

""" same characters in a string has same memory address """
str7 = "hanzala"
print("id(str7[0]) --> ",id(str7[0]),'\n');print("id(str7[1]) --> ",id(str7[1]),'\n');print("id(str7[2]) --> ",id(str7[2]),'\n');print("id(str7[3]) --> ",id(str7[3]),'\n')
print("id(str7[4]) --> ",id(str7[4]),'\n');print("id(str7[5]) --> ",id(str7[5]),'\n');print("id(str7[6]) --> ",id(str7[6]),'\n')
""" you can see id(str7[1]), id(str7[4]) and id(str7[6]) have same memory addresses ,because, these have same character """

""" all sliced parts of a string have not the same memory address """
print("id(str7[2:6]) --> ",id(str7[2:6]),'\n');print("id(str7[1:4]) --> ",id(str7[1:4]),'\n')
print("id(str7[-5:-3]) --> ",id(str7[-5:-3]),'\n');print("id(str7[-2:-6]) --> ",id(str7[-2:-6]),'\n')
print("id(str7[-1:-4]) --> ",id(str7[-1:-4]),'\n');print("id(str7[3:5]) --> ",id(str7[3:5]),'\n')



# for list
l = [1,2,53.665,'haider',34-42j,True]
l1 = [1,5,1,6.5,1,5.6,433.67,0,-445,-344,1,-1]
l2 = ['abc','wed','aaf','abc']

print("id(l) --> ",id(l),'\n')
print("id(l1) --> ",id(l1),'\n')
print("id(l2) --> ",id(l2),'\n')

""" same elements in a list have the same memory address """
print("id(l2[0]) --> ",id(l2[0]),'\n');print("id(l2[1]) --> ",id(l2[1]),'\n');print("id(l2[2]) --> ",id(l2[2]),'\n');print("id(l2[3]) --> ",id(l2[3]),'\n')
""" you can see id(l2[1]) and id(l2[3]) have same memory addresses , because, they have same element """

""" all sliced parts of a list have same memory address """
print("id(l1[2:6]) --> ",id(l1[2:6]),'\n');print("id(l1[1:4]) --> ",id(l1[1:4]),'\n')
print("id(l1[-5:-3]) --> ",id(l1[-5:-3]),'\n');print("id(l1[-2:-6]) --> ",id(l1[-2:-6]),'\n')
print("id(l1[-1:-4]) --> ",id(l1[-1:-4]),'\n');print("id(l1[3:5]) --> ",id(l1[3:5]),'\n')




# for tuple
tp1 = (1,2,3,2,'haider','hanzala',9-45j,'haider')
tp2 = (34.34,123.0,232.565,789.433)
tp3 = ('wad','ajh','aafre','wad')

print("id(tp1) --> ",id(tp1),'\n')
print("id(tp2) --> ",id(tp2),'\n')
print("id(tp3) --> ",id(tp3),'\n')

""" same elements in a tuple have the same memory address """
print("id(tp3[0]) --> ",id(tp3[0]),'\n');print("id(tp3[1]) --> ",id(tp3[1]),'\n');print("id(tp3[2]) --> ",id(tp3[2]),'\n');print("id(tp3[3]) --> ",id(tp3[3]),'\n')
""" you can see id(tp3[1]) and id(tp3[3]) have same memory addresses , because, they have same element """

""" all sliced parts of a tuple have nat same memory address """
print("id(tp2[2:6]) --> ",id(tp2[2:6]),'\n');print("id(tp2[1:4]) --> ",id(tp2[1:4]),'\n')
print("id(tp2[-5:-3]) --> ",id(tp2[-5:-3]),'\n');print("id(tp2[-2:-6]) --> ",id(tp2[-2:-6]),'\n')
print("id(tp2[-1:-4]) --> ",id(tp2[-1:-4]),'\n');print("id(tp2[3:5]) --> ",id(tp2[3:5]),'\n')




# for dict
dict1 = {'a':1,'b':2,'c':3,'d':1}
dict2 = {'name':'haider','class':"10th B","""subject""":2}
dict3 = {'subject' : ['physics','math','chemistry'],'abcd':{100:'a',200:'b',300:'c'},
         'teachers':{'sudhanshu','sanket','vishwamohan','nitin','kirish','vishwamohan','haider'}}

print("id(dict1) --> ",id(dict1),'\n')
print("id(dict2) --> ",id(dict2),'\n')
print("id(dict3) --> ",id(dict3),'\n')

""" the keys having same values have same memory addresses """
print("id(dict1['a']) --> ",id(dict1['a']),'\n');print("id(dict1['b']) --> ",id(dict1['b']),'\n')
print("id(dict1['c']) --> ",id(dict1['c']),'\n');print("id(dict1['d']) --> ",id(dict1['d']),'\n')
""" you can see id(dict1['a']) and id(dict1['d']) have same memory addresses , because, they have same values """




# for set
s1 = {1,3,2,566,"haider",90+97j,3.655,'naeem',"hanzala"}
s2 = {1,45,344,90,-9049,393993}
s3 = {'tdf','cdfe','ahde','tdf','ziue','wyet'}

print("id(s1) --> ",id(s1),'\n')
print("id(s2) --> ",id(s2),'\n')
print("id(s3) --> ",id(s3),'\n')

