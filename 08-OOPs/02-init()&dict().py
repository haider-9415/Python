"""
   __init__ -->  it is an in-built-method, it is used to provide data to the class and 
   it is called 'constructor' in other wirds, we create this function when we have to 
   pass specific data for specific objects

   we have to create different objects for different data of different users

   in this, we have to create constructors using the pointer of the function and the
   pointer contains the memory address of current object, it provides to its objects 
   individual copy of the attributes to store data
   syntex --> poinetr_name.constructer_name, remember, constructer_name may be anything

"""

class pwskills:
    
    def __init__(self, course, duration, mentor): # here, self is the pointer
        
        self.course = course
        self.duration = duration
        self.mentor = mentor
    
    def display(self):
        print(f'Course:{self.course} - Duration:{self.duration} - Mentor:{self.mentor} \n')

# on craeting objects for this type of functions, we have to pass attributes which are given in the function

# ob1 = pwskills() # it will give run time error, because, we did not pass attributes

ob2 = pwskills('DSM','9hr','sudhanshu sir')
ob3 = pwskills('JWSD','6hr','vishwa sir')

# syntex to access data --> object_name.attribute_name
print("course --> ",ob2.course)
print("duration --> ",ob2.duration)
print("mentor --> ",ob2.mentor,'\n')
print(".....................................................................\n")

print("course --> ",ob3.course)
print("duration --> ",ob3.duration)
print("mentor --> ",ob3.mentor,'\n')
print(".....................................................................\n")

# similarly we can access methods 
print('ob2.display(): '), ob2.display()
print('ob2.display(): '), ob3.display()
print(".....................................................................\n")

# we can update the value of attributs
ob2.duration = '3hr'
ob2.mentor = 'James Bond'
print("course --> ",ob2.course)
print("duration --> ",ob2.duration)
print("mentor --> ",ob2.mentor,'\n')
print(".....................................................................\n")



class database:

    def __init__(pn,user_id, password) :
        pn.cons_id = user_id
        pn.cons_pass = password

ob4 = database('haider', '1234567')
ob5 = database('hanzala', '7654321')
ob6 = database('harry', '1234567')
ob7 = database('naeem', '101010101')

print("user_id --> ",ob4.cons_id)
print("password --> ",ob4.cons_pass,'\n')
print(".....................................................................\n")

print("user_id --> ",ob5.cons_id)
print("password --> ",ob5.cons_pass,'\n')
print(".....................................................................\n")

print("user_id --> ",ob6.cons_id)
print("password --> ",ob6.cons_pass,'\n')
print(".....................................................................\n")

print("user_id --> ",ob7.cons_id)
print("password --> ",ob7.cons_pass,'\n')
print(".....................................................................\n")



"""
    __dict__ --> using this function, we can see that what an object has it returns a dictionary
"""
print('ob2.__dict__ --> ',ob2.__dict__,'\n')
print('ob3.__dict__ --> ',ob3.__dict__,'\n')
print('ob4.__dict__ --> ',ob4.__dict__,'\n')
print('ob5.__dict__ --> ',ob5.__dict__,'\n')
print('ob6.__dict__ --> ',ob6.__dict__,'\n')
print('ob7.__dict__ --> ',ob7.__dict__,'\n')
print(".....................................................................\n")
