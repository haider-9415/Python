"""
    we can shuffle elements in an array

    we can use shuffle() & permutation()

    shuffle() returns None not the shuffled array, it makes changes on original array

    permutation() returns the shuffled array, it does not make changes on original array
"""

import numpy as np
from numpy import random

""" shuffling 1D array """

# using shuffle() 
arr1 = np.array([1,2,3,4,5,6,7,8,9,10])
print('arr1: before shuffling --> ',arr1, '\n')

shuffle_arr1 = random.shuffle(arr1)
print('arr1: after shuffling --> ',arr1, '\n')
print('shuffle_arr1 --> ',shuffle_arr1, '\n') # it will return None
print('\n..........................................................\n')

# using permutation() 
arr2 = np.array([1,2,3,4,5,6,7,8,9,10])
print('arr2: before shuffling --> ',arr2, '\n')

shuffle_arr2 = random.permutation(arr2)
print('arr2: after shuffling --> ',arr2, '\n')
print('shuffle_arr2 --> ',shuffle_arr2, '\n') # it will return shuffled array
print('\n..........................................................\n')




""" shuffleing 2D array """
arr3 = np.array([[1,2,3,4], ['a','b','c','d'], [5,6,7,8], 
                 [-1,-2,-3,-4], ['e','f','g','h'], [-5,-6,-7,-8]])

shuffle1_arr3 = random.permutation(arr3)
print('shuffle1_arr3:\n',shuffle1_arr3)
print('\n..........................................................\n')

shuffle2_arr3 = random.permutation(arr3[0])
print('shuffle2_arr3 --> ',shuffle2_arr3)
print('\n..........................................................\n')

shuffle3_arr3 = random.permutation(arr3[4])
print('shuffle3_arr3 --> ',shuffle3_arr3)
print('\n..........................................................\n')




""" shuffling 3D array """
arr4 = np.array([[[1,2,3,4], ['a','b','c','d'], [5,6,7,8]],
                   [[-1,-2,-3,-4], ['e','f','g','h'], [-5,-6,-7,-8]]
                  ])

shuffle1_arr4 = random.permutation(arr4)
print('shuffle1_arr4:\n',shuffle1_arr4)
print('\n..........................................................\n')

shuffle2_arr4 = random.permutation(arr4[1])
print('shuffle2_arr4:\n',shuffle2_arr4)
print('\n..........................................................\n')

shuffle3_arr4 = random.permutation(arr4[1, 2])
print('shuffle3_arr4 -->',shuffle3_arr4)
print('\n..........................................................\n')

shuffle4_arr4 = random.permutation(arr4[0, 1])
print('shuffle4_arr4 -->',shuffle4_arr4)
print('\n..........................................................\n')



