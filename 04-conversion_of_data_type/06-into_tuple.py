# we can convert string,set,dictionary and list into tuple
# only keys are convert into tuple,if we convert dictionary into tuple

# string --> tuple
str1 = 'this is awsome'
str2 = "haider"
print("string --> tuple")
print("    ",str1,"-->",tuple(str1))
print("    ",str2,"-->",tuple(str2))

# set-> tuple
set1 = {0,1,2,3,4,5,6,7,8,9}
set2 = {'haider','hanzala','naeem','hanzala'}
print("set --> tuple")
print("    ",set1,"-->",tuple(set1))
print("    ",set2,"-->",tuple(set2))

# dictionary --> tuple
dict1 = {1:'a',2:'b',3:'c',4:'d'}
dict2 = {'name':'haider','class':'12th','subject':'PCM'}
print("dictionary --> tuple")
print("    ",dict1,"-->",tuple(dict1 ))
print("    ",dict2,"-->",tuple(dict2 ))

# list --> tuple
lt1 = [0,1,2,3,4,5,6,7,8,9]
lt2 = ['haider',2323,7+4+5-4]
print("list --> tuple")
print("    ",lt1,"-->",tuple(lt1 ))
print("    ",lt2,"-->",tuple(lt2 ))

