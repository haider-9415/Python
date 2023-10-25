""" 
    filter(function,iterable) --> it checks each element of the iterable fulfils the condition of the function or not
    remember filter() accept all elements of a sequence that are true for the given functon
    and map() applies the functionality of the given function on each element of the sequence 
"""




# for list
l11 = [203,202,-22,-22,-2929,21,-12021,]

""" we have to get +ve no. from l11 """

""" using loop """
list2 = []
print("using loop: ")
for i in l11:
    if i > 0: list2.append(i)
print("    list2 --> ",list2)

""" using filter(), we can do this easly """
print("using filter(): ")
def only_posit(n):
    if n > 0 : return n
print("    l11 --> ",list(filter(only_posit,l11)))

""" it gives a filter object and we have to convert it into list, tuple or set """
def for_even(n):
    if n%2 == 0: return n
print("filter(for_even,[1,2,3,4,5,6,7,8,9,10] --> ",filter(for_even,[1,2,3,4,5,6,7,8,9,10]))
print("type(filter(for_even,[1,2,3,4,5,6,7,8,9,10])) --> ",type(filter(for_even,[1,2,3,4,5,6,7,8,9,10])))
print("list(filter(for_even,[1,2,3,4,5,6,7,8,9,10])) --> ",list(filter(for_even,[1,2,3,4,5,6,7,8,9,10])),'\n')
def for_odd(n):
    if n%2 != 0: return n
print("filter(for_odd,[1,2,3,4,5,6,7,8,9,10] --> ",filter(for_odd,[1,2,3,4,5,6,7,8,9,10]))
print("type(filter(for_odd,[1,2,3,4,5,6,7,8,9,10])) --> ",type(filter(for_odd,[1,2,3,4,5,6,7,8,9,10])))
print("tuple(filter(for_odd,[1,2,3,4,5,6,7,8,9,10])) --> ",tuple(filter(for_odd,[1,2,3,4,5,6,7,8,9,10])),'\n')
def for_mult_2_3(n):
    if n%2==0 and n%3==0: return n
print("filter(for_mult_2_3,[1,2,4,3,9,7,8,24,30,45,18] --> ",filter(for_mult_2_3,[1,2,4,3,9,7,8,24,30,45,18]))
print("type(filter(for_mult_2_3,[1,2,4,3,9,7,8,24,30,45,18])) --> ",type(filter(for_mult_2_3,[1,2,4,3,9,7,8,24,30,45,18])))
print("set(filter(for_mult_2_3,[1,2,4,3,9,7,8,24,30,45,18])) --> ",set(filter(for_mult_2_3,[1,2,4,3,9,7,8,24,30,45,18])),'\n') 

""" we can use also loop to print a filter object, because, that is also an iterable object """
print("using loop: ")
var1 = filter(only_posit,[19,202,-293,200,2,-293,-229])
for i in var1:
    print(i,end=',')
print('\n')

""" write a program to find who is the eligible person to vote and who is not using filter function """
dict1 = {12:'a',45:'b',18:'c',15:'d',60:'e',10:'f'}
print("tell who is the eligible person to vote from the following, their ages have been mentioned")
print(dict1)
print("..............................................................................................")
def eligibility(n):
    if n>18: return n
per_eli_vote = filter(eligibility,dict1.keys())
print("the persons eligible to vote are",end=': ')
for i in per_eli_vote:
    print(dict1[i],end=',') # we can print the person names easly, therefore, we have made person names as values
print("\n.............................................................................................. \n")

""" using lambda function """
seq = [92,3292302,2023,1034,23923,93292,1294,39237,32823,32946]
even = list(filter(lambda x:x%2==0,seq))
print("even --> ",even,'\n')
odd = list(filter(lambda x:x%2!=0,seq))
print("odd --> ",odd,'\n')

""" if we take None as function then it will not accept those which boolean values are zero like false none & 0 """
seq1 =  [1,'1',0,'0',False,True,None,'haider','@#$']
print("list(filter(None,seq1)) --> ",list(filter(None,seq1)),'\n')


""" find square root of a no. using filter and map functions """
# we will import math module
import math as m
# in math module, sqrt() is a function that finds square root of +ve integers only
print("m.sqrt(9) --> ",m.sqrt(9))
print("m.sqrt(9) --> ",m.sqrt(3),'\n')
# print("m.sqrt(9) --> ",m.sqrt(-9)) # it will give run time error, because, input is -ve
# if there is a -ve no. then what will we do ?
# Therefore, we will use filter and map functions
seq2 = [4,9,16,-25,49,-3,2]
def search_posi(n):
    if n>=0: return n
filtered = filter(search_posi,seq2) # to remove -ve numbers
maped = map(m.sqrt,filtered) # to find squar root of +ve numbers
print("square root: ")
print('    using multiple lines: ',list(maped))

# we can do this in single line
print("    using single line",end=': ')
print(list ( map ( m.sqrt, filter( lambda n:n>=0, [4,9,16,-25,49,-3,2] ) ) ), '\n')




# for string

""" to remove 'a','d','e','k' and 'w' from a string"""
def remove_char(n):
    characters = ['a','d','e','k','w']
    if n not in characters: return n
str8 = 'abcdefghijklmnopqrstuvwxyz'
print("filter(fing_char,str8) --> ",filter(remove_char,str8))
print("list(filter(fing_char,str8)) --> ",list(filter(remove_char,str8)),'\n')

""" to remove 'a' from a string"""
def remove_a(n):
    if n != 'a': return n
str9 = 'hanzala'
print("filter(remove_a,str9) --> ",filter(remove_a,str9))
print("list(filter(remove_a,str9)) --> ",list(filter(remove_a,str9)),'\n')

""" to find vowels in a string"""
def find_vow(n):
    vowels = ['a','e','i','o','u']
    if n in vowels: return n
str110 = 'ajsoedndjeownabdwowna'
print("filter(find_vow,str10) --> ",filter(find_vow,str110))
print("list(filter(find_vow,str10)) --> ",list(filter(find_vow,str110)),'\n')

