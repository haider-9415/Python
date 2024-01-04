"""
    Series is a 1D array which holds data of any type

    it is like a column in a table

    it is printed with indices of the values
"""
import pandas as pd

list1 = [1,2,30,43,57]
series1 = pd.Series(list1)
print(f'series1:\n{series1}')
print(f'type(series1) --> {type(series1)}')
print(f'type(list1) --> {type(list1)}')
print('\n.....................................................\n')


# we can use indexing to get individual elements
# remember it has no -ve indexing
print('series1[0] -->',series1[0])
print('series1[1] -->',series1[1])
print('series1[2] -->',series1[2])
print('series1[3] -->',series1[3])
print('series1[4] -->',series1[4])
print('\n.....................................................\n')


# we can change indexing
list2 = [1,2,3]
series2 = pd.Series(list2, index=['x','y','z'])
print(f'series2:\n{series2}')
print(f'type(series2) --> {type(series2)}')
print(f'type(list2) --> {type(list2)}')
print('\n.....................................................\n')

# now we have to use given indices to access individual elements
print('series2["x"] -->',series2["x"])
print('series2["y"] -->',series2["y"])
print('series2["z"] -->',series2["z"])
print('\n.....................................................\n')



""" we can use dictionary while creating series with own indices """
calorie = {'day1': 340, 'day2': 270, 'day3': 380, 'day4': 440}
series3 = pd.Series(calorie)
print(f'series3:\n{series3}')
print(f'type(series3) --> {type(series3)}')
print(f'type(calorie) --> {type(calorie)}')
print('\n.....................................................\n')


# using dictionary, we can create a series of values using their keys
series4 = pd.Series(calorie, index=['day1','day4'])
print(f'series4:\n{series4}')
print(f'type(series4) --> {type(series4)}')
print('\n.....................................................\n')


