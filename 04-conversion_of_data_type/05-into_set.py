# we can convert string,tuple,dictionary and list into set
# remember order of elements in a set changes and no element can come again
# only keys are convert into set,if we convert dictionary into set

# string --> set
str1 = 'this is a glass'
str2 = 'hanzala'
print("string --> set")
print("    ",str1,"-->",set(str1))
print("    ",str2,"-->",set(str2))

# tuple --> set
tp1 = (0,1,2,3,4,5,6,7,8,9)
tp2 = ('haider','hanzala','naeem')
tp3 = 'he','she','it','they'
tp4 = 383,393,833,664
print("tuple --> set")
print("    ",tp1,"-->",set(tp1))
print("    ",tp2,"-->",set(tp2))
print("    ",tp3,"-->",set(tp3))
print("    ",tp4,"-->",set(tp4))

# dictionary --> set
dict1 = {1:'a',2:'b',3:'c',4:'d'}
dict2 = {'name':'haider','class':'12th','subject':'PCM'}
print("dictionary --> set")
print("    ",dict1,"-->",set(dict1 ))
print("    ",dict2,"-->",set(dict2 ))

# list --> set
lt1 = [0,1,2,3,4,5,6,7,8,9]
lt2 = ['haider',2323,7+4+5-4,'those']
print("list --> set")
print("    ",lt1,"-->",set(lt1 ))
print("    ",lt2,"-->",set(lt2 ))