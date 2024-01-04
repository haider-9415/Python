import numpy as np
from numpy import random 


""" to generate random number between 0 & 100 """

# for integers 
random1 = random.randint(100)
random2 = random.randint(100)
print('random1 --> ',random1)
print('random2 --> ',random2)
print('type(random1) --> ',type(random1))
print('type(random2) --> ',type(random2))
print('\n..................................................\n')

# for float numbers
# it generates random number between 0 & 1 if we don't pass any number
random3 = random.rand()
random4 = random.rand()
print('random3 --> ',random3)
print('random4 --> ',random4)
print('type(random3) --> ',type(random3))
print('type(random4) --> ',type(random4))
print('\n..................................................\n')


""" to create 1D array having 'n' random integers """
random7 = random.randint(100, size=(5)) # it will return array having 5 integers between 0 & 100
random8 = random.randint(200, size=(10)) # it will return array having 10 integers between 0 & 200
print('random7 --> ',random7)
print('random8 --> ',random8)
print('type(random7) --> ',type(random7))
print('type(random8) --> ',type(random8))
print('\n..................................................\n')


""" to create 2D array of 'n x m' with random integers """
random9 = random.randint(100, size=(3, 6)) # it will return array having 3 rows & 6 columns with random integers
random10 = random.randint(200, size=(4, 11)) # it will return array having 4 rows & 11 columns with random integers
print('random9:\n',random9)
print('random10:\n',random10)
print('type(random9) --> ',type(random9))
print('type(random10) --> ',type(random10))
print('\n..................................................\n')


""" to create 1D array of 'n' elements with random float numbers """
random11 = random.rand(10) # it will return array having 10 random float numbers
random12 = random.rand(20) # it will return array having 20 random float numbers
print('random11:\n',random11)
print('random12:\n',random12)
print('type(random11) --> ',type(random11))
print('type(random12) --> ',type(random12))
print('\n..................................................\n')


""" to create 2D array of 'n x m' with random float numbers """
random13 = random.rand(5, 6) # it will return array having 5 rows & 6 columns with random float numbers
random14 = random.rand(7, 7) # it will return array having 7 rows & 7 columns with random float numbers
print('random13:\n',random13)
print('random14:\n',random14)
print('type(random13) --> ',type(random13))
print('type(random14) --> ',type(random14))
print('\n..................................................\n')


""" if we want to chose a random number from an existing array then """
arr1 = np.array([1,2,4,2,5556,-234,0,11,-4232,2321.334,-132.1])
random15 = random.choice(arr1)
random16 = random.choice(arr1)
print('random15 -->',random15)
print('random16 -->',random16)
print('type(random15) --> ',type(random15))
print('type(random16) --> ',type(random16))
print('\n..................................................\n')


""" we can create 2d array from the elements of 1D array """
arr1 = np.array([1,2,4,2,5556,-234,0,11,-4232,2321.334,-132.1])
random17 = random.choice(arr1, size=(3, 5))
random18 = random.choice(arr1, size=(4, 15))
print('random17:\n',random17)
print('random18:\n',random18)
print('type(random17) --> ',type(random17))
print('type(random18) --> ',type(random18))
print('\n..................................................\n')
