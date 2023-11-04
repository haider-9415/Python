""" using return statement, we can access the value of 
    the local variable outside the function
"""
p, n, r = 10000, 3, 12.25
def SI(p, n, r):
    si = (p*n*r)/100
    print("inside the function - si: ",si)
    return si

si = SI(10000, 3, 12.25)
print("outside the function - si: ",si)
total_pay = p + si
print('total_pay --> ',total_pay)
print('.................................................\n')



# when we use return for multiple parameters then it will return in a tuple
def func1(a,b,c,d):
    return a,b,c,d
a = func1("haider",[1,2,3,'a','b',89+9j],{'a','b','c','d'},2023)
print("a --> ",a)
print("type(a) --> ",type(a),'\n')

# we can assign them in multiple variables like this
e,f,g,h = func1("haider",[1,2,3,'a','b',89+9j],{'a','b','c','d'},2023)
print("e --> ",e);print("f --> ",f);print("g --> ",g);print("h --> ",h,'\n')
print("type(e) --> ",type(e));print("type(f) --> ",type(f));print("type(g) --> ",type(g));print("type(h) --> ",type(h),'\n')
print('.................................................\n')

# if we don't use 'return' then the function returns 'None' by default
def hello():
    print('Hello, i am haider')
output = hello()
print('output --> ',output)
print('.................................................\n')
