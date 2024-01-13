class employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
    def display(self):
        print(f"ID: {self.id} - Name: {self.name} - Salary: {self.salary}\n")

ob_employee  = employee(10, 'haider', 50000)
print('before any change')
ob_employee.display()
print("..................................................................\n")


# we will create a class that changes the salary of the employee on accessing his/her salary from 'employee' class
class changes:
    @staticmethod
    def increament(obj):
        obj.salary += 5000
        obj.display()

print('after the change')
changes.increament(ob_employee)
print("..................................................................\n")

