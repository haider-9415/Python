"""
    Dataframe is a data set in pandas

    data set in pandas is usually a multidimentional table

    it is printed in table form

    we can say it is 2D array
"""
import pandas as pd


dict1 = {"calorie":[420,380,390,270], "duration":[50, 40, 45, 35]}
DF1 = pd.DataFrame(dict1)
print(f'DF1:\n{DF1}')
print(f'type(DF1) --> {type(DF1)}')
print(f'type(dict1) --> {type(dict1)}')
print('\n.....................................................\n')



""" we can access individual row using its index """
# in the form of series
print(f'DF1.loc[0]:\n{DF1.loc[0]}\n')
print(f'DF1.loc[1]:\n{DF1.loc[1]}\n')
print(f'DF1.loc[2]:\n{DF1.loc[2]}\n')
print(f'DF1.loc[3]:\n{DF1.loc[3]}\n')
print('\n.....................................................\n')
# in the form of table
print(f'DF1.loc[[0]]:\n{DF1.loc[[0]]}\n')
print(f'DF1.loc[[1]]:\n{DF1.loc[[1]]}\n')
print(f'DF1.loc[[2]]:\n{DF1.loc[[2]]}\n')
print(f'DF1.loc[[3]]:\n{DF1.loc[[3]]}\n')
print('\n.....................................................\n')



""" we can access more than one row using their indices """
print(f'DF1.loc[[0,1]]:\n{DF1.loc[[0,1]]}\n')
print(f'DF1.loc[[1,2]]:\n{DF1.loc[[1,2]]}\n')
print(f'DF1.loc[[0,3]]:\n{DF1.loc[[0,3]]}\n')
print(f'DF1.loc[[3,1]]:\n{DF1.loc[[3,1]]}\n')
print(f'DF1.loc[[3,0]]:\n{DF1.loc[[3,0]]}\n')
print('\n.....................................................\n')



""" we can set our own indices"""
DF2 = pd.DataFrame(dict1, index=['day1', 'day2', 'day3', 'day4'])
print(f'DF2:\n{DF2}')
print(f'type(DF2) --> {type(DF2)}')
print('\n.....................................................\n')

# now we have to use these indices
print(f'DF2.loc[["day1","day2"]]:\n{DF2.loc[["day1","day2"]]}\n')
print(f'DF2.loc[["day2","day3"]]:\n{DF2.loc[["day2","day3"]]}\n')
print(f'DF2.loc[["day1","day4"]]:\n{DF2.loc[["day1","day4"]]}\n')
print(f'DF2.loc[["day4","day2"]]:\n{DF2.loc[["day4","day2"]]}\n')
print(f'DF2.loc[["day4","day1"]]:\n{DF2.loc[["day4","day1"]]}\n')
print('\n.....................................................\n')

# or
print(f'DF2.loc["day1"]:\n{DF2.loc["day1"]}\n')
print(f'DF2.loc["day2"]:\n{DF2.loc["day2"]}\n')
print(f'DF2.loc["day3"]:\n{DF2.loc["day3"]}\n')
print(f'DF2.loc["day4"]:\n{DF2.loc["day4"]}\n')
print('\n.....................................................\n')

print(f'DF2.loc[["day1"]]:\n{DF2.loc[["day1"]]}\n')
print(f'DF2.loc[["day2"]]:\n{DF2.loc[["day2"]]}\n')
print(f'DF2.loc[["day3"]]:\n{DF2.loc[["day3"]]}\n')
print(f'DF2.loc[["day4"]]:\n{DF2.loc[["day4"]]}\n')
print('\n.....................................................\n')

