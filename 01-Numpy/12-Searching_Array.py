"""
    we can search an array for a certain value 
    and returns the indecies that get match

    we will use where()

    it goes to each element of the given array and checks it
"""
import numpy as np
arr1 = np.array([1,2,3,4,5,6,4,7,4,8,3,2,2,4,8])

search1_arr1 = np.where(arr1 == 4)
print('4 in arr1 at -->',search1_arr1)
print('\n...............................................................................\n')

search2_arr1 = np.where(arr1 == 6)
print('6 in arr1 at -->',search2_arr1)
print('\n...............................................................................\n')

search3_arr1 = np.where(arr1 == 8)
print('8 in arr1 at -->',search3_arr1)
print('\n...............................................................................\n')



arr2 = np.array(['a','b','c','d','abcd','acbd','abdc','acdb'])

search4_arr2 = np.where(arr2 == 'a')
print('"a" in arr2 at -->',search4_arr2)
print('\n...............................................................................\n')

search5_arr2 = np.where(arr2 == 'ab')
print('"ab" in arr2 at -->',search5_arr2)
print('\n...............................................................................\n')

search6_arr2 = np.where(arr2 == 'abdc')
print('"abdc" in arr2 at -->',search6_arr2)
print('\n...............................................................................\n')




""" we can set conditions """

search7_arr1 = np.where(arr1%2 == 0)
print('even no. in arr1 at -->',search7_arr1)
print('\n...............................................................................\n')

search8_arr1 = np.where(arr1%2 == 1)
print('odd no. in arr1 at -->',search8_arr1)
print('\n...............................................................................\n')



""" 
    we can use searchsorted() it works as where() does 
    
    but:
        it performs binary search on array 

        it returns the index of first appearence of the element
        that you are searching

    if we want to get element no. of the elelment in the array
    then we have to use side='right'
"""

search9_arr1 = np.searchsorted(arr1, 4)
print('index no. of first 4 in arr1 -->',search9_arr1)
print('\n...............................................................................\n')

search10_arr1 = np.searchsorted(arr1, 4, side='right')
print('element no. of first 4 in arr1 -->',search10_arr1)
print('\n...............................................................................\n')

search11_arr2 = np.searchsorted(arr2, 'a')
print('index no. of first "a" in arr2 -->',search11_arr2)
print('\n...............................................................................\n')

search12_arr2 = np.searchsorted(arr2, 'a', side='right')
print('element no. of first "a" in arr2 -->',search12_arr2)
print('\n...............................................................................\n')



arr3 = np.array(['a','b','c','d'])

search13_arr3 = np.searchsorted(arr3, 'b')
print('index no. of first "a" in arr3 -->',search13_arr3)
print('\n...............................................................................\n')

search14_arr3 = np.searchsorted(arr3, 'b' ,side='right')
print('element no. of first "b" in arr3 -->',search14_arr3)
print('\n...............................................................................\n')


""" searchsorted() can tell us that where can we place some values
    in the given array such that the array becomes sorted

    it will return the index no. of the places in given array

    it does not place the values in the given array
"""
arr4 = np.array([3,5,7,9])

tell1_arr4 = np.searchsorted(arr4, [2,4,8])
# it will return 0 index of 3 for 2, 1 index of 5 for 4, 3 index of 7 for 8
print('tell1_arr4 -->',tell1_arr4)
print('\n...............................................................................\n')


arr5 = np.array([3,7,5,9])

tell2_arr5 = np.searchsorted(arr5, [2,4,8])
# it will return 0 index of 3 for 2, 1 index of 7 for 4, 3 index of 7 for 8
print('tell2_arr5 -->',tell2_arr5)
print('\n...............................................................................\n')

tell3_arr5 = np.searchsorted(arr5, [2,4,10])
# it will return 0 index of 3 for 2, 1 index of 7 for 4, 4 index of 9 for 10
print('tell3_arr5 -->',tell3_arr5)
print('\n...............................................................................\n')

