"""
    we can an sort an array in ascending or descending order
    using sort()
"""
import numpy as np

arr1 = np.array([100,3,2,6,9,0,6,4,65,6,-1,3,-2,1,33,3,4])

sort1_arr1 = np.sort(arr1)
print('sort1_arr1 -->',sort1_arr1)
print('\n...............................................................................\n')



""" in case of string, strings are sorted according to their numeric values in ASCII """

arr2 = np.array(['a','b','C','A','d','abc','acb','bcd','Abc','cbA'])

sort1_arr2 = np.sort(arr2)
print('sort1_arr2 -->',sort1_arr2)
print('\n...............................................................................\n')



""" in case of boolean, False comes first and True second """

arr3 = np.array([False, True, True, False])

sort1_arr3 = np.sort(arr3)
print('sort1_arr3 -->',sort1_arr3)
print('\n...............................................................................\n')



""" we can sort numeric and boolean values togather 
    but False becomes 0 and True becomes 1
"""
arr4 = np.array([False,3,-6,-5,100, True,45,3,5,63, True, False,0])

sort1_arr4 = np.sort(arr4)
print('sort1_arr4 -->',sort1_arr4)
print('\n...............................................................................\n')



""" we can sort 2D array """
arr5 = np.array([[3,4,1,2], ['Z','d','c','D'], [10,0,4,-4]])

sort1_arr5 = np.sort(arr5)
print('sort1_arr5:\n',sort1_arr5)
print('\n...............................................................................\n')

""" if you want t sort one element then you can do it """ 
sort2_arr5 = np.sort(arr5[0])
print('sort2_arr5:\n',sort2_arr5)
print('\n...............................................................................\n')

sort3_arr5 = np.sort(arr5[2])
print('sort3_arr5:\n',sort3_arr5)
print('\n...............................................................................\n')



""" similarly we can sort 3D array """

arr6 = np.array([[[3,4,1,2], ['Z','d','c','D'], [10,0,4,-4]],
                   [[-7,1,True,-4], ['e','F','O','h'], [0,-6,False,-8]]
                  ])

sort1_arr6 = np.sort(arr6)
print('sort1_arr6:\n',sort1_arr6)
print('\n...............................................................................\n')

sort2_arr6 = np.sort(arr6[1])
print('sort2_arr6:\n',sort2_arr6)
print('\n...............................................................................\n')

sort3_arr6 = np.sort(arr6[1, 2])
print('sort3_arr6:\n',sort3_arr6)
print('\n...............................................................................\n')

sort4_arr6 = np.sort(arr6[0, 0])
print('sort4_arr6:\n',sort4_arr6)
print('\n...............................................................................\n')


