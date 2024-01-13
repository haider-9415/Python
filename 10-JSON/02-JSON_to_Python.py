"""
    we will convert the following json object into python object
"""
import json


data = {
    "Age":23,
    "City":"pune",
    "Ismarried":False,
    "Name":"Haider",
    "Number":1234567890,
    "Subject":[
        "Data Structures",
        "Computer Graphics",
        "Web Development"
    ]
}

json_data = json.dumps(data)


"""
    using loads() --> it converts the json data in 
    the current python file

"""
py_object1 = json.loads(json_data)
print('\n----------------------- using loads() -----------------------\n')
print(f'py_object1:\n{py_object1}')
print(f'type(py_object1) --> {type(py_object1)}')
print('\n...................................................................\n')


"""
    using load() --> it converts the json data present in 
    the json file
"""
print('\n----------------------- using load() -----------------------\n')
with open('file2.json', 'r') as fl2:
    py_object2 = json.load(fl2)
    print(f'py_object2:\n{py_object2}')
    print(f'type(py_object2) --> {type(py_object2)}')
    fl2.close()

print('\n...................................................................\n')
