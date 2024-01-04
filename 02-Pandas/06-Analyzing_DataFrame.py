import pandas as pd

""" using head() """

# by default, it prints first 5 rows
fl1 = pd.read_csv('file1.csv')
print('fl1.head():\n',fl1.head())
print('\n..........................................................................\n')

# we can print specific no. of rows from starting
print('fl1.head(10):\n',fl1.head(10))
print('\n..........................................................................\n')
print('fl1.head(17):\n',fl1.head(17))
print('\n..........................................................................\n')




""" using tail() """

# by default, it prints last 5 rows
fl1 = pd.read_csv('file1.csv')
print('fl1.tail():\n',fl1.tail())
print('\n..........................................................................\n')

# we can print specific no. of rows from ending
print('fl1.tail(10):\n',fl1.tail(10))
print('\n..........................................................................\n')
print('fl1.tail(17):\n',fl1.tail(17))
print('\n..........................................................................\n')



""" using info(), we can get datatype of values in each column
    and know how many non-null values and etc.
"""
print(fl1.info())
print('\n..........................................................................\n')
