""" to get key&value pairs --> .items() """




dict1 = {'subject' : ['physics','math','chemistry'],'abcd':{100:'a',200:'b',300:'c'},
         'teachers':{'sudhanshu','sanket','vishwamohan','nitin','kirish','vishwamohan','haider'}}


print("key&value pairs",end=": ")
print(dict1.items(),'\n')
print(type(dict1.items()),'\n')
print("after converting in list",end=": ")
print(list(dict1.items()),'\n')