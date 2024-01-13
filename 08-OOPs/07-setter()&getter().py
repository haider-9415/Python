class Employee:

    def set_value(self): # setter()
        self.name = input('Enter employee name: ')
        self.salary = int(input('Enter employee salary: '))

    def get_value(self): # getter()
        print(f'\nName: {self.name} - Salary: {self.salary} \n')

emp1 = Employee()
emp2 = Employee()

# to set value
emp1.set_value()
emp1.get_value()
print(".....................................................................\n")

emp2.set_value()
emp2.get_value()
print(".....................................................................\n")



print('emp1.__dict__ --> ',emp1.__dict__)
print('emp2.__dict__ --> ',emp2.__dict__)
print(".....................................................................\n")

