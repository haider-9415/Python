# we can pass function as a parameter or argument

def hello():
    print('this is "hello" function \n')

def demo(func):
    func()
    print('func --> ',func)

hello()

demo(hello)

print('hello --> ',hello)
print('......................................................................\n')



# another example
def Bonus():
    bonus = 2000
    return bonus

def TotalSalary(b):
    salary = 30000
    Total = b() + salary
    print('Total salary: ', Total)

TotalSalary(Bonus)
print('......................................................................\n')



