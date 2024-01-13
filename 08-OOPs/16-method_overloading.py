class addition1:
    def add(self, n1, n2):
        return f"{n1} + {n2} = {n1 + n2}"

    def add(self, n1, n2, n3):
        return f'{n1} + {n2} + {n3} = {n1 + n2 + n3} \n'

add1 = addition1()

"""
    it will give error, because, in python, if a class has methods 
    of same name then it executes the last one and last one accepts 3 arguments
"""
# add1.add(100, 200)

""" it will not give error """
print('add1.add(100, 200, 300) --> ',add1.add(100, 200, 300))

"""
    to avoid it, use single function and conditional statements in it
"""
print("..................................................................\n")

