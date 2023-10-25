""" syntax --> for i,j,etc. condition:
                   statement(s)              """
""" it knows the range of data stored in the variable """

str1 = "pwskills"

# using for loop, we will print all letters in string str1
print("elements of str1:")
for i in str1:
    print(i,end=',')
print()

# we can convert all letters in str1 in capital letters
print("elements of str1 in upper case:")
for j in str1:
    print(j.upper(),end=',')
print()



lt1 = [1,2,3,282.44,43.0,'haider','naeem',90-82j]
lt2 = [1,3,2,5,6,4,8,7,5,9483,80,93,8223,232]

# using for loop, we will print all letters in list lt1
print("elements of lt1:")
for j in lt1:
    print(j,end=',')
print()

# after adding 2 with all elements of list lt2
print("elements of lt2 after addition of 2:")
for a in lt2:
    print(a+2,end=',')
print()

# if we want all even no. in lt2
print("even elements of lt2:")
for a in lt2:
    if a%2 == 0:
        print(a,end=',')
print() 

# if we want all odd no. in lt2
print("odd elements of lt2:")
for a in lt2:
    if a%2 != 0:
        print(a,end=',')
print() 

# if we want a list 'l1' that contains only odd no. in l2
l2 = [2321,354438,90482,9329203,8493847,923903,940340,927332,83737,9832938,93065
      ,62535,73376,93489,3048533,84856,3874727,9328475,945858]
l1 = []

for i in l2:
    if i%2 != 0:
        l1.append(i)
print("l1 -->",l1)



""" make lists for each data-type present in l3 seperatly """
l3 = [12,3,32.43,4,930.0,2,'haider','naeem',177,29,'naeem',True,False,False]

l_int = []
l_str = []
l_bool = []
l_float = []

for i in l3:
    if type(i) == int:
        l_int.append(i)
    elif type(i) == str:
        l_str.append(i)
    elif type(i) == float:
        l_float.append(i)
    else:
        l_bool.append(i)

print("l3 -->",l3)
print("l_int -->",l_int)
print("l_str -->",l_str)
print("l_float -->",l_float)
print("l_bool -->",l_bool)


""" we can make a list such that """
l = [ i*i for i in range(2,21,2)]
print("l -->",l)
# it is called list comprehension
""" similarly """
x = [ i+i for i in range(2,21,2)]
print("x -->",x)

""" using loop, we can take elements of a list from user """
l4 = []
n = int(input("enter length of l4: ")) # because, input function converts input in string,so, we use int()
print("enter elements for l4 ")
for i in range (n):
    l4.append(input())
print("l4 -->",l4)


""" we can obtain elements of tuple using loop """
t1 = (1,2,33.43,32.32,23,'haider',True,'hanzala',90-2j)
print("elements of t1:")
for j in t1:
    print(j,end=',')
print()


""" similarly on dictionary """
d1 = {'name':'hanzala','subjects':['math','physics','chemistry','english','hindi','urdu'],'class':'12th','sec':'4-B'}
print("using .items():")
print(d1.items()) # it gives key-value pairs in list format

# using loop, we can obtain key-value pairs
print("using loop, key-value pairs in d1:")
for i in d1.items():
    print(i,end=',')
print()

# using loop, we can obtain only keys
print("keys in d1:")
for i in d1.keys():
    print(i,end=',')
print()

# using loop, we can obtain only values
print("values in d1:")
for i in d1.values():
    print(i,end=',')
print()

# if we want only the value that is in list format then
print("value in list format in d1:")
for i in d1.values():
    if type(i) == list:
        print(i)



# using of enumerate function --> it gives index and the character present at the index
s = 'haider'
print("s -->",s)
for index,character in enumerate(s):
    print(index,' --> ',character)

s1 = '~!@#$%^&*()_+:"?><|\\{}`,./;[]\\=-'
print("s1 -->",s1)
for index,character in enumerate(s1):
    print("element at index in s1 ",index,' is ',character)