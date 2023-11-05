a = 1000
l = [10,'as3',None]
def func1():
    print('it is func1')

print('globals() --> ', globals(), '\n')

global_data = globals()

print('global_data["a"] --> ',global_data["a"], '\n')
print('global_data["l"] --> ',global_data["l"], '\n')
print('global_data["func1"] --> ',global_data["func1"], '\n')

""" 
    becuse it returns a dictionary therefore we can use 
    any method of dictionary to manipulate it
"""