class pwskills:
    
    def __init__(self, course, duration, mentor): # here, self is the pointer
        
        self.course = course
        self.duration = duration
        self.mentor = mentor
    
    def display(self):
        print(f'Course:{self.course} - Duration:{self.duration} - Mentor:{self.mentor} \n')


ob2 = pwskills('DSM','9hr','sudhanshu sir')
ob3 = pwskills('JWSD','6hr','vishwa sir')


# to get value of attribute --> getattr(object, attribute)
print("getattr(ob2, 'course') ---> ",getattr(ob2, 'course'), '\n')
print("getattr(ob3, 'course') ---> ",getattr(ob3, 'course'), '\n')
print(".....................................................................\n")


# to set value of the attributes --> setattr(object. attribute, value)
setattr(ob2, 'duration', '4hr'), setattr(ob2, 'mentor', 'abcd1234')
print("course --> ",ob2.course)
print("duration --> ",ob2.duration)
print("mentor --> ",ob2.mentor,'\n')
print(".....................................................................\n")


# to delete the attribute --> delattr(object, attribute)
# it returns 'None'
print('ob3.__dict__ --> ',ob3.__dict__ , '\n')
delattr(ob3, 'mentor')
print('ob3.__dict__ --> ',ob3.__dict__)
print(".....................................................................\n")


# to check that an attribute 'x' is of the object 'y' or not --> hasattr(object, attribute)
# it returns true or false
print("hasattr(ob2, 'mentor') --> ",hasattr(ob2, 'mentor'), '\n')
print("hasattr(ob2, 'mentoor') --> ",hasattr(ob2, 'mentoor'), '\n')
print("hasattr(ob3, 'mentor') --> ",hasattr(ob3, 'mentor'), '\n') # it will give false because we have deleted it
print(".....................................................................\n")




