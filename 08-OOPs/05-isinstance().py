"""
    it is used to chack an object 'x' is the object of class 'y' or not

    it returns true or false

    syntax --> isinstance(object, class_name)
"""

class pwskills:
    
    # it is documentation-string, it tells that what is the purpose of creating the class
    ''' this class is for maintaining the course its duration and its mentor '''

    def __init__(self, course, duration, mentor): # here, self is the pointer
        
        self.course = course
        self.duration = duration
        self.mentor = mentor
    
    def display(self):
        print(f'Course:{self.course} - Duration:{self.duration} - Mentor:{self.mentor} \n')

ob2 = pwskills('DSM','9hr','sudhanshu sir')
ob3 = pwskills('JWSD','6hr','vishwa sir')


class demo():
    pass

ob4 = demo()


print('isinstance(ob2, pwskills) --> ',isinstance(ob2, pwskills), '\n')
print(".....................................................................\n")

print('isinstance(ob2, demo) --> ',isinstance(ob2, demo), '\n')
print(".....................................................................\n")

print('isinstance(ob4, demo) --> ',isinstance(ob4, demo), '\n')
print(".....................................................................\n")

print('isinstance(ob4, pwskills) --> ',isinstance(ob4, pwskills), '\n')
print(".....................................................................\n")



