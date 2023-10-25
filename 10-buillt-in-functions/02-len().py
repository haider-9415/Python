# len() --> it gives length of an object or elements of the object

# for list
l = [1,2,53.665,'haider',34-42j,True]
l1 = [43,5,4,6.5,6,5.6,433.67,0,-445,-344,1,-1]
l2 = ['abc','wed','aaf','fd']

print('length of l = ',len(l),'\n')
print('length of l1 = ',len(l1),'\n')
print('length of l2= ',len(l2),'\n')




# for string, in this, it gives no. of characters
str1 = 'haider'
str2 = 'this is the lecture to know the in-built functions of string '
print("length of str1 = ",len(str1),'\n')
print("length of str2 = ",len(str2),'\n')

s1 = "" # empty string
print("length of s1 = ",len(s1),'\n')

s2 = "[1,2,3,4]" # s2 has 9 elements
print("length of s2 = ",len(s2),'\n') 

s3 = '(1,2,3)' # s3 has 7 elements
print("length of s3 = ",len(s3),'\n') 

""" if s[x:y] is a part of string 's' then  len(s[x:y]) = (y-x)  
    if x&y are -ve then  len(s[x:y]) = (|x|-|y|)                   """
print("length of len(str2[2:10]) = ",len(str2[2:10]),'\n')
print("length of len(str2[5:25]) = ",len(str2[5:25]),'\n')
print("length of len(str2[-11:-1]) = ",len(str2[-11:-1]),'\n')
print("length of len(str2[-25:-5]) = ",len(str2[-25:-5]),'\n')




# for set
s1 = {1,3,2,566,"haider",90+97j,3.655,'naeem',"hanzala"}
s2 = {1,45,344,90,-9049,393993}
s3 = {'tdf','cdfe','ahde','aavk','ziue','wyet'}

print("length of s1 = ",len(s1),'\n')
print("length of s2 = ",len(s2),'\n')
print("length of s3 = ",len(s3),'\n')




# for tuple
tp1 = (1,2,3,2,'haider','hanzala',9-45j,'haider')
tp2 = (34.34,123.0,232.565,789.433)
tp3 = ('wad','ajh','aafre','yakf')

print("length of tp1 = ",len(tp1),'\n')
print("length of tp2 = ",len(tp2),'\n')
print("length of tp3 = ",len(tp3),'\n')




# for dict, in this, it gives no. of keys
dict1 = {'a':1,'b':2,'c':3,'d':4}
dict2 = {'name':'haider','class':"10th B","""subject""":'PCM'}
dict3 = {'subject' : ['physics','math','chemistry'],'abcd':{100:'a',200:'b',300:'c'},
         'teachers':{'sudhanshu','sanket','vishwamohan','nitin','kirish','vishwamohan','haider'}}

print("length of dict1 = ",len(dict1),'\n')
print("length of dict2 = ",len(dict2),'\n')
print("length of dict3 = ",len(dict3),'\n')