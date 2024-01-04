"""
    it is reverse of joining array

    we use array_split(arr, n), n tells in how many peices you want to break the array

    it returns the result in a list

    if 'n' is greater then no. of elements in an xD array by 'm' 
    then m subarray(s) will be empty
"""

import numpy as np

arr1 = np.array([1,2,3,4,5,6,7,8,9])

# to breake into 3 parts
splitted1_arr1 = np.array_split(arr1, 3)
print('splitted1_arr1 -->',splitted1_arr1)
print('\n...............................................................................\n')
# we can assign in variables
x1, y1, z1 = splitted1_arr1
print('x1 -->', x1); print('y1 -->', y1); print('z1 -->', z1)
print('\n...............................................................................\n')

# to breake into 4 parts
splitted2_arr1 = np.array_split(arr1, 4)
print('splitted2_arr1 -->',splitted2_arr1)
print('\n...............................................................................\n')
# we can assign in variables
x2, y2, z2, p2 = splitted2_arr1
print('x2 -->', x2); print('y2 -->', y2); print('z2 -->', z2); print('p2 -->', p2)
print('\n...............................................................................\n')




arr2 = np.array([[1,2,3,4], ['a','b','c','d'], [5,6,7,8]])

# to breake into 3 parts
splitted3_arr2 = np.array_split(arr2, 3)
print('splitted3_arr2 -->',splitted3_arr2)
print('\n...............................................................................\n')
# we can assign in variables
x3, y3, z3 = splitted3_arr2
print('x3 -->', x3); print('y3 -->', y3); print('z3 -->', z3)
print('\n...............................................................................\n')

# to breake into 4 parts
splitted4_arr2 = np.array_split(arr2, 4)
print('splitted4_arr2 -->',splitted4_arr2)
print('\n...............................................................................\n')
# we can assign in variables
x4, y4, z4, p4 = splitted4_arr2
print('x4 -->', x4); print('y4 -->', y4); print('z4 -->', z4); print('p4 -->', p4)
print('\n...............................................................................\n')



arr3 = np.array([[1,2,3,4], ['a','b','c','d'], [5,6,7,8], 
                 [-1,-2,-3,-4], [-5,-6,-7,-8]])

# to breake into 4 parts
splitted5_arr3 = np.array_split(arr3, 4)
print('splitted5_arr3 -->',splitted5_arr3)
print('\n...............................................................................\n')
# we can assign in variables
x5, y5, z5, p5 = splitted5_arr3
print('x5 -->', x5); print('y5 -->', y5); print('z5 -->', z5); print('p5 -->', p5)
print('\n...............................................................................\n')

# to breake into 6 parts
splitted6_arr3 = np.array_split(arr3, 6)
print('splitted6_arr3 -->',splitted6_arr3)
print('\n...............................................................................\n')
# we can assign in variables
x6, y6, z6, p6, q6, r6 = splitted6_arr3
print('x6 -->', x6); print('y6 -->', y6); print('z6 -->', z6)
print('p6 -->', p6); print('q6 -->', q6); print('r6 -->', r6)
print('\n...............................................................................\n')

# to breake into 9 parts
splitted7_arr3 = np.array_split(arr3, 9)
print('splitted7_arr3 -->',splitted7_arr3)
print('\n...............................................................................\n')
# we can assign in variables
x6, y6, z6, p6, q6, r6, m6, n6, o6 = splitted7_arr3
print('x6 -->', x6); print('y6 -->', y6); print('z6 -->', z6)
print('p6 -->', p6); print('q6 -->', q6); print('r6 -->', r6)
print('m6 -->', m6); print('n6 -->', n6); print('o6 -->', o6)
print('\n...............................................................................\n')




"""
  we can split column wise
"""
arr4 = np.array([[1,2,3,4], ['a','b','c','d'], [5,6,7,8], 
                 [-1,-2,-3,-4], ['e','f','g','h'], [-5,-6,-7,-8]])

# to breake into 3 parts
splitted8_arr4 = np.array_split(arr4, 3 ,axis=1)
print('splitted8_arr4 -->',splitted8_arr4)
print('\n...............................................................................\n')
# we can assign in variables
x7, y7, z7 = splitted8_arr4
print('x7:\n', x7); print('y7:\n', y7); print('z7:\n', z7)
print('\n...............................................................................\n')

""" or we can use hsplit(arr, n), but remember, n = no. elements of individual arrays in 2d array """
# E.g.
splitted9_arr4 = np.hsplit(arr4, 4)
print('splitted9_arr4 -->',splitted9_arr4)
print('\n...............................................................................\n')
# we can assign in variables
x8, y8, z8, p8 = splitted9_arr4
print('x8:\n', x8); print('y8:\n', y8); print('z8:\n', z8); print('p8:\n', p8); 
print('\n...............................................................................\n')
