"""
    CSV files contains comma separated values

    it contains simple text



"""
import pandas as pd

# to load CSV file into a dataframe
fl1 = pd.read_csv('file1.csv')
print('fl1.to_string():\n',fl1.to_string())
print('\n..........................................................................\n')

# without to_string()
print('fl1:\n',fl1)
print('\n..........................................................................\n')


""" we can check that how much rows our system shows in 
    a proper dataframe without using to_string()
"""
print('pd.options.display.max_rows --> ',pd.options.display.max_rows)
print('\n..........................................................................\n')

# file3.csv will be in proper dataframe without using to_tring()
fl2 = pd.read_csv('file3.csv')
print('fl2:\n',fl2)
print('\n..........................................................................\n')

# we can increase the no. of rows
pd.options.display.max_rows = 300
print('pd.options.display.max_rows --> ',pd.options.display.max_rows)
print('\n..........................................................................\n')

# now, file1.csv will be in proper dataframe without using to_tring()
print('fl1:\n',fl1)
print('\n..........................................................................\n')


