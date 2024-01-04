"""
    Data types in NumPy:
                    1)  i for integer
                    2)  b for boolean
                    3)  u for unsigned nteger
                    4)  f for float
                    5)  c for complex float
                    6)  m for timedelta
                    7)  M for datetime
                    8)  O for object
                    9)  S for string
                    10) U for unicode string
                    11) V for momery  

    dtype --> to check the datatype of numpy array                    
"""

import numpy as np

arr1 = np.array([1,2,3,4,5,6,7,8,9])
print('arr1 -->',arr1)
print('arr1.dtype -->',arr1.dtype)
print('\n.............................................\n')

# it returns Un, where n = the length of greates element in the array
arr2 = np.array(['abcd','b','c11','2','ee'])
print('arr2 -->',arr2)
print('arr2.dtype -->',arr2.dtype)
print('\n.............................................\n')


# creatin array with a defined datatype
arr3 = np.array([1,2222222,333,4444,5], dtype='S')
print('arr3 -->',arr3)
print('arr3.dtype -->',arr3.dtype)
print('\n.............................................\n')

# creatin array with a defined datatype & its size
arr4 = np.array([1,2222222,333,4444,5], dtype='i4')
print('arr4 -->',arr4)
print('arr4.dtype -->',arr4.dtype)
print('\n.............................................\n')

# for array of string, we cannot set integer datatype if all elements are not numeric string
# arr5 = np.array(['1','2','a','4'], dtype='i')
# print('arr5 -->',arr5)
# print('arr5.dtype -->',arr5.dtype)
# print('\n.............................................\n')

# but it will not give error
arr6 = np.array(['1','2','3','4'], dtype='i')
print('arr6 -->',arr6)
print('arr6.dtype -->',arr6.dtype)
print('\n.............................................\n')



"""
    astype() --> to convert datatype of existing array
"""
# to convert bollean into integer
arr7 = np.array([1.2, 3.45, 566.334, 3.1])
arr8 = arr7.astype('i')
print('arr8 -->',arr8)
print('arr8.dtype -->',arr8.dtype)
print('\n.............................................\n')

# to convert string into integer
arr9 = np.array(['1234','21','3','42'])
arr10 = arr9.astype('i')
print('arr10 -->',arr10)
print('arr10.dtype -->',arr10.dtype)
print('\n.............................................\n')

# to convert integer into boolean, we have to use 'bool' rather than 'b'
arr11 = np.array([1, 0, 3])
arr12 = arr11.astype(bool)
print('arr12 -->',arr12)
print('arr12.dtype -->',arr12.dtype)
print('\n.............................................\n')


arr13 = np.array(['a','b',1,2,3,100,None])
print('arr13 -->',arr13)
print('arr13.dtype -->',arr13.dtype)
print('\n.............................................\n')
