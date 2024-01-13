class employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = fname + lname + "@gmail.com"
    
    @property
    def email(self):
        return f'{self.fname}{self.lname}@gmail.com'
    
    def display(self):
        return f'first-name:{self.fname} - last-name:{self.lname} - mail-ID:{self.email}'

e1 = employee('tony', 'stark')
e2 = employee('harry', 'potter')
e3 = employee('steven', 'strange')

"""
    without using @property
"""
"""
e1.fname = 'haider'
# you will see that the 'email' variable will not be updated it has still 'tony' as 'fname'
# print('e1.email --> ',e1.email, '\n')
# so will create the method
print('e1.email() --> ',e1.email(), '\n')
print('e1.display() --> ',e1.display(), '\n')
print('.....................................................\n')

# similarly
e2.fname = 'thor'
print('e2.email() --> ',e2.email(), '\n')
print('e2.display() --> ',e2.display(), '\n')
print('.....................................................\n')

e3.fname = 'loki'
print('e3.email() --> ',e3.email(), '\n')
print('e3.display() --> ',e3.display(), '\n')
print('.....................................................\n')

"""



"""
    with using @property
"""
e1.fname = 'haider'
print('e1.email --> ',e1.email, '\n')
print('e1.display() --> ',e1.display(), '\n')
print('.....................................................\n')

e2.fname = 'thor'
e2.lname = 'odin'
print('e2.email --> ',e2.email, '\n')
print('e2.display() --> ',e2.display(), '\n')
print('.....................................................\n')

e3.fname = 'loki'
print('e3.email --> ',e3.email, '\n')
print('e3.display() --> ',e3.display(), '\n')
print('.....................................................\n')


