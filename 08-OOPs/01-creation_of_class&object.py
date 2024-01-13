"""
   Class --> it is like a blue print for objects having same type of functions 
   E.g. --> 'car' is class and 'Audi', 'BMW', 'Mustang', etc. are objects of the class 'car' which have same functionalities like breake, accelerate, etc. 

   Syntex -->  class class_name:
                   statement(s)    

"""

class cl1:
    pass

class cl2:
    print("Helo! \n")

class cl3:

    # we have to give a pointer to the function in a class that may be anything like your name and etc.
    def wlcome_msg(hanzala):
        return "welcome to pwskills\n"
    
""" if we have to access a code from a class then we have to create object of the class 
    so to access welcome_mag() from class cl3, we have to create its object.
    form one object, we can access all things from its class and we can creat multiple 
    objects of one class

    Syntex --> object_name = class_name()
    syntex to access the code --> object_name.code_variable

"""

ob1 = cl3() # here ob1 is an object of class cl3

print(ob1.wlcome_msg())


