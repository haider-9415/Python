"""
    data distribution is a list of all possible values and how often 
    each value occures

    such lists are important while working with statistics and
    data science




"""
import numpy as np
from numpy import random 

""" now we will create a 1D array with 100 values where each value 
    will be 3, 5, 7 or 9

    we will have to set probabilties for each value
    so let,
        probability of 3 be 0.1,
        probability of 5 be 0.3,
        probability of 7 be 0.6 &
        probability of 9 be 0.0
    remember: sum of all probabilities must be 1

"""
arr1 = random.choice([3,5,7,9], p=[0.1,0.3,0.6,0.0], size=(100))
print('arr1:\n',arr1)
print('\n..........................................................\n')



""" now we will create 1D array of 1000 values with digits 1,2,6,7,9 """
arr2 = random.choice([1,2,6,7,9], p=[0.2,0.2,0.2,0.2,0.2], size=(100))
print('arr2:\n',arr2)
print('\n..........................................................\n')



""" similarly we can create 2D & 3D arrays """

# for 2D
arr3 = random.choice([1,2,6,7,9], p=[0.1,0.3,0.3,0.1,0.2], size=(20, 6))
print('arr3:\n',arr3)
print('\n..........................................................\n')

# for 3D
arr3 = random.choice([1,2,6,7,9], p=[0.1,0.3,0.3,0.1,0.2], size=(20, 6, 8))
print('arr3:\n',arr3)
print('\n..........................................................\n')



