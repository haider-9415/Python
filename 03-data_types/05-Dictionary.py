# type-5 --> dictionary
""" key must not be repeated in a dictionary """

""" a list ,dictonary and a set can not be the key and a key should not be started with spaciel 
    case character but tuple,boolean,numeric data and string can be a key """

""" value can be a last,dictionary,set,tuple,etc. """

dict1 = {'a':1,'b':2,'c':3,'d':4}
print("dict1 -->",dict1)
print(dict1['a']);print(dict1['b']);print(dict1['c']);print(dict1['d'])

dict2 = {'name':'haider','class':"10th B","""subject""":'PCM'}
print("dict2 -->",dict2)
print(dict2['name']);print(dict2['class']);print(dict2["subject"]);

dict3 = {}
print("dict3 -->",dict3)

dict4 = {(12,3.2,'haider'): 'hanzala',True : 900}
print("dict4 -->",dict4)
print(dict4[(12,3.2,'haider')]);print(dict4[True])

dict5 = {'subject' : ['physics','math','chemistry'],'abcd':{100:'a',200:'b',300:'c'},
         'teachers':{'sudhanshu','sanket','vishwamohan','nitin','kirish','vishwamohan','haider'}}
print("dict5 -->",dict5)
print(dict5['subject'])
print(dict5['subject'][0]);print(dict5['subject'][1]);print(dict5['subject'][2])
print(dict5['abcd'])
print(dict5['abcd'][100]);print(dict5['abcd'][200]);print(dict5['abcd'][300])
print(dict5['teachers'])


print(type(dict1))
print(type(dict2))
print(type(dict3))
print(isinstance(dict1,dict))
print(isinstance(dict2,dict))
print(isinstance(dict3,dict))


""" we acn add new key&value pairs """
dict1['e'] = 5
dict1['f'] = 6
print("dict1 -->",dict1)


""" we can update values """
dict2['name'] = 'hanzala'
dict2['class'] = '12th'
print("dict2 -->",dict2)


""" we can delete any key&value pair using 'del' keyword"""
del dict5['abcd']
print("dict5 -->",dict5)