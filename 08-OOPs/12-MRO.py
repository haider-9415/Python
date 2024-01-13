class A:
    pass
class B:
    pass
class C:
    pass
class X(A,B,C):
    pass
class Y(B,C):
    pass
class P(X,Y):
    pass

# to know the MRO of a class 
print('A.mro(): --> ',A.mro(), '\n')
print('B.mro(): --> ',B.mro(), '\n')
print('C.mro(): --> ',C.mro(), '\n')
print('X.mro(): --> ',X.mro(), '\n')
print('Y.mro(): --> ',Y.mro(), '\n')
print('P.mro(): --> ',P.mro(), '\n')

print(".................................................................\n")




""" if there is a method of same name in parent classes
    then which class comes first, its method will be executed
"""
class cl4:
    def same_meth(self):
        return "this is the part of cl4 class \n"
    
class cl5:
    def same_meth(self):
        return "this is the part of cl5 class \n"
    
class cl6(cl4,cl5):
    def meth_cl6(self):
        return "this is the part of cl6 class \n"

ob_child4 = cl6()
print("ob_child4.same_meth() --> ",ob_child4.same_meth()) # here, method of class cl4 will be executed, because, cl4 is first in 'cl6(cl4,cl5)'

class cl7(cl5,cl4):
    def meth_cl7(self):
        return "this is the part of cl7 class \n"

ob_child5 = cl7()
print("ob_child5.same_meth() --> ",ob_child5.same_meth()) # here, method of class cl4 will be executed, because, cl5 is first in 'cl6(cl5,cl4)'

print(".................................................................\n")


