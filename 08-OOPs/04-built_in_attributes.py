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


# to get documentation-string --> class_name.__doc__
print('pwskills.__doc__ --> ',pwskills.__doc__ ,'\n')
print(".....................................................................\n")


# to get all data of a class in dictionary --> class_name.__doc__
print('pwskills.__dict__ --> ',pwskills.__dict__ ,'\n')
print(".....................................................................\n")


# to get class name --> class_name.__name__
print('pwskills.__name__ --> ',pwskills.__name__ ,'\n')
print(".....................................................................\n")


# to get module name of the class --> class_name.__module__
# if the class is not imported then it returns --> __main__
# if the class is imported then it returns --> module_name
print('pwskills.__module__ --> ',pwskills.__module__ ,'\n')

from classes import database
print('database.__module__ --> ',database.__module__ ,'\n')
print(".....................................................................\n")
