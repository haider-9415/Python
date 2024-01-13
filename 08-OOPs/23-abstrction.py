"""
   abstrction --> it can be said a skeleton defined by the manager who distributes methods amongs
                  his employees to write their codes
"""


# for abstraction, we have to import 'ABC' and 'abstractproperty' from the package 'abc'
from abc import ABC, abstractproperty


# now we will create inheritance of ABC class
class pwskills(ABC):
    # before each methods, we have to entered '@abstractproperty' and in each method we will write 'pass'
    @abstractproperty
    def DSM_class(self):
        pass

    @abstractproperty
    def mentor_name(self):
        pass

    @abstractproperty
    def class_timing(self):
        pass

    @abstractproperty
    def class_material(self):
        pass


""" each employee will make inheritance of pwskills and write codes which is given to him.
    he will work on given methods but he has to define other methods empty also
    before each method, he has to entered @property .
"""


# let us assume DSM_class() & mentor_name() are given to employee_1 to write their codes
class empl_1(pwskills):

    @property
    def DSM_class(self):
        return "it is Data Science Master class\n"
    
    @property
    def mentor_name(self):
        return "Sudhanshu sir and Krish Naik sir\n"
    
    @property
    def class_timing(self):
        pass
    
    @property
    def class_material(self):
        pass

# and class_timig() & class_material() are given to eployee_2 to write their codes
class empl_2(pwskills):

    @property
    def class_timing(self):
        return "2:00pm to 4:00pm and 6:00pm to 8:00pm \n"
    
    @property
    def class_material(self):
        return "laptop, copy and pen \n"
    
    @property
    def DSM_class(self):
        pass
    
    @property
    def mentor_name(self):
        pass


ob_empl1 = empl_1()
print("ob_empl1.DSM_class --> ",ob_empl1.DSM_class,'\n')
print("ob_empl1.mentor_name --> ",ob_empl1.mentor_name,'\n')
print("ob_empl1.class_timing --> ",ob_empl1.class_timing,'\n')
print("ob_empl1.class_material --> ",ob_empl1.class_material,'\n')
print(".................................................................................\n")


ob_empl2 = empl_2()
print("ob_empl2.class_timing --> ",ob_empl2.class_timing,'\n')
print("ob_empl2.class_material --> ",ob_empl2.class_material,'\n')
print("ob_empl2.DSM_class --> ",ob_empl2.DSM_class,'\n')
print("ob_empl2.mentor_name --> ",ob_empl2.mentor_name,'\n')
print(".................................................................................\n")