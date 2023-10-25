# type-3 --> list
lt1 = [2,'lucknow',109.5,"9787",3+7j]
lt2 = ["haider","hanzala","hanzala",'naeem']
lt3 = [1+2+3+4+5+6+7+8+9,"~`#<>?|:;.,"]
lt4 = [123456789123456789]

print("lt1 --> ",lt1)
print(lt1[0]);print(lt1[1]);print(lt1[2]);print(lt1[3]);print(lt1[4])
print(lt1[1][0]);print(lt1[1][1]);print(lt1[1][2]);print(lt1[1][3]);print(lt1[1][4]);print(lt1[1][5]);print(lt1[1][6])
print(".....................................................................\n\n")
print("lt2 --> ",lt2)
print(lt2[0]);print(lt2[1]);print(lt2[2]);print(lt2[3])
print(lt2[0][0]);print(lt2[0][1]);print(lt2[0][2]);print(lt2[0][3]);print(lt2[0][4]);print(lt2[0][5])
print(".....................................................................\n\n")
print("lt3 --> ",lt3)
print(lt3[0]);print(lt3[1])
print(".....................................................................\n\n")
print("lt4 --> ",lt4)
print(lt4[0])
print(".....................................................................\n\n")
print(type(lt1))
print(type(lt2))
print(type(lt2))
print(type(lt4))
print(isinstance(lt1,list))
print(isinstance(lt2,list))
print(isinstance(lt2,list))
print(isinstance(lt4,list))
print(".....................................................................\n\n")

""" we can change any value in list at an index, therefore, the list is 
    called 'mutable'.
    But we can not change any value in a string at an index, therefore,
    the string is called 'immutable' """
lt1[0] = 'hanzala' # it will remove 2 at 0th index from 'hanzala' in lt1
print("lt1[0] = 'hanzala' -->",lt1)
lt2[1] = 'delhi' # it will remove 'hanzala' at 1st index from 'delhi' in lt2
print("lt2[1] = 'delhi' -->",lt2)

# str = 'hanzala'
# str[3] = 'f' # it will give run time error,because, it is a string not a list
# print(str)
print(".....................................................................\n\n")

""" if we multiply a list by 'x' then the data in the list repeats
    'x' times """
l = [1,3,2.44,'haider',True]
print("after 'l' mult. by 2")
print(l*2)
print("after 'l' mult. by 3")
print(l*3)
print("after 'l' mult. by 5")
print(l*5)
print(".....................................................................\n\n")

""" we can add tow or more lists """
l1 = [1,2,3,'abcd']
l2 = [2.3,23+1j,92-90j ,'haider']
l3 = ['hanzala','efgh','ijkl']
print("l1+l2 -->",l1+l2)
print("l3+l2 -->",l3+l2)
print("l1+l3+l2 -->",l1+l3+l2)
print("l1+l2+l3 -->",l1+l2+l3)
print(".....................................................................\n\n")

""" we can add elements of different lists """
print("l1[3]+l3[3]+l2[1] -->",l1[3]+l2[3]+l3[1])
# # both of the following give run time error,because,a data type can not be added with another data type
# print("l3[2]+l2[2]+l1[3] -->",l3[2]+l2[2]+l1[3])
# print("l2[0]+l3[1]+l2[2] -->",l2[0]+l3[1]+l2[2]) 
print(".....................................................................\n\n")

""" we can make a list of lists, remember, each list will be an element of that list """
l4 = [lt1,lt2,l3]
print('l4 -->',l4)
l5 = [lt3,l2,l1,lt4,8774,'haider']
print('l5 -->',l5)
l6 = [lt1,lt2,lt3,lt4,l,l1,l2,l3]
print('l6 -->',l6)
print(".....................................................................\n\n")



""" types of list """
# 1) empty list --> [] or list() could be used to creat an empty list
l7 = []
print("l7 --> ",l7)
print("type(l7) --> ",type(l7))
l8 = list()
print("l8 --> ",l8)
print("type(l8) --> ",type(l8))
print(".....................................................................\n\n")

# 2) long list --> a list containing multiple lines is called long list
l9 = [1,2,3,4,5,'a','b','c','d','e',
      6,7,8,9,10,'!','@','#','%','&'
      ,84-93j,73+0j,True,False]
print("l9 --> ",l9)
print("type(l9) --> ",type(l9))
print(".....................................................................\n\n")

# 3) nested list --> if element of a list is itself a list then it is called nested list
l10 = [1,2,3,4,[10,20,30,'a','b','c','d'],True,False]
print("l10 --> ",l10)
print("type(l10) --> ",type(l10))
l11 = [1,[2,[3,[4,[5,[6,[7,[8,[9,[10,[11,[12,[13,[14,[[15],16],17],18],19],20],21],22],23],24],25],26],27],28],29],30]
print("l11 --> ",l11)
print("type(l11) --> ",type(l11))
print(".....................................................................\n\n")

# 4) list from sequences
t = (1,2,3,4,5,6)
l12 = [t] # in this, (1,2,3,4,5,6) is the element of l12
print("l12 --> ",l12)
print("type(l12) --> ",type(l12))
l13 = list(t) # in this, elements of (1,2,3,4,5,6) are the elements of l13
print("l13 --> ",l13)
print("type(l13) --> ",type(l13))

s = {1,2,3,4,5,6}
l14 = [s] # in this, {1,2,3,4,5,6} is the element of l14
print("l14 --> ",l14)
print("type(l14) --> ",type(l14))
l15 = list(s) # in this, elements of {1,2,3,4,5,6} are the elements of l15
print("l15 --> ",l15)
print("type(l15) --> ",type(l15))

d = {1:'a',2:'b',3:'c'}
l16 = [d] # in this, {1:'a',2:'b',3:'c'} is the element of l16
print("l16 --> ",l16)
print("type(l16) --> ",type(l16))
l17 = list(d) # in this, keys of {1:'a',2:'b',3:'c'} are the elements of l17
print("l17 --> ",l17)
print("type(l17) --> ",type(l17))

str = "abcd1234#$%^"
l18 = [str] # in this, "abcd1234#$%^" is the element of l18
print("l18 --> ",l18)
print("type(l18) --> ",type(l18))
l19 = list(str) # in this, characters of "abcd1234#$%^" are the elements of l19
print("l19 --> ",l19)
print("type(l19) --> ",type(l19))
print(".....................................................................\n\n")

""" an empty list is equivalent to zero, False or empty string """
if []: # if [] is equivalent to True then if-statement will  execute otherwise else-statement will execute
    print("you can see that [] is not eqivalent to False")
else:
    print("you can see that [] is eqivalent to False",'\n')
if list(): # if list() is equivalent to True then if-statement will  execute otherwise else-statement will execute
    print("you can see that list() is not eqivalent to False")
else:
    print("you can see that list() is eqivalent to False",'\n')
print(".....................................................................\n\n")


""" we can add elements in a list at specific indeces using slices 
    syntex -->  list_name[start:stop] = sequence(like string,tuple,set,ets.)
"""
l20 = [1,2,3,4,5,6,7,8,9,10]
print("before modification: l20 --> ",l20)
l20[2:6] = "abcd"
print("after modification: l20 --> ",l20)
l20[-2:-8] = ('e','f','g','h','i','j','k','l','m')
print("after modification: l20 --> ",l20)
print(".....................................................................\n\n")


""" creation a copy of a list """
list1 = [1,2,3,4,5,6]
list2 = list1
list2[2] = 10
print("list1 --> ",list1);print("list2 --> ",list2,'\n') # since 10 is being updated in both list1 & list2 therefore it is not a copying process
print(".....................................................................\n\n")
# to create a copy of a list, we use list(), list_name.copy(), storing all elements using slicing
print("using list()")
list3 = [1,2,3,4,5,6]
list4 = list(list3)
list4[2] = 10
print("list3 --> ",list3);print("list4 --> ",list4,'\n') # since 10 is being updated in list4 only therefore it is a copying process
print("using list_name.copy()")
list5 = list3.copy()
list5[0] = 20
print("list3 --> ",list3);print("list5 --> ",list5,'\n') # since 20 is being updated in list5 only therefore it is a copying process
print("using slicing")
list6 = list3[::-1]
list6[5] = 50
print("list3 --> ",list3);print("list6 --> ",list6,'\n') # since 50 is being updated in list6 only therefore it is a copying process
print(".....................................................................\n\n")