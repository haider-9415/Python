
"""
    getting some elements out of an existing array and creating a new
    array is called filtering

    we will do it on the basis of condition, if any element fullfil the
    given condition then it becomes the element of a new array

    if we want to get elements at specific indices then we create an list
    having boolean values and place True at those indices in the list
"""

import numpy as np

# if we want to get elements at indices 1, 2, 4, 5 & 9, i.e., elements 2, 3, 5, 6 & 10
arr1 = np.array((1,2,3,4,5,6,7,8,9,10))
filter1 = [False, True, True, False, True, True, False, False, False, True]

result1 = arr1[filter1]
print('result1 --> ',result1)
print('type(result1) --> ',type(result1))
print('\n.........................................................\n')


# if we want even numbers only 
arr2 = np.array((1,2,3,4,5,6,7,8,9,10))
filter2 = []
for element in arr2:
    if element%2 == 0:
        filter2.append(True)
    else: filter2.append(False)

result2 = arr2[filter2]
print('result2 --> ',result2)
print('type(result2) --> ',type(result2))
print('filter2 --> ',filter2)
print('\n.........................................................\n')


# if we want all elements starting with 'a' 
arr3 = np.array(['a','b','abd','dca','dac','asdwerefaaaf','wewdaa'])
filter3 = []
for element in arr3:
    if element[0] == 'a':
        filter3.append(True)
    else: filter3.append(False)

result3 = arr3[filter3]
print('result3 --> ',result3)
print('type(result3) --> ',type(result3))
print('filter3 --> ',filter3)
print('\n.........................................................\n')


""" we can do it without using loop """
# to get evem numbers
arr4 = np.array((1,2,3,4,5,6,7,8,9,10))
filter4 = arr4%2 == 0
result4 = arr4[filter4]
print('result4 --> ',result4)
print('type(result4) --> ',type(result4))
print('filter4 --> ',filter4)
print('\n.........................................................\n')


""" we can use list comprehension """
# to get elements starting with 'a'
arr5 = np.array(['a','b','abd','dca','dac','asdwerefaaaf','wewdaa'])
filter5 = [True if elm[0]=='a' else False for elm in arr5]
result5 = arr5[filter5]
print('result5 --> ',result5)
print('type(result5) --> ',type(result5))
print('filter5 --> ',filter5)
print('\n.........................................................\n')


