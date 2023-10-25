""" to sort a list --> .sort(). All elements must be of same data type """


l1 = ['abc','wed','aaf','fd',1,2,3]
l2 = [23,43,65,90,776,6,54,333,45,-1,337343,-292383]
l3 = ['pwskills','coolege wallah','sudh','python']

l2.sort()
print('l2 -->',l2,'\n')

# l1.sort()
# print(l1) # it will give run time error,because, elements in l1 do not belong to same data type 

""" if we applay it on a list containing strings then it will sort it as in dictionary """
l3.sort()
print('l3 -->',l3,'\n')

""" to sort in descending order using reverse attribute """
l2.sort(reverse=True)
print('l2 -->',l2,'\n')
l3.sort(reverse=True)
print('l3 -->',l3,'\n')

