"""
    copy is the new array having elements of an array
    view only shows the elements of an array

    on changing the elements of copy does not affet on original array
    but view

    copy() --> to make copy

    view() --> to make view
"""

import numpy as np

arr1 = np.array([1,2,3,4,5,6])
copy_arr1 = arr1.copy()
print('arr1 -->',arr1, '\n')
print('copy_arr1 -->',copy_arr1, '\n')

copy_arr1[1] = 100 # element at 1st index = 100
print('copy_arr1 -->',copy_arr1, '\n')
# but it will not affect on arr1
print('arr1 -->',arr1, '\n')

print('\n....................................................\n')


arr2 = np.array([1,2,3,4,5,6])
view_arr2 = arr2.view()
print('arr2 -->',arr2, '\n')
print('view_arr2 -->',view_arr2, '\n')

view_arr2[1] = 100 # element at 1st index = 100
print('view_arr2 -->',view_arr2, '\n')
# and it will affect on arr2
print('arr2 -->',arr2, '\n')

print('\n....................................................\n')
