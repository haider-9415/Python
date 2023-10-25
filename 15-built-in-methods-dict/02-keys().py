""" to get all keys --> .keys() """



dict1 = {'subject' : ['physics','math','chemistry'],'abcd':{100:'a',200:'b',300:'c'},
         'teachers':{'sudhanshu','sanket','vishwamohan','nitin','kirish','vishwamohan','haider'}}


print("Keys",end=': ')
print(dict1.keys(),'\n')
print(type(dict1.keys()),'\n')
print("after converting in list",end=": ")
print(list(dict1.keys()),'\n')