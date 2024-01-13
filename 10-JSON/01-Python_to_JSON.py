"""
    we will convert the following python object into json
"""
import json

info = {'name':'haider', 'age':22, 'ismarried':False, 'insurance':None}

name = 'haider'
age = 22
data1 = ['haider', 22, False, None]
data2 = ('haider', 22, False, None)
var = None



""" using dumps() --> it does not create file

    for indentation, use indent=no. of spaces

    we can specify separator between elements and even key-value pairs but
    the json-data in json file will give error 
"""
json_object1 = json.dumps(info, indent=4, separators=('~', '|'))
print('using dumps():')
print(f'json_object1 --> {json_object1}')
print('type(json_object1) --> ',type(json_object1), '\n')
print('\n...................................................................\n')



""" using dump() --> it creates json file and it returns None
"""
print('using dump():')

with open('file1.json', 'w') as fl1:
    result = json.dump(info, fl1, indent=4)
    print(f'result --> {result}')

print('\n...................................................................\n')



print(f'data1 --> {data1}')
print('type(data1) --> ',type(data1), '\n')
print(f'json.dumps(data1) --> {json.dumps(data1)}')
print('type(json.dumps(data1)) --> ',type(json.dumps(data1)), '\n')
print('\n...................................................................\n')

print(f'data2 --> {data2}')
print('type(data2) --> ',type(data2), '\n')
print(f'json.dumps(data2) --> {json.dumps(data2)}')
print('type(json.dumps(data2)) --> ',type(json.dumps(data2)), '\n')
print('\n...................................................................\n')
