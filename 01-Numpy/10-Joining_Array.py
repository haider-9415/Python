""" Using concatinate() """

import numpy as np

# joining 1D array
arr1 = np.array([1,2,3,4,5,6,7])
arr2 = np.array(['a','b','c','d'])

concate1 = np.concatenate((arr1, arr2))
print('concate1 -->',concate1)
print('\n....................................................\n')

concate2 = np.concatenate((arr2, arr1))
print('concate2 -->',concate2)
print('\n....................................................\n')



# joining 2D array
arr3 = np.array([[1,2,3], ['a','b','c']])
arr4 = np.array([[4,5,6], ['d','e','f']])
arr5 = np.array([[7,8,9], ['g','h','i']])

concate3 = np.concatenate((arr3, arr4, arr5))
print('concate3:\n',concate3)
print('\n....................................................\n')

# on passing axis=1, it joins sub arrays having same index number
concate4 = np.concatenate((arr4, arr3, arr5), axis=1)
print('concate4:\n',concate4)
print('\n....................................................\n')

arr6 = np.array([[1,2,3], ['a','b','c'], ['i','ii','iii']])
arr7 = np.array([[4,5,6], ['d','e','f'], ['iv','v','vi']])
arr8 = np.array([[7,8,9], ['g','h','i'], ['vii','viii','ix']])

concate5 = np.concatenate((arr6, arr7, arr8))
print('concate5:\n',concate5)
print('\n....................................................\n')

concate6 = np.concatenate((arr6, arr7, arr8), axis=1)
print('concate6:\n',concate6)
print('\n....................................................\n')



# joining 3D arrays
arr9 = np.array([[[1,2,3,4], ['a','b','c','d'], [5,6,7,8]],
                   [[-1,-2,-3,-4], ['e','f','g','h'], [-5,-6,-7,-8]]
                  ])

arr10 = np.array([[[9,10,11,12], ['i','j','k','l'], [13,14,15,16]],
                   [[-9,-10,-11,-12], ['m','n','o','p'], [-13,-14,-15,-16]]
                  ])

concate7 = np.concatenate((arr9,arr10))
print('concate7:\n',concate7)
print('\n....................................................\n')

concate8 = np.concatenate((arr9,arr10), axis=1)
print('concate8:\n',concate8)
print('\n....................................................\n')

# on passing axis=2, it joins sub arrays having same index number
concate9 = np.concatenate((arr9,arr10), axis=2)
print('concate9:\n',concate9)
print('\n....................................................\n')



""" Using stack(), it makes nD array in (n+1)D array """
arr11 = np.array([1,2,3,4])
arr12 = np.array(['a','b','c','d'])

concate10 = np.stack((arr11,arr12))
print('concate10:\n',concate10)
print('concate10.ndim -->',concate10.ndim)
print('\n....................................................\n')

concate11 = np.stack((arr3,arr4))
print('concate11:\n',concate11)
print('concate11.ndim -->',concate11.ndim)
print('\n....................................................\n')

concate12 = np.stack((arr3,arr4,arr5))
print('concate12:\n',concate12)
print('concate12.ndim -->',concate12.ndim)
print('\n....................................................\n')

concate13 = np.stack((arr3,arr4,arr5), axis=1)
print('concate13:\n',concate13)
print('concate13.ndim -->',concate13.ndim)
print('\n....................................................\n')

concate14 = np.stack((arr9,arr10), axis=1)
print('concate14:\n',concate14)
print('concate14.ndim -->',concate14.ndim)
print('\n....................................................\n')

concate15 = np.stack((arr9,arr10), axis=2)
print('concate15:\n',concate15)
print('concate15.ndim -->',concate15.ndim)
print('\n....................................................\n')

concate16 = np.stack((arr9,arr10), axis=3)
print('concate16:\n',concate16)
print('concate16.ndim -->',concate16.ndim)
print('\n....................................................\n')



""" using hstack() """
# it concatinates row wise
concate16 = np.hstack((arr1,arr2))
print('concate16:\n',concate16)
print('concate16.ndim -->',concate16.ndim)
print('\n....................................................\n')

concate17 = np.hstack((arr3,arr4,arr4))
print('concate17:\n',concate17)
print('concate17.ndim -->',concate17.ndim)
print('\n....................................................\n')

concate18 = np.hstack((arr9,arr10))
print('concate18:\n',concate18)
print('concate18.ndim -->',concate18.ndim)
print('\n....................................................\n')



""" using vstack() """
# it concatinates column wise 
concate19 = np.vstack((arr11,arr12))
print('concate19:\n',concate19)
print('concate19.ndim -->',concate19.ndim)
print('\n....................................................\n')

concate20 = np.vstack((arr6,arr7,arr8))
print('concate20:\n',concate20)
print('concate20.ndim -->',concate20.ndim)
print('\n....................................................\n')

concate21 = np.vstack((arr9,arr10))
print('concate21:\n',concate21)
print('concate21.ndim -->',concate21.ndim)
print('\n....................................................\n')



