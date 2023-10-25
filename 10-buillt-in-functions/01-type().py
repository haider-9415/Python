# it finds data type of an object

# for string
str1 = 'haider'
str2 = 'this is the lecture to know the in-built functions of string '

print("type(str1) --> ",type(str1),'\n');print("type(str2) --> ",type(str2),'\n')
print("type('12343) --> ",type('12343'),'\n');print("type('!@##$#:<>') --> ",type('!@##$#:<>'),'\n')
print("type(['s','dsww']) --> ",type("['s','dsww',322,'wass']"),'\n')



# for list
l = [1,2,53.665,'haider',34-42j,True]
l1 = [43,5,4,6.5,6,5.6,433.67,0,-445,-344,1,-1]

print("type(l) --> ",type(l),'\n')
print("type(l1) --> ",type(l1),'\n')



# for set
s1 = {1,3,2,566,"haider",90+97j,3.655,'naeem',"hanzala"}
s2 = {1,45,344,90,-9049,393993}
s3 = {'tdf','cdfe','ahde','aavk','ziue','wyet'}

print("type(s1) --> ",type(s1),'\n')
print("type(s2) --> ",type(s2),'\n')
print("type(s3) --> ",type(s3),'\n')



# for tuple
tp1 = (1,2,3,2,'haider','hanzala',9-45j,'haider')
tp2 = (34.34,123.0,232.565,789.433)
tp3 = ('wad','ajh','aafre','yakf')

print("type(tp1) --> ",type(tp1),'\n')
print("type(tp2) --> ",type(tp2),'\n')
print("type(tp3) --> ",type(tp3),'\n')



# for dictionary
dict1 = {'a':1,'b':2,'c':3,'d':4}
dict2 = {'name':'haider','class':"10th B","""subject""":'PCM'}
dict3 = {'subject' : ['physics','math','chemistry'],'abcd':{100:'a',200:'b',300:'c'},
         'teachers':{'sudhanshu','sanket','vishwamohan','nitin','kirish','vishwamohan','haider'}}

print("type(dict1) --> ",type(dict1),'\n')
print("type(dict2) --> ",type(dict2),'\n')
print("type(dict3) --> ",type(dict3),'\n')



# for boolean
bl1 = True
bl2 = False

print("type(bl1) --> ",type(bl1),'\n')
print("type(bl2) --> ",type(bl2),'\n')



# for None
print("type(None) --> ",type(None),'\n')