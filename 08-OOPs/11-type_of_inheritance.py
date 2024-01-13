

"""
    single inheritance
"""
class cl1():
    def func_cl1(self):
        return "this is the function of cl1 \n"
class cl2(cl1):
    def func_cl2(self):
        return "this is the function of cl2 \n"

ob_cl2 = cl2()
print('ob_cl2.func_cl2() --> ',ob_cl2.func_cl2())
print('ob_cl2.func_cl1() --> ',ob_cl2.func_cl1())
print(".................................................................\n")



"""
    multi-level inheritance
"""
class customer():
    def __init__(self):
        print('customer constructor called \n')
    def func_customer(self):
        self.name = 'haider'
        return self.name

class employee(customer):
    def __init__(self):
        super().__init__() # it will execute init() of class 'customer'
        print('employee constructor called \n')
    def func_employee(self):
        self.salary = 30000
        return self.salary

class manager(employee):
    def __init__(self):
        super().__init__() # it will execute init() of class 'employee'
        print('manager constructor called \n')
    def func_manager(self):
        self.bonus = 5000
        return self.bonus

ob_manager = manager()
print('ob_manager.func_customer() --> ',ob_manager.func_customer(), '\n')
print('ob_manager.func_employee() --> ',ob_manager.func_employee(), '\n')
print('ob_manager.func_manager() --> ',ob_manager.func_manager(), '\n')
print(".................................................................\n")

ob_employee = employee()
print('ob_employee.func_customer() --> ',ob_employee.func_customer(), '\n')
print('ob_employee.func_employee() --> ',ob_employee.func_employee(), '\n')
print(".................................................................\n")




"""
    Hierarchical Inheritance
"""
class school:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class teacher(school):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

class student(school):
    def __init__(self, name, age, fees):
        super().__init__(name, age)
        self.fees = fees

s1 = student('harry',18, 1000)
s2 = student('haider',21, 2000)
print(s1.__dict__ , '\n')
print(s2.__dict__ , '\n')
print(".................................................................\n")

t1 = teacher('abcd',25, 8000)
t2 = teacher('efgh',37, 10000)
print(t1.__dict__ , '\n')
print(t2.__dict__ , '\n')
print(".................................................................\n")



class cl1:
    def meth_cl1(self):
        return "this is the part of cl1 class\n"

class cl2:
    def meth_cl2(self):
        return "this is the part of cl2 class\n"
    
class cl3(cl1,cl2): # child of cl1 and cl2
    def meth_cl3(self):
        return "this is the part of cl3 class\n"

ob_child1 = cl3()

print("ob_child1.meth_cl1() --> ",ob_child1.meth_cl1())
print("ob_child1.meth_cl2() --> ",ob_child1.meth_cl2())
print("ob_child1.meth_cl3() --> ",ob_child1.meth_cl3())
print(".................................................................\n")



