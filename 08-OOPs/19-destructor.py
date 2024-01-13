class employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
    def display(self):
        print(f"ID: {self.id} - Name: {self.name} - Salary: {self.salary}\n")

    # definig destructor
    def __del__(self):
        print('destructor called\n')

ob_employee1  = employee(10, 'haider', 50000)
ob_employee1.display()
"""
    destructor is called after interpreting all lines of the file
    whether you delete the object or not
"""
print('.....................................................\n')

ob_employee2 = ob_employee1

# ater deleting 'ob_employee1', the destructor will not be called 
del ob_employee1

# ater deleting 'ob_employee2', the destructor will be called 
del ob_employee2
