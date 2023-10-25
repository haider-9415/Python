""" to implement a function, a keyword 'def' is used """

""" syntex --> def func_name(argument(s)): 
                   docstring --> it tells that what the function do
                   code                              
"""

from math import pi

# function for curved surface area of cylinder
def cylinder (h,r):
    "it calculates curved surface area of cylinder "
    area = 2*pi*h*r
    return area

# function for curved surface area of cone
def cone (l,r):
    "it calculates curved surface area of cone "
    area = pi*r*l
    return area

# length of fabric
def len_feb(t_area,width_fab):
    "it calculates the length of fabric "
    length = t_area/width_fab
    return length

# cost (exclusive of tax)
def cost(len_feb,rate):
    "it calculates the cost (exclusive of tax) "
    cost = len_feb*rate
    return cost

# net amount (inclusive of tax)
def amount(cost):
    "it calculates the cost (inclusive of tax) "
    tax = 0.18*cost
    net_amount = tax+cost
    return net_amount



# function for swaping values
def swap(a,b):
    " it swaps two values "
    a,b = b,a
    print("after swaping")
    print("    a =",a," & b =",b,'\n')

a = int(input("enter a: "))
b = int(input("enter b: "))
print("before swaping")
print("    a =",a," & b =",b)
swap(a,b)


"""
   lambda function
   lambda is a keyword that is used to create a nameless-function
   we don;t have to name the function 

   syntex --> lambda parameters: statement(s)
"""
l1 = lambda a,b,c: a+b+c
print("l1(10,20,30) --> ",l1(10,20,30),'\n')

l2 = lambda a,b: a**b
print("l2(10,2) --> ",l2(10,2),'\n')
print("l2(2,5) --> ",l2(2,5),'\n')
print("l2(100,2) --> ",l2(100,2),'\n')