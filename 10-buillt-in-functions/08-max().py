# to find max. --> max(two iterables,*iterables,key,default)

""" we can find max. value among two or more non-iterable objects """
print("max(384,293) --> ",max(384,293),'\n')
print("max(20,383,3928,392) --> ",max(20,383,3928,392),'\n')
n_i = [10,20,30,40,50,60]
print("max(n_i) --> ",max(n_i),'\n')




# for string
str1 = 'haider'
str2 = 'this is the lecture to know the in-built functions of string '
str3 = 'HANZALA'
str4 = 'Naeem'

""" in string, max. is found according to unicode value """
# we can pass single string, in this case, which character has max. unicode value that is the result
st1 = 'hdubetr'
print("max(st1) --> ",max(st1),'\n') # it will give 'u', because, it has max. unicode value
# we can pass multiple strings, in this case, it compares strings and if unicode value of ith index of string 's' is max. then it will return string 's'
print("max('sje','sowkw','Zjsi') --> ",max('sje','sowkw','Zjsi'),'\n') # it will give 'sowkw', because, 'o' has max. unicode value than 'j'
print("max(str1,str3,str4) --> ",max(str1,str3,str4),'\n') # it will give 'str1', because, 'h',in str1, has max. unicode value
print("max(str1,str2) --> ",max(str2,str1),'\n') # it will give 'str2', because, 't', in str2, has max. unicode value

""" if we have to find max. according to our directions, we use key attribute """
# if we have to find max. based on length then
print("max(str1,str3,str4,key=len) --> ",max(str1,str3,str4,key=len),'\n')
# if we have to find min. avoiding -ve sign
print("max(293,292,-192,-929,-1,-29,920,key=abs) --> ",max(293,292,-192,-929,-1,-29,920,key=abs),'\n') # avoiding -ve sign, '929' is max.

""" on giving empty string, it gives run time error """
# st2 = ""
# print("max(st2) --> ",max(st2))
# print("abcd")

""" to svoiding this, we use default attribute"""
# the following will not give error, because, we have used default attribute and will proceed
# remember, default attribute can be used with single string only
st3 = ""
print("max(st3) --> ",max(st3,default="s3 is empty string"))
print("abcd\n") # it will execute
# on finding max. between empty string and non empty string, there is no error and it will give non empty string as max.
print("max(st3,'abcd') --> ",max(st3,'abcd'),'\n')




# for list
# in case of list, mas() works if all elements belong to same data type 
l1 = [43,5,4,6,6,5,433,0,-445,-344,1,-1]
l2 = ['ab','ae','ac','ad']
l3 = [1,2,3,'a','b','f']

""" we can pass single list """
print("max(l1) --> ",max(l1),'\n')
print("max(l2) --> ",max(l2),'\n')
# print("max(l3) --> ",max(l3),'\n') # it will give run time error, all elements do not belong to the same data type
# but decimal and float can be compared
print("[1,2,3,43.5,43.5,43,3] --> ",max([1,2,3,43.5,43.5,43,3]))

# in case of numbers, it compares them as we do
print("max([1,2,3,4,5,6,7,8,9,10]) --> ",max([1,2,3,4,5,6,7,8,9,10]),'\n')
print("max([1.5,273.29,8238.032,8283.823]) --> ",max([1.5,273.29,8238.032,8283.823]),'\n')
print("max([20//4,60//3,40//5]) --> ",max([20//4,60//3,40//5]),'\n')
# remember max() does not work with complex numbers
# print("max([10-10j,20+5j,60-7j,90+1j]) --> ",max([10-10j,20+5j,60-7j,90+1j]),'\n')


""" we can pass multiple lists """
# if all elements are numbers then it will return the list having greatest ith element
l4 = [1,3,5,7,9]; l5 = [2,4,6,8]; l6 = [10,1,0]
print("max(l4,l5) --> ",max(l4,l5),'\n') # it will return l5, because, 2 > 1
print("max(l6,l5) --> ",max(l6,l5),'\n') # it will return l6, because, 10 > 2

# if all elements are strings then it will return the list which ith element comes after the corresponding ith elements of other list
l7 = ['a','b','c','z']; l8 = ['a','b','c','d']; l9 = ['aa','lb','ac','za']; l10 = ['aa','ab','fa','zz']
print("max(l7,l8) --> ",max(l7,l8),'\n') # it will return l7, because, 'z' comes after 'd'
print("max(l9,l10) --> ",max(l9,l10),'\n') # it will return l10, because, 'lb' comes after 'ab'

""" if we have to find max. according to our directions, we use key attribute """
# if we have to find max. based on length then
print("max(l4,l5,l6,key=len) --> ",max(l4,l5,l6,key=len),'\n')
# if we have to find max. avoiding -ve sign
print("max([293,292,-192,-929,-1,-29,920],key=abs) --> ",max([293,292,-192,-929,-1,-29,920],key=abs),'\n') # avoiding -ve sign, '929' is max.

""" on giving empty list, it gives run time error """
# l11 = []
# print("max(l11) --> ",max(l11))
# print("abcd")

""" to svoiding this, we use default attribute"""
# the following will not give error, because, we have used default attribute and will proceed
# remember, default attribute can be used with single list only
l12 = []
print("max(l12) --> ",max(l12,default="l12 is empty string"))
print("abcd\n") # it will execute
# on finding max. between empty list and non empty list, there is no error and it will give non empty list as max.
print("max(l12,[1,2,3,4]) --> ",max(l12,[1,2,3,4]),'\n')




# for tuple
# in case of tuple, mas() works if all elements belong to same data type 
t1 = (43,5,4,6,6,5,433,0,-445,-344,1,-1)
t2 = ('ab','ae','ac','ad')
t3 = (1,2,3,'a','b','f')

""" we can pass single tuple """
print("max(t1) --> ",max(t1),'\n')
print("max(t2) --> ",max(t2),'\n')
# print("max(t3) --> ",max(t3),'\n') # it will give run time error, all elements do not belong to the same data type
# but decimal and float can be compared
print("max((1,2,3,43.5,43.6,43,3)) --> ",max((1,2,3,43.5,43.6,43,3)))

# in case of numbers, it compares them as we do
print("max((1,2,3,4,5,6,7,8,9,10)) --> ",max((1,2,3,4,5,6,7,8,9,10)),'\n')
print("max((1.5,273.29,8238.032,8283.823)) --> ",max((1.5,273.29,8238.032,8283.823)),'\n')
print("max((20//4,60//3,40//5)) --> ",max((20//4,60//3,40//5)),'\n')
# remember max() does not work with complex numbers
# print("max((10-10j,20+5j,60-7j,90+1j)) --> ",max((10-10j,20+5j,60-7j,90+1j)),'\n')


""" we can pass multiple tuple """
# if all elements are numbers then it will return the tuple having greatest ith element
t4 = (1,3,5,7,9); t5 = (2,4,6,8); t6 = (10,1,0)
print("max(t4,t5) --> ",max(t4,t5),'\n') # it will return t5, because, 2 > 1
print("max(t6,t5) --> ",max(t6,t5),'\n') # it will return t6, because, 10 > 2

# if all elements are strings then it will return the tuple which ith element comes after the corresponding ith elements of other tuple
t7 = ('a','b','c','z'); t8 = ('a','b','c','d'); t9 = ('aa','lb','ac','za'); t10 = ('aa','ab','fa','zz')
print("max(t7,t8) --> ",max(t7,t8),'\n') # it will return t7, because, 'z' comes after 'd'
print("max(t9,t10) --> ",max(t9,t10),'\n') # it will return t10, because, 'lb' comes after 'ab'

""" if we have to find max. according to our directions, we use key attribute """
# if we have to find max. based on length then
print("max(t4,t5,t6,key=len) --> ",max(t4,t5,t6,key=len),'\n')
# if we have to find max. avoiding -ve sign
print("max((293,292,-192,-929,-1,-29,920),key=abs) --> ",max((293,292,-192,-929,-1,-29,920),key=abs),'\n') # avoiding -ve sign, '929' is max.

""" on giving empty tuple, it gives run time error """
# t11 = ()
# print("max(t11) --> ",max(t11))
# print("abcd")

""" to svoiding this, we use default attribute"""
# the following will not give error, because, we have used default attribute and will proceed
# remember, default attribute can be used with single string only
t12 = ()
print("max(t12) --> ",max(t12,default="t12 is empty string"))
print("abcd\n") # it will execute
# on finding max. between empty tuple and non empty tuple, there is no error and it will give non empty list as max.
print("max(t12,(1,2,3,4)) --> ",max(t12,(1,2,3,4)),'\n')




# for set
# in case of set, mas() works if all elements belong to same data type 
s1 = {43,5,4,6,6,5,433,0,-445,-344,1,-1}
s2 = {'ab','ae','ac','ad'}
s3 = {1,2,3,'a','b','f'}

""" we can pass single set """
print("max(s1) --> ",max(s1),'\n')
print("max(s2) --> ",max(s2),'\n')
# print("max(s3) --> ",max(s3),'\n') # it will give run time error, all elements do not belong to the same data type
# but decimal and float can be compared
print("max((1,2,3,43.5,43.6,43,3)) --> ",max((1,2,3,43.5,43.6,43,3)))

# in case of numbers, it compares them as we do
print("max({1,2,3,4,5,6,7,8,9,10}) --> ",max({1,2,3,4,5,6,7,8,9,10}),'\n')
print("max({1.5,273.29,8238.032,8283.823}) --> ",max({1.5,273.29,8238.032,8283.823}),'\n')
print("max({20//4,60//3,40//5}) --> ",max({20//4,60//3,40//5}),'\n')
# remember max() does not work with complex numbers
# print("max({10-10j,20+5j,60-7j,90+1j}) --> ",max({10-10j,20+5j,60-7j,90+1j}),'\n')


""" we can pass multiple sets """
# if all elements are numbers then it will return the list having greatest ith element
s4 = {1,3,5,7,9}; s5 = {2,4,6,8}; s6 = {10,1,0}
print("max(s4,s5) --> ",max(s4,s5),'\n') # it will return s5, because, 2 > 1
print("max(s6,s5) --> ",max(s6,s5),'\n') # it will return s6, because, 10 > 2

# if all elements are strings then it will return the set which ith element comes after the corresponding ith elements of other set
s7 = {'a','b','c','z'}; s8 = {'a','b','c','d'}; s9 = {'aa','lb','ac','za'}; s10 = {'aa','ab','fa','zz'}
print("max(s7,s8) --> ",max(s7,s8),'\n') # it will return t7, because, 'z' comes after 'd'
print("max(s9,s10) --> ",max(s9,s10),'\n') # it will return t10, because, 'lb' comes after 'ab'

""" if we have to find max. according to our directions, we use key attribute """
# if we have to find max. based on length then
print("max(s4,s5,s6,key=len) --> ",max(s4,s5,s6,key=len),'\n')
# if we have to find max. avoiding -ve sign
print("max({293,292,-192,-929,-1,-29,920},key=abs) --> ",max({293,292,-192,-929,-1,-29,920},key=abs),'\n') # avoiding -ve sign, '929' is max.

""" on giving empty list, it gives run time error """
# s11 = {}
# print("max(s11) --> ",max(s11))
# print("abcd")

""" to svoiding this, we use default attribute"""
# the following will not give error, because, we have used default attribute and will proceed
# remember, default attribute can be used with single set only
s12 = {}
print("max(s12) --> ",max(s12,default="s12 is empty string"))
print("abcd\n") # it will execute
# we know an empty {} is a dictionary so we can not compare empty {} and a set, it will give run time error and max() does not work with dictionary
# print("max(s12,{1,2,3,4}) --> ",max(s12,{1,2,3,4}))
# print(max(s12,{1:'a',2:'b'}))


