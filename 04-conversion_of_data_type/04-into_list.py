# we can convert string,tuple,dictionary and set into list
# only keys are convert into set,if we convert dictionary into set

# string --> list
str1 = 'this is a glass'
str2 = 'hanzala'
print("string --> list")
print("    ",str1,"-->",list(str1))
print("    ",str2,"-->",list(str2))

# tuple --> list
tp1 = (0,1,2,3,4,5,6,7,8,9)
tp2 = ('haider','hanzala','naeem')
tp3 = 'he','she','it','they'
tp4 = 383,393,833,664
print("tuple --> list")
print("    ",tp1,"-->",list(tp1))
print("    ",tp2,"-->",list(tp2))
print("    ",tp3,"-->",list(tp3))
print("    ",tp4,"-->",list(tp4))

# dictionary --> list
dict1 = {1:'a',2:'b',3:'c',4:'d'}
dict2 = {'name':'haider','class':'12th','subject':'PCM'}
print("dictionary --> list")
print("    ",dict1,"-->",list(dict1 ))
print("    ",dict2,"-->",list(dict2 ))

# set --> list
set1 = {0,1,2,3,4,5,6,7,8,9}
set2 = {'haider',2323,7+4+5-4,'those'}
print("set --> list")
print("    ",set1,"-->",list(set1 ))
print("    ",set2,"-->",list(set2 ))