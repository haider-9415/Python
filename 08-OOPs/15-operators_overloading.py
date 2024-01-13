"""
    step-1 => python checks datatype(class) of operands
    step-2 => goes in that class
    step-3 => call __func-name__()
"""

num1 = 100
num2 = 100

print('num1 + num2 --> ',num1 + num2, '\n')
# we can do it like that
print('num1.__add__(num2) --> ',num1.__add__(num2), '\n')
# or
print('int.__add__(num1 + num2) --> ',int.__add__(num1, num2), '\n')
print("..................................................................\n")


str1 = 'Hello'
str2 = 'Haider'

print('str1 + str2 --> ',str1 + str2, '\n')
# we can do it like that
print('str1.__add__(str2) --> ',str1.__add__(str2), '\n')
# or
print('str.__add__(str1 + str2) --> ',str.__add__(str1, str2), '\n')
"""
    you can see that __add__() is working differently for different classes
"""
print("..................................................................\n")



"""
    we can assign meaning for a operator
"""
class Books1:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

ob1_books1 = Books1('abcd', 100)
ob2_books1 = Books1('efgh', 200)

print('usign --> ob1_books1.pages + ob2_books1.pages:')
print("total no. of pages = ",ob1_books1.pages + ob2_books1.pages, '\n')
# the following will give error, because there is no function is defined for '+' for objects
# ob1_books1 + ob2_books1 --> ob1_books1.__add__(ob2_books1) --> Books1.__add__(ob1_books1, ob2_books1)
# print("total no. of pages = ",ob1_books1 + ob2_books1, '\n')

# now we will assign __add__() for '+'
class Books2:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __add__(self, other): # self contains 'ob1_books2' & other contains 'ob2_books2'
        total = self.pages + other.pages
        return total
    
ob1_books2 = Books2('abcd', 100)
ob2_books2 = Books2('efgh', 200)
# now it will not give error
print('usign --> ob1_books2 + ob2_books2:')
print("total no. of pages = ",ob1_books2 + ob2_books2, '\n')
print("..................................................................\n")

# but
ob3_books2 = Books2('efgh', 300)
# it will give error, because, 'ob1_books2 + ob2_books2' becomes objects of 'int' class and 'ob3_books2' is object of 'Books2' class
# print("total no. of pages = ",ob1_books2 + ob2_books2 + ob3_books2, '\n')

# to resolve it
class Books3:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __add__(self, other): # self contains 'ob1_books2' & other contains 'ob2_books2'
        total = self.pages + other.pages
        return Books3('All Books', total)
    
    def __str__(self):
        return str(self.pages) # __str__() returns only string

ob1_books3 = Books3('abcd', 100)
ob2_books3 = Books3('efgh', 200)
ob3_books3 = Books3('efgh', 300)
# now it wil not give error
print('using --> ob1_books3 + ob2_books3 + ob3_books3:')
print("total no. of pages = ",ob1_books3 + ob2_books3 + ob3_books3, '\n')
print("..................................................................\n")

# now we can use multiple objects
ob4_books3 = Books3('efgh', 400)
ob5_books3 = Books3('efgh', 500)
ob6_books3 = Books3('efgh', 600)

print('using --> ob1_books3 + ob2_books3 + ob3_books3 + ob4_books3 + ob5_books3 + ob6_books3:')
print("total no. of pages = ",ob1_books3 + ob2_books3 + ob3_books3 + ob4_books3 + ob5_books3 + ob6_books3, '\n')
print("..................................................................\n")





"""
    now we will see overloading of comparision operator
"""
class hotel:
    def __init__(self, name, fare):
        self.name = name
        self.fare = fare

    def __gt__(self, other):
        return self.fare > other.fare

h1 = hotel('Radhe Lal', 20000)
h2 = hotel('Prem', 10000)

print('h1 > h2 --> ',h1 > h2)
print('h1 < h2 --> ',h1 < h2)
print("..................................................................\n")
