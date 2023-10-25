""" to remove all key&value pairs --> .clear() """


dict1 = {'subject' : ['physics','math','chemistry'],'abcd':{100:'a',200:'b',300:'c'},
         'teachers':{'sudhanshu','sanket','vishwamohan','nitin','kirish','vishwamohan','haider'}}
dict2 = {1:'a',2:'b'}

dict2.clear()
print("dict2 --> ",dict2)
print("type(dict2) --> ",type(dict2),'\n')

print("dict1.clear() -->",dict1.clear())

print("type(dict1.clear()) -->",type(dict1.clear()),'\n')
