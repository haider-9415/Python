"""
    shape of an array is the no. of elements in each list given in the array

    if array is 1D then it returns (m,), m = no. of elements in the array

    if array is 2D then it returns (m, n), 
    m = no. of elements in outer array & n = no. of elements in inner array
"""

import numpy as np

arr1 = np.array([1,2,3,4,5,6])
print('arr1 -->',arr1)
print('arr1.shape -->',arr1.shape)
print('\n....................................................\n')

arr2 = np.array([[1,2,3,4], ['a','b','c','d']])
print('arr2 -->',arr2)
print('arr2.shape -->',arr2.shape)
print('\n....................................................\n')

arr3 = np.array([[[1,2,3,4], ['a','b','c','d']],
                 [[5,6,7,8], ['e','f','g','h']]])
print('arr3 -->',arr3)
print('arr3.shape -->',arr3.shape)
print('\n....................................................\n')

arr4 = np.array([[[1,2,3,4], ['a','b','c','d']],
                 [[5,6,7,8], ['e','f','g','h']],
                 [[9,10,11,12], ['i','j','k','l']]])
print('arr4 -->',arr4)
print('arr4.shape -->',arr4.shape)
print('\n....................................................\n')

arr5 = np.array([[[1,2,3,4], ['a','b','c','d']],
                 [[5,6,7,8], ['e','f','g','h']],
                 [[9,10,11,12], ['i','j','k','l']]], ndmin=5)
print('arr5 -->',arr5)
print('arr5.shape -->',arr5.shape)
print('\n....................................................\n')

arr6 = np.array([1,2,3,4,5,6], ndmin=6)
print('arr6 -->',arr6)
print('arr6.shape -->',arr6.shape)
print('\n....................................................\n')

