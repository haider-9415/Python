"""
    we can use try-except blocks inside of another try-except blocks
"""

try:
    f1 = open('data1.txt', mode='r') # replace 'data1.txt' with 'data.txt'
    my_data = f1.read()
    print(f'\n{my_data}\n')
except Exception as e:
    print(f'\n{e}\n')
else:
    print('Read operation success\n')
finally:
    """ if we don't use this try-except block then it will give error
        because there is no file named 'data.txt', therefore, the 'f1'
        variable does not exists, so, it will give error on using 'f1'
    """
    try:
        f1.close()
    except:
        pass

print('Rest of Code\n')