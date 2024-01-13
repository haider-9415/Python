"""
   polymorphism --> 'poly' means 'multiple' and 'morphism' means 'behavior'
   E.g. infront of your parents, you behave like their child
        infront of your friends, you behave like a friend and etc.
   so this is called polymorphism

   in term of programming, it refers to methods/functions/operators with the same name that can be 
                           executed on many objects or classes.
"""
def add(x , y):
    return x+y

print(add(100, 200),'\n') # here, add() is working for addition operation
print(add("hanzala ", " naeem"),'\n') # here, add() is working for concatination operation
""" you can see same function behaves differently for different operations 
    so this is called 'polymorphism'                                        
"""
print(".................................................................................\n")



""" polymorphism in function"""
# example-1
class cl1:
    def test(self):
        return "this is cl1\n"
class cl2:
    def test(self):
        return "this is cl2\n"  
    
def test(x):
    return x.test()

ob_cl1 = cl1()
ob_cl2 = cl2()

print("test(ob_cl1) --> ",test(ob_cl1))
print("test(ob_cl2) --> ",test(ob_cl2))
""" you can see that the test() is working for multiple classes
    on passing object of class cl1, it is working for class cl1 and
    on passing object of class cl2, it is working for class cl2
"""
print(".................................................................................\n")

# example-2
class BMW:
    def name(self):
        print('BMW:')
    def fuel_type(self):
        print('Diesel')
    def max_speed(self):
        print('max speed: 200\n')

class Ferrari:
    def name(self):
        print('Ferrari:')
    def fuel_type(self):
        print('Petrol')
    def max_speed(self):
        print('max speed: 180\n') 
    
def car_details(obj):
    obj.name()
    obj.fuel_type()
    obj.max_speed()

ob_bmw = BMW()
ob_ferrari = Ferrari()

car_details(ob_bmw)
car_details(ob_ferrari)
print(".................................................................................\n")



"""
    example of polymorphism in built-in-functions
"""

# len()
# for string, it calculates no. of characters
print("len('abcd1234') --> ",len('abcd1234'), '\n')

# for list, it calculates no. of elements whether each element has more than one characters
print("len(['a', 'bcd',123]) --> ",len(['a', 'bcd',123]), '\n')

# for dictionary, it calculates no. of keys whether each key has more than one characters
print("len({1:'a',2:'b','c':3}) --> ",len({1:'a',2:'b','c':3}), '\n')
print(".................................................................................\n")




"""
    polymorphism with inheritance
"""
class vehical:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def get_details(self):
        print(f"Name: {self.name} - Color: {self.color} - Price: {self.price}", '\n')
    
    def max_speed(self):
        print("max speed liit is 120 \n")
    
    def gear(self):
        print('gear change is 5 \n')

class car(vehical):
    def max_speed(self):
        print("max speed liit is 180 \n")

    def gear(self):
        print('gear change is 7 \n')


ob_vehical = vehical('truck', 'red', '12,00,000')
ob_car = car('mustang', 'back', '1,12,00,000')

ob_vehical.get_details()
ob_car.get_details()

ob_vehical.max_speed()
ob_car.max_speed()

ob_vehical.gear()
ob_car.gear()

"""
    you can see that max_speed() & gear() are behaving differently for objects of
    different classes
"""
print(".................................................................................\n")
