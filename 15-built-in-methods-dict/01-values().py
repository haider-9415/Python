""" to get all values --> .values() """



dict1 = {'subject' : ['physics','math','chemistry'],'abcd':{100:'a',200:'b',300:'c'},
         'teachers':{'sudhanshu','sanket','vishwamohan','nitin','kirish','vishwamohan','haider'}}


print("values",end=': ')
print(dict1.values(),'\n')
print(type(dict1.values()),'\n')
print("after converting in list",end=': ')
print(list(dict1.values()),'\n')