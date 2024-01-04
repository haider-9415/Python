"""
    we can the change of array like adding or removing 
    the elements

    we use reshape()

    we have to know its length
"""

import numpy as np

# reshaping from 1D to 2D
arr1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
reshape1_arr1 = arr1.reshape(4, 3)
# it means breake arr1 in four sub arrays and each array has 3 elements
print('arr1 -->',arr1)
print('reshape1_arr1:\n',reshape1_arr1)
print('arr1.ndim -->',arr1.ndim)
print('reshape1_arr1.ndim -->',reshape1_arr1.ndim)
print('arr1.shape -->',arr1.shape)
print('reshape1_arr1.shape -->',reshape1_arr1.shape)
print('\n....................................................\n')

# similarly
arr1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
reshape2_arr1 = arr1.reshape(2, 6)
# it means breake arr1 in two sub arrays and each array has 6 elements
print('arr1 -->',arr1)
print('reshape2_arr1:\n',reshape2_arr1)
print('arr1.shape -->',arr1.shape)
print('reshape2_arr1.shape -->',reshape2_arr1.shape)
print('\n....................................................\n')



# reshaping from 1D to 3D
arr1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
reshape3_arr1 = arr1.reshape(2, 3, 2)
# it means breake arr1 has 2 elements & each of them has three & then each of them has two elements
print('arr1 -->',arr1)
print('reshape3_arr1:\n',reshape3_arr1)
print('arr1.ndim -->',arr1.ndim)
print('reshape3_arr1.ndim -->',reshape3_arr1.ndim)
print('arr1.shape -->',arr1.shape)
print('reshape3_arr1.shape -->',reshape3_arr1.shape)
print('\n....................................................\n')

arr1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
reshape4_arr1 = arr1.reshape(2, 2, 3)
print('arr1 -->',arr1)
print('reshape4_arr1:\n',reshape4_arr1)
print('arr1.ndim -->',arr1.ndim)
print('reshape4_arr1.ndim -->',reshape4_arr1.ndim)
print('arr1.shape -->',arr1.shape)
print('reshape4_arr1.shape -->',reshape4_arr1.shape)
print('\n....................................................\n')



# if you have to reshape 1D into 2D, give -1 as 2nd parameter, it will reshape it
arr1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
reshape5_arr1 = arr1.reshape(2, -1)
print('arr1 -->',arr1)
print('reshape5_arr1:\n',reshape5_arr1)
print('arr1.ndim -->',arr1.ndim)
print('reshape5_arr1.ndim -->',reshape5_arr1.ndim)
print('arr1.shape -->',arr1.shape)
print('reshape5_arr1.shape -->',reshape5_arr1.shape)
print('\n....................................................\n')

# if you have to reshape 1D into #D, give -1 as 3rd parameter, it will reshape it
arr1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
reshape6_arr1 = arr1.reshape(2, 2, -1)
print('arr1 -->',arr1)
print('reshape6_arr1:\n',reshape6_arr1)
print('arr1.ndim -->',arr1.ndim)
print('reshape6_arr1.ndim -->',reshape6_arr1.ndim)
print('arr1.shape -->',arr1.shape)
print('reshape6_arr1.shape -->',reshape6_arr1.shape)
print('\n....................................................\n')



# reshaping from 2D to 1D
arr2 = np.array([[1,2,3,4], ['a','b','c','d'], [5,6,7,8]])
reshape7_arr1 = arr2.reshape(-1)
print('arr2:\n',arr2)
print('reshape7_arr1 -->',reshape7_arr1)
print('arr2.ndim -->',arr2.ndim)
print('reshape7_arr1.ndim -->',reshape7_arr1.ndim)
print('arr2.shape -->',arr2.shape)
print('reshape7_arr1.shape -->',reshape7_arr1.shape)
print('\n....................................................\n')



# reshaping from 3D to 1D
arr3 = np.array([[[1,2,3,4], ['a','b','c','d'], [5,6,7,8]],
                   [[-1,-2,-3,-4], ['e','f','g','h'], [-5,-6,-7,-8]]
                  ])
reshape8_arr1 = arr3.reshape(-1)
print('arr3:\n',arr3)
print('reshape8_arr1:\n',reshape8_arr1)
print('arr3.ndim -->',arr3.ndim)
print('reshape8_arr1.ndim -->',reshape8_arr1.ndim)
print('arr3.shape -->',arr3.shape)
print('reshape8_arr1.shape -->',reshape8_arr1.shape)
print('\n....................................................\n')


"""
    there are alot of functions to for reshaping like flatten, ravel, rot90, flip, fliplr, flipud.
"""