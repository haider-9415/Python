"""
    Instance Variable
"""
class pwskills:
    def __init__(self, course, duration, mentor):
        self.course = course
        self.duration = duration
        self.mentor = mentor
    
    def change(self,fname, lname, age):
        self.your_fname = fname
        self.your_lname = lname
        self.your_age = age

    def display(self):
        print(f'Course:{self.course} - Duration:{self.duration} - Mentor:{self.mentor} \n')

ob2 = pwskills('DSM','9hr','sudhanshu sir')
ob3 = pwskills('JWSD','6hr','vishwa sir')

# we can create Instance Variable outside of the class for a perticular object
ob2.validity = '18-months'
print('ob2.__dict__ --> ',ob2.__dict__ , '\n')
print('ob3.__dict__ --> ',ob3.__dict__ , '\n')
print(".....................................................................\n")

print('ob2.validity --> ',ob2.validity, '\n')
# the following will give error
# print('ob3.validity --> ',ob3.validity, '\n')
print(".....................................................................\n")

# we can delete it 
del ob2.course

print('after deleting:')
print('ob2.__dict__ --> ',ob2.__dict__ , '\n')
print(".....................................................................\n")

# we can create or change it using instance method
# instance method is the method in class to create or change the Instance Variable
ob2.change('haider', 'harry', 21)
print('after creating:')
print('ob2.__dict__ --> ',ob2.__dict__)
print(".....................................................................\n")

ob2.change('harry', 'haider', 18)
print('after changing:')
print('ob2.__dict__ --> ',ob2.__dict__)

print(".....................................................................\n")




"""
    Class Variable
"""
class Employee:

    company_name = 'infosys' # class variable

    def __init__(self, nm, sl):
        self.name = nm
        self.salary = sl
    
    @classmethod
    def class_var(cls, comp):
        cls.company_name = comp
        print('company_name --> ', cls.company_name, '\n')

emp1 = Employee('haider', 30000)
emp2 = Employee('harry', 35000)

# to access it
print('Employee.company_name --> ',Employee.company_name, '\n')
print('emp1.company_name --> ',emp1.company_name, '\n')
print('emp2.company_name --> ',emp2.company_name, '\n')
print(".....................................................................\n")

# to modify it
# we can not modify using object reference, it will create an 'Instance Variable'
Employee.company_name = 'tata-motors'
print('Employee.company_name --> ',Employee.company_name, '\n')
print(".....................................................................\n")

# we can get & modify it using class meethod 
Employee.class_var('microsoft')
print('Employee.company_name --> ',Employee.company_name, '\n')
print('emp1.company_name --> ',emp1.company_name, '\n')
print('emp2.company_name --> ',emp2.company_name, '\n')
print(".....................................................................\n")


