import copy 

myList = [[1,2,3],['a','b','c'],[4,'d',5,'e']]
print('myList --> ',myList)
print('id(myList) --> ',id(myList))
print('id(myList[0]) --> ',id(myList[0]))
print('id(myList[1]) --> ',id(myList[1]))
print('id(myList[2]) --> ',id(myList[2]))
print('..................................................\n')

newList = copy.copy(myList)
print('newList --> ',newList)
print('id(newList) --> ',id(newList))
print('id(newList[0]) --> ',id(newList[0]))
print('id(newList[1]) --> ',id(newList[1]))
print('id(newList[2]) --> ',id(myList[2]))
print('..................................................\n')
""" you can see ID of 'myList' & ID of 'newList' only have been changed but other's ID are same """



""" here you can see on changing in one, the change will happen in other one also """
newList[0][2] = 'haider' 
myList[2][1] = 10000

print('myList --> ',myList)
print('newList --> ',newList)
