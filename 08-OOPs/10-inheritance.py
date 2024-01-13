"""
    inheritance --> allows us to define a class that inherits all the methods and 
    properties from another class.
    using this property, we can reuse methods 

    syntex --> class c2(c1):    
                   statement(s)
                here, class 'c2' is the inheritance of class 'c1'
                c1 is called parrent class and c2 is called child class
"""

class c1:
    def pwskills(self):
        return "pwskills is the platform to improve your skills in the tech field\n"

class c2(c1):
    pass

ob1 = c2()

print(ob1.pwskills()) # you can see that we are calling pwskills() through the object of 'c2'
print(".................................................................................\n")



class mentor: # parent class

    def __init__(self, mentor_name, mentor_email_id, mentor_contact):
        self.mentor_name = mentor_name
        self.mentor_email_id = mentor_email_id
        self.mentor_contact = mentor_contact
    
    def mentor_details(self): # to print details of __init__() inside the class
        return self.mentor_name, self.mentor_email_id, self.mentor_contact
        

class DSM(mentor): # child class
    def print_DSM(self):
        return "detail of my Data Science Master class mentors\n"

# ob_DSM = DSM() # it will give error, because, 'DSM' is the inheritance of 'mentor' and it has __init__()

ob_DSM1 = DSM("sudhanshu", 'abcd@pw.live', 1234567890)
ob_DSM2 = DSM('krish naik', "efgh@pw.live", 1231231234)

print(ob_DSM1.print_DSM())

# to print outside of the class mentor
print("name: ",ob_DSM1.mentor_name)
print("email_id: ",ob_DSM1.mentor_email_id)
print("cantact: ",ob_DSM1.mentor_contact,'\n')

print("name: ",ob_DSM2.mentor_name)
print("email_id: ",ob_DSM2.mentor_email_id)
print("cantact: ",ob_DSM2.mentor_contact,'\n')

# to print inside of the class 'mentor'
print(ob_DSM1.mentor_details(),'\n')
print(ob_DSM2.mentor_details(),'\n')
print(".................................................................................\n")



"""
    constructor over-riding
    when both parent and child classes have init() then init() of child class is prioritized
"""
class myClass1(mentor):
    def __init__(self):
        print( "this is class 'myClass1'" )

ob_myClass1 = myClass1()

print('ob_myClass1 --> ',ob_myClass1) # it will not give error, here, init() of myClass1 will be executed
print(".................................................................................\n")

# we can use super() to exeecute init() of parent class
class myClass2(mentor):
    def __init__(self):
        super().__init__('abcd', '1234@gmail', 12345)
        print( "this is class 'myClass2' \n" )

# we have to pass arguments, otherwise it will give error
ob_myClass2 = myClass2()
print('ob_myClass2.mentor_details() --> ',ob_myClass2.mentor_details(), '\n')
print('ob_myClass2.__dict__ --> ',ob_myClass2.__dict__) # it will not give error, here, init() of myClass1 will be executed
print(".................................................................................\n")




""" if a method of same name is present in both parent and child classes then
    by default that method will be executed, object of which class is created

    this is called method over-riding
"""
class xyz:
    def test(self):
        return "this is th part of parent class \n"

class abc(xyz):
    def test(self):
        return "this is the part of child class \n" 

# you can observe
ob_child2 = abc()
print("ob_child2.test() --> ",ob_child2.test())

ob_parent = xyz()
print("ob_parent.test() --> ",ob_parent.test())
print(".................................................................................\n")

# but using super(), we can execut the method present in parent class through the object of child class
class mno(xyz):
    def test(self):
        print('super().test() --> ',super().test())
        return "this is the part of child class\n"

# you can observe
ob_child3 = mno()
print('ob_child3.test() --> ',ob_child3.test())
print(".................................................................................\n")




