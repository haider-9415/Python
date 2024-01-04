"""
    Iterating means going through the elemeents of the arrray one by one
"""

import numpy as np

# Iterate 1D array
arr1 = np.array([1,2,3,'a','b',None,True])
x = 1
for i in arr1:
    print(f'element-{x} -->',i)
    x += 1
print('\n....................................................\n')



# Iterate 2D array
arr2 = np.array([[1,2,3,4], ['a','b','c','d'], [5,6,7,8]])
x = 1
for i in arr2:
    print(f'element-{x} -->',i)
    x += 1
print('\n....................................................\n')

x = 0
for i in arr2:
    print(f'in:',i)
    y = 1
    for j in arr2[x]:
        print(f'element-{y} -->',j)
        y += 1
    x += 1
    print()
print('\n....................................................\n')



# Iterate 3D array
arr3 = np.array([[[1,2,3,4], ['a','b','c','d'], [5,6,7,8]],
                   [[-1,-2,-3,-4], ['e','f','g','h'], [-5,-6,-7,-8]]])
x = 1
for i in arr3:
    print(f'element-{x}:\n',i)
    x += 1
print('\n....................................................\n')

x = 0
for i in arr3:
    print(f'in:\n',i)
    y = 1
    for j in arr3[x]:
        print(f'element-{y} -->',j)
        y += 1
    x += 1
    print()
print('\n....................................................\n')
# or
for i in arr3:
    print(f'in:\n',i)
    y = 1
    for j in i:
        print(f'element-{y} -->',j)
        y += 1
    print()
print('\n....................................................\n')

for i in arr3:
    for j in i:
        print(f'in:',j)
        z = 1
        for k in j:
            print(f'element-{z} -->',k)
            z += 1
        print()
print('\n....................................................\n')
# or
x = 0
for i in arr3:
    y = 0
    for j in arr3[x]:
        print(f'in:',j)
        z = 1
        for k in arr3[x,y]:
            print(f'element-{z} -->',k)
            z += 1
        y += 1
        print()
    x += 1
print('\n....................................................\n')


 

""" we can iterate using nditer() """

print('using nditer():\n')

print('using np.nditer(arr3):\n')
for i in np.nditer(arr3):
    print(i)
print('\n....................................................\n')

print('using np.nditer(arr3[:, ::2]):\n')
for i in np.nditer(arr3[:, ::2]):
    print(i)
print('\n....................................................\n')

print('using np.nditer(arr2[:, ::2]):\n')
for i in np.nditer(arr2[:, ::2]):
    print(i)
print('\n....................................................\n')



