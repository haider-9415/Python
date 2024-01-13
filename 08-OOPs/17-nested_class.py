class outer:
    def __init__(self):
        print("outer class constructor called\n")
    def display(self):
        print('this is display() for outer class\n')
    
    class inner:
        def __init__(self):
            print("inner class constructor called\n")
        def show(self):
            print('this is show() for inner class\n')

ob_outer = outer()
ob_outer.display()
print("..................................................................\n")

# to create the object of inner class
ob_inner1 = ob_outer.inner()
ob_inner1.show()
print("..................................................................\n")

# if we create the object of inner class then the constructor of outer class will also be called
ob_inner1 = outer().inner()
ob_inner1.show()
print("..................................................................\n")


# we can not access thee functions of inner class using the object of outer class
# it will give error
# ob_outer.show()


"""
    we can create the object of inner class in the outer class
"""
class student:
    def __init__(self, name, roll_no, dd, mm, yy):
        self.name = name
        self.roll_no = roll_no
        # to create the object of inner class, i.e., 'DOB' class
        self.dob = self.DOB(dd, mm, yy)

    def display(self):
        print(f"Name: {self.name} - roll no.: {self.roll_no}")
        self.dob.display()

    class DOB:
        def __init__(self, dd, mm, yy):
            self.date = dd
            self.month = mm
            self.year = yy

        def display(self):
            print(f"date of birth: {self.date}-{self.month}-{self.year}\n")

ob1_student = student('haider', 211, 18, 3, 2002)
ob2_student = student('harry', 202, 12, 7, 2000)
ob3_student = student('hanzala', 199, 8, 1, 1999)

ob1_student.display()
ob2_student.display()
ob3_student.display()
print("..................................................................\n")
