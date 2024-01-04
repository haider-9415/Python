"""
    Cleaning Data means fixing bad data in your data set

    bad data could be empty cell, data in a wrong formate, wrong data
    and duplicate data 

    we have to remove whole row if it contains any bad data

"""
import pandas as pd

fl1 = pd.read_csv('dirtydata.csv')
print('fl1.to_string():\n',fl1.to_string())
print('\n..........................................................................\n')



""" empty cell will give you wrong result always so we will have 
    to remove it using dropna()
"""
cln_null1 = fl1.dropna()
print('cln_null1:\n',cln_null1)
print('\n..........................................................................\n')

# to remove in original data frame
fl1.dropna(inplace=True)
print('fl1.to_string():\n',fl1.to_string())
print('\n..........................................................................\n')



""" we can replace with any other value using fillna() """
fl2 = pd.read_csv('dirtydata.csv')
cln_null2 = fl2.fillna(100000)
print('cln_null2:\n',cln_null2)
print('\n..........................................................................\n')

cln_null3 = fl2.fillna('bad-value')
print('cln_null3:\n',cln_null3)
print('\n..........................................................................\n')

# to replace in original data frame
fl2.fillna('null-value', inplace=True)
print('fl2.to_string():\n',fl2.to_string())
print('\n..........................................................................\n')



""" we can replce or remove in a perticular column using its name """

fl3 = pd.read_csv('dirtydata.csv')
fl3["Calories"].fillna('bad-value', inplace=True)
print('fl3.to_string():\n',fl3.to_string())
print('\n..........................................................................\n')



""" we can also replace empty cells with mean, median or mode """

# for mean
fl4 = pd.read_csv('dirtydata.csv')
mean_value = fl4["Calories"].mean()
fl4["Calories"].fillna(mean_value, inplace=True)
print('fl4.to_string():\n',fl4.to_string())
print('\n..........................................................................\n')

# for median
fl5 = pd.read_csv('dirtydata.csv')
median_value = fl5["Calories"].median()
fl5["Calories"].fillna(median_value, inplace=True)
print('fl5.to_string():\n',fl5.to_string())
print('\n..........................................................................\n')

# for mode
fl6 = pd.read_csv('dirtydata.csv')
mode_value = fl6["Calories"].mode()[0]
fl6["Calories"].fillna(mode_value, inplace=True)
print('fl6.to_string():\n',fl6.to_string())
print('\n..........................................................................\n')




""" now we will fix data in wong formate 
    
    there are two ways to fix it
    1) removing the rows
    2) convert all cells of the column in same formate
"""
fl7 = pd.read_csv('dirtydata.csv')
print('fl7.to_string():\n',fl7.to_string())
print('\n..........................................................................\n')

# there is a wrong format in 'date' column
# to convert all cells in same formate, use to_datetime()
fl8 = pd.read_csv('dirtydata.csv')
fl8["Date"] = pd.to_datetime(arg=fl8["Date"], dayfirst=True, format='mixed')
print('fl8.to_string():\n',fl8.to_string())
print('\n..........................................................................\n')


""" to remove the rows having null values in Date column """
fl9 = pd.read_csv('dirtydata.csv')
fl9.dropna(subset=["Date"], inplace=True)
print('fl9.to_string():\n',fl9.to_string())
print('\n..........................................................................\n')




""" now we will fix wrong data
"""
fl10 = pd.read_csv('dirtydata.csv')
print('fl10.to_string():\n',fl10.to_string())
print('\n..........................................................................\n')

""" there is a wrong data in Duration column that is 450 so
    we have to set it 45

    we have to use index of the row
"""

fl11 = pd.read_csv('dirtydata.csv')
fl11.loc[7, "Duration"] = 45
print('fl11.to_string():\n',fl11.to_string())
print('\n..........................................................................\n')




""" we can use loop to set limit """

fl12 = pd.read_csv('dirtydata.csv')
for i in fl12.index:
    if fl12.loc[i, "Duration"] > 60:
        fl12.loc[i, "Duration"] = 60

print('fl12.to_string():\n',fl12.to_string())
print('\n..........................................................................\n')




""" for larger dataset, we can use loop to remove rows having wrong data """

fl13 = pd.read_csv('dirtydata.csv')
for i in fl13.index:
    if fl13.loc[i, "Duration"] > 60:

        fl13.drop(i, inplace=True)
print('fl13.to_string():\n',fl13.to_string())
print('\n..........................................................................\n')




""" now we will remove duplicate rows """
fl14 = pd.read_csv('dirtydata.csv')
print('fl14.to_string():\n',fl14.to_string())
print('\n..........................................................................\n')

# 1st we need to discover duplicate rows so we use duplicated()
# it returns True for duplicate rows
fl15 = pd.read_csv('dirtydata.csv')
print('fl15.duplicated():\n',fl15.duplicated())
print('\n..........................................................................\n')
# it has returned True at 12 index


""" to removee all duplicate rows, drop.duplicates() """
fl14 = pd.read_csv('dirtydata.csv')
fl14.drop_duplicates(inplace=True)
print('fl14.to_string():\n',fl14.to_string())
print('\n..........................................................................\n')
