import numpy as np

# array[start : stop : step], the index that 'stop' holds is not counted


""" +ve slicing """
arr1 = np.array(['a','b',1,2,3,100,None])
print('arr1[1] --> ',arr1[1], '\n')
print('arr1[5] --> ',arr1[5], '\n')
print('arr1[1:5] --> ',arr1[1:5], '\n')

# to count 5th index
print('arr1[1:5+1] --> ',arr1[1:5+1], '\n')
# or
print('arr1[1:6] --> ',arr1[1:6], '\n')

# to get all values after ith index
print('arr1[3:] --> ',arr1[3:], '\n')

# to get all values up to ith index from starting
print('arr1[:6] --> ',arr1[:6], '\n')



""" -ve slicing """
print('arr1[-5:-1] --> ',arr1[-5:-1], '\n')

print('arr1[-5:] --> ',arr1[-5:], '\n')


""" step --> it creates gaps between elements it works like 'end' """
arr2 = np.array([1,2,3,4,5,6,7,8,9,10])

print('arr2[0:8:1] --> ',arr2[0:8:1], '\n')

print('arr2[0:8:2] --> ',arr2[0:8:2], '\n')

print('arr2[0::2] --> ',arr2[0::2], '\n')

print('arr2[0:8:3] --> ',arr2[0:8:3], '\n')

# to reverse an array
print('arr2[::-1] --> ',arr2[::-1], '\n')
print('\n.............................................\n')



""" slicing of 2D array """
arr3 = np.array([[1,2,3,4], ['a','b','c','d']])

print('arr3[1][1:4] --> ',arr3[1][1:4], '\n')
# or
print('arr3[1, 1:4] --> ',arr3[1, 1:4], '\n')

print('arr3[0][:4:2] --> ',arr3[0][:4:2], '\n')

print('arr3[0, :4:2] --> ',arr3[0, :4:2], '\n')

print('arr3[0, 0:4:2] --> ',arr3[0, 0:4:2], '\n')

print('arr3[0, ::-1] --> ',arr3[0, ::-1], '\n')

print('arr3[-1, ::-1] --> ',arr3[-1, ::-1], '\n')

# to get elements at 2nd index from 2 rows of arr2
print('arr3[0:2, 2] --> ',arr3[0:2, 2], '\n') # it will return '3' from 0th row and 'c' from 1st row of arr2
# similarly you can get array of elements at ith index from 'n' rows of an array
# we can using slicing to get values. in this case it returns 2D arrary
print('arr3[0:2, 1:3] --> ',arr3[0:2, 1:3], '\n')


 

arr4 = np.array([[[1,2,3,4], ['a','b','c','d']],
                   [[5,6,7,8], ['e','f','g','h']]])

print('arr4[1][1:4] --> ',arr4[1][1][1:4], '\n')

print('arr4[1][1:4] --> ',arr4[1, 1 ,1:4], '\n')

print('arr4[1][1:4] --> ',arr4[1, 0 ,1:3], '\n')

print('arr4[1][1:4] --> ',arr4[0, 0 ,::2], '\n')

print('arr4[1][1:4] --> ',arr4[0, 1 ,::2], '\n')

# in this also, we can get elements from different arrays
print('arr4[1][1:4] --> ',arr4[0, 0:2 ,3], '\n')

print('arr4[1][1:4] --> ',arr4[1, 0:2 ,2], '\n')

print('arr4[1][1:4] --> ',arr4[0:2, 1 ,3], '\n')

print('arr4[1][1:4] --> ',arr4[0:2, 0 ,1], '\n')

print('arr4[1][1:4]\n',arr4[0:2, 0:2 ,2], '\n')

print('arr4[1][1:4]\n',arr4[0:2, 0:2 ,0], '\n')

print('arr4[1][1:4]\n',arr4[0:2, 0:2 ,1:3], '\n')

print('arr4[1][1:4]\n',arr4[0:2, 0:2 ,0:3], '\n')

print('arr4[1][1:4]\n',arr4[0:2, 0:2 ,2:3], '\n')

print('\n.............................................\n')



