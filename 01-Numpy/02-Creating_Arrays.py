import numpy as np

# to create array, we use array() 
arr1 = np.array([1,2,3,'a',5,'b',True])
print('arr1 --> ',arr1)
print('type(arr1) --> ',type(arr1), '\n')
print('.............................................\n')

# we can use also set and others
arr2 = np.array((1,2,3,'a',5,'b',True))
print('arr2 --> ',arr2)
print('type(arr2) --> ',type(arr2), '\n')
print('.............................................\n')

arr3 = np.array({1,2,3,'a',5,'b',True,'b'})
print('arr3 --> ',arr3)
print('type(arr3) --> ',type(arr3), '\n')
print('.............................................\n')


# Creating 0-D array
ZeroD1 = np.array(45)
ZeroD2 = np.array('haider')
print('ZeroD1 --> ',ZeroD1)
print('type(ZeroD1) --> ',type(ZeroD1), '\n')
print('ZeroD2 --> ',ZeroD2)
print('type(ZeroD2) --> ',type(ZeroD2), '\n')
print('.............................................\n')


# Creating 1-D array
OneD1 = np.array(['a','b',1,2,3,100,None])
OneD2 = np.array(('a','b',1,2,3,100,None))
print('OneD1 --> ',OneD1)
print('type(OneD1) --> ',type(OneD1), '\n')
print('OneD2 --> ',OneD2)
print('type(OneD2) --> ',type(OneD2), '\n')
print('.............................................\n')


# Creating 2-D array
TwoD = np.array([[1,2,3,4], ['a','b','c','d'], [5,6,7,8]])
print('TwoD: \n',TwoD)
print('type(TwoD) --> ',type(TwoD), '\n')
print('.............................................\n')


# Creating 3-D array
ThreeD = np.array([[[1,2,3,4], ['a','b','c','d'], [5,6,7,8]],
                   [[-1,-2,-3,-4], ['e','f','g','h'], [-5,-6,-7,-8]]
                  ])
print('ThreeD: \n',ThreeD)
print('type(ThreeD) --> ',type(ThreeD), '\n')
print('.............................................\n')


# ndim --> it is used to check the dimension of the array
print('ZeroD1.ndim --> ',ZeroD1.ndim,'\n')
print('OneD1.ndim --> ',OneD1.ndim,'\n')
print('TwoD.ndim --> ',TwoD.ndim,'\n')
print('ThreeD.ndim --> ',ThreeD.ndim,'\n')
print('.............................................\n')


# ndmin --> it is used to convert he array into lower dimension to heigher dimension
arr4 = np.array([1,2,3,4,5], ndmin=6)
print('arr4 --> ',arr4)
print('type(arr4) --> ',type(arr4))
print('arr4.ndim --> ',arr4.ndim, '\n')
print('.............................................\n')


arr5 = np.array([[1,2,3,4,5], [6,7,8,9,10]], ndmin=8)
print('arr5 --> ',arr5)
print('type(arr5) --> ',type(arr5))
print('arr5.ndim --> ',arr5.ndim, '\n')
print('.............................................\n')


# here it will not work
arr6 = np.array([[1,2,3,4,5], [6,7,8,9,10]], ndmin=1)
print('arr6 --> ',arr6)
print('type(arr6) --> ',type(arr6))
print('arr6.ndim --> ',arr6.ndim, '\n')
print('.............................................\n')

