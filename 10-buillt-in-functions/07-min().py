# min(two iterables,*iterables,key,default) --> to find min.

""" we can find min. value among two or more non-iterable object """
print("min(384,293) --> ",min(384,293))
print("min(20,383,3928,392) --> ",min(20,383,3928,392),'\n')
n_i = [10,20,30,40,50,60]
print("min(n_i) --> ",min(n_i),'\n')




# for string
str1 = 'haider'
str2 = 'this is the lecture to know the in-built functions of string '
str3 = 'HANZALA'
str4 = 'Naeem'

""" in string, min. is found according to unicode value """
# we can pass single string, in this case, which element has min. unicode value that is min.
s6 = 'hdubetr'
print("min(s6) --> ",min(s6),'\n') # it will give 'b', because, it has min. unicode value

""" we can pass multiple strings, in this case, it compares strings and if unicode value of ith index of string 's' is min. then it will return string 's' """
print("min('sje','sowkw','Zjsi') --> ",min('sje','sowkw','Zjsi'),'\n') # it will give 'Zjsi', because, it has min. unicode value
print("min(str1,str3,str4) --> ",min(str1,str3,str4),'\n') # it will give 'str3', because, 'H',in str3, has min. unicode value
print("min(str1,str2) --> ",min(str2,str1),'\n') # it will give 'str1', because, 'h' has min. unicode value

""" if we have to find min. according to our directions, we use key attribute """
# if we have to find min. based on length then
print("min(str1,str3,str4,key=len) --> ",min(str1,str3,str4,key=len),'\n')
# if we have to find min. avoiding -ve sign
print("min(293,292,-192,929,-1,-29,920,key=abs) --> ",min(293,292,-192,929,-1,-29,920,key=abs),'\n') # avoiding -ve sign, '1' is min.

""" on giving empty string, we use default attribute to avoid error """
# # it will give error, because, s7 is empty and not proceed 
# s7 = ""
# print("min(s7) --> ",min(s7))
# print("abcd")

# the following will not give error, because, we have used default attribute and proceed
# remember, default attribute can be used with single string only
s7 = ""
print("min(s7) --> ",min(s7,default="s7 is empty string"))
print("abcd\n") # it will execute
# on finding min. between empty string and non empty string, there is no error and it will give empty string as min.
print("min(s7,'abcd') --> ",min(s7,'abcd'),'\n')




# for list
# in case of list, min() works if all elements belong to same data type 
l1 = [43,5,4,6,6,5,433,0,-445,-344,1,-1]
l2 = ['ab','ae','ac','ad']
l3 = [1,2,3,'a','b','f']

""" we can pass single list """
print("min(l1) --> ",min(l1),'\n')
print("min(l2) --> ",min(l2),'\n')
# print("min(l3) --> ",min(l3),'\n') # it will give run time error, because, all elements do not belong to the same data type
# but decimal and float can be compared
print("[1,2,3,43.5,43.5,43,3] --> ",min([1,2,3,43.5,43.5,43,3]))

# in case of numbers, it compares them as we do
print("min([1,2,3,4,5,6,7,8,9,10]) --> ",min([1,2,3,4,5,6,7,8,9,10]),'\n')
print("min([1.5,273.29,8238.032,8283.823]) --> ",min([1.5,273.29,8238.032,8283.823]),'\n')
print("min([20//4,60//3,40//5]) --> ",min([20//4,60//3,40//5]),'\n')
# remember min() does not work with complex numbers
# print("min([10-10j,20+5j,60-7j,90+1j]) --> ",min([10-10j,20+5j,60-7j,90+1j]),'\n')


""" we can pass multiple lists """
# if all elements are numbers then it will return the list having lowest ith element
l4 = [1,3,5,7,9]; l5 = [2,4,6,8]; l6 = [10,1,0]
print("min(l4,l5) --> ",min(l4,l5),'\n') # it will return l4, because, 1 < 2
print("min(l6,l5) --> ",min(l6,l5),'\n') # it will return l5, because, 2 < 10

# if all elements are strings then it will return the list which ith element comes after the corresponding ith elements of other list
l7 = ['a','b','c','z']; l8 = ['a','b','c','d']; l9 = ['aa','lb','ac','za']; l10 = ['aa','ab','fa','zz']
print("min(l7,l8) --> ",min(l7,l8),'\n') # it will return l8, because, 'd' comes before 'z'
print("min(l9,l10) --> ",min(l9,l10),'\n') # it will return l10, because, 'ab' comes before 'lb'

""" if we have to find min. according to our directions, we use key attribute """
# if we have to find min. based on length then
print("min(l4,l5,l6,key=len) --> ",min(l4,l5,l6,key=len),'\n')
# if we have to find min. avoiding -ve sign
print("min([293,292,-192,-929,-1,-29,920],key=abs) --> ",min([293,292,-192,-929,-1,-29,920],key=abs),'\n') # avoiding -ve sign, '1' is min.

""" on giving empty list, it gives run time error """
# l11 = []
# print("min(l11) --> ",min(l11))
# print("abcd")

""" to svoiding this, we use default attribute"""
# the following will not give error, because, we have used default attribute and will proceed
# remember, default attribute can be used with single list only
l12 = []
print("min(l12) --> ",min(l12,default="l12 is empty string"))
print("abcd\n") # it will execute
# on finding min. between empty list and non empty list, there is no error and it will give empty list as min.
print("min(l12,[1,2,3,4]) --> ",min(l12,[1,2,3,4]),'\n')




# for tuple
# in case of tuple, min() works if all elements belong to same data type 
t1 = (43,5,4,6,6,5,433,0,-445,-344,1,-1)
t2 = ('ab','ae','ac','ad')
t3 = (1,2,3,'a','b','f')

""" we can pass single tuple """
print("min(t1) --> ",min(t1),'\n')
print("min(t2) --> ",min(t2),'\n')
# print("min(t3) --> ",min(t3),'\n') # it will give run time error, all elements do not belong to the same data type
# but decimal and float can be compared
print("min((1,2,3,43.5,43.6,43,3)) --> ",min((1,2,3,43.5,43.6,43,3)))

# in case of numbers, it compares them as we do
print("min((1,2,3,4,5,6,7,8,9,10)) --> ",min((1,2,3,4,5,6,7,8,9,10)),'\n')
print("min((1.5,273.29,8238.032,8283.823)) --> ",min((1.5,273.29,8238.032,8283.823)),'\n')
print("min((20//4,60//3,40//5)) --> ",min((20//4,60//3,40//5)),'\n')
# remember min() does not work with complex numbers
# print("min((10-10j,20+5j,60-7j,90+1j)) --> ",min((10-10j,20+5j,60-7j,90+1j)),'\n')


""" we can pass multiple tuple """
# if all elements are numbers then it will return the tuple having greatest ith element
t4 = (1,3,5,7,9); t5 = (2,4,6,8); t6 = (10,1,0)
print("min(t4,t5) --> ",min(t4,t5),'\n') # it will return t4, because, 1 < 2
print("min(t6,t5) --> ",min(t6,t5),'\n') # it will return t5, because, 2 < 10

# if all elements are strings then it will return the tuple which ith element comes after the corresponding ith elements of other tuple
t7 = ('a','b','c','z'); t8 = ('a','b','c','d'); t9 = ('aa','lb','ac','za'); t10 = ('aa','ab','fa','zz')
print("min(t7,t8) --> ",min(t7,t8),'\n') # it will return t7, because, 'd' comes before 'z'
print("min(t9,t10) --> ",min(t9,t10),'\n') # it will return t10, because, 'ab' comes befor 'lb'

""" if we have to find min. according to our directions, we use key attribute """
# if we have to find min. based on length then
print("min(t4,t5,t6,key=len) --> ",min(t4,t5,t6,key=len),'\n')
# if we have to find min. avoiding -ve sign
print("min((293,292,-192,-929,-1,-29,920),key=abs) --> ",min((293,292,-192,-929,-1,-29,920),key=abs),'\n') # avoiding -ve sign, '1' is min.

""" on giving empty tuple, it gives run time error """
# t11 = ()
# print("min(t11) --> ",min(t11))
# print("abcd")

""" to svoiding this, we use default attribute"""
# the following will not give error, because, we have used default attribute and will proceed
# remember, default attribute can be used with single string only
t12 = ()
print("min(t12) --> ",min(t12,default="t12 is empty string"))
print("abcd\n") # it will execute
# on finding min. between empty tuple and non empty tuple, there is no error and it will give empty tuple as min.
print("min(t12,(1,2,3,4)) --> ",min(t12,(1,2,3,4)),'\n')




# for set
# in case of set, min() works if all elements belong to same data type 
s1 = {43,5,4,6,6,5,433,0,-445,-344,1,-1}
s2 = {'ab','ae','ac','ad'}
s3 = {1,2,3,'a','b','f'}

""" we can pass single set """
print("min(s1) --> ",min(s1),'\n')
print("min(s2) --> ",min(s2),'\n')
# print("min(s3) --> ",min(s3),'\n') # it will give run time error, all elements do not belong to the same data type
# but decimal and float can be compared
print("min((1,2,3,43.5,43.6,43,3)) --> ",min((1,2,3,43.5,43.6,43,3)))

# in case of numbers, it compares them as we do
print("min({1,2,3,4,5,6,7,8,9,10}) --> ",min({1,2,3,4,5,6,7,8,9,10}),'\n')
print("min({1.5,273.29,8238.032,8283.823}) --> ",min({1.5,273.29,8238.032,8283.823}),'\n')
print("min({20//4,60//3,40//5}) --> ",min({20//4,60//3,40//5}),'\n')
# remember min() does not work with complex numbers
# print("min({10-10j,20+5j,60-7j,90+1j}) --> ",min({10-10j,20+5j,60-7j,90+1j}),'\n')


""" we can pass multiple sets """
# if all elements are numbers then it will return the list having greatest ith element
s4 = {1,3,5,7,9}; s5 = {2,4,6,8}; s6 = {10,1,0}
print("min(s4,s5) --> ",min(s4,s5),'\n') # it will return s4, because, 1 < 2
print("min(s6,s5) --> ",min(s6,s5),'\n') # it will return s5, because, 2 < 10

# if all elements are strings then it will return the set which ith element comes after the corresponding ith elements of other set
s7 = {'a','b','c','z'}; s8 = {'a','b','c','d'}; s9 = {'aa','lb','ac','za'}; s10 = {'aa','ab','fa','zz'}
print("min(s7,s8) --> ",min(s7,s8),'\n') # it will return t7, because, 'd' comes before 'z'
print("min(s9,s10) --> ",min(s9,s10),'\n') # it will return t10, because, 'ab' comes befor 'lb'

""" if we have to find min. according to our directions, we use key attribute """
# if we have to find min. based on length then
print("min(s4,s5,s6,key=len) --> ",min(s4,s5,s6,key=len),'\n')
# if we have to find min. avoiding -ve sign
print("min({293,292,-192,-929,-1,-29,920},key=abs) --> ",min({293,292,-192,-929,-1,-29,920},key=abs),'\n') # avoiding -ve sign, '1' is min.

""" on giving empty list, it gives run time error """
# s11 = {}
# print("min(s11) --> ",min(s11))
# print("abcd")

""" to svoiding this, we use default attribute"""
# the following will not give error, because, we have used default attribute and will proceed
# remember, default attribute can be used with single set only
s12 = {}
print("min(s12) --> ",min(s12,default="s12 is empty string"))
print("abcd\n") # it will execute
# we know an empty {} is a dictionary so we can not compare empty {} and a set, it will give run time error and min() does not work with dictionary
# both of the following will give run time error
# print("min(s12,{1,2,3,4}) --> ",min(s12,{1,2,3,4}))
# print(min(s12,{1:'a',2:'b'}))


