# before over-riding
class cl1():
    def func_cl1(self):
        return "this is function of class-1 \n"

ob_cl1 = cl1()
print('ob_cl1 --> ',ob_cl1)
print("..................................................................\n")


# after over-riding
class cl2():
    def __str__(self):
        return "this is function of class-1 \n"

ob_cl2 = cl2()
print('ob_cl2 --> ',ob_cl2)
print("..................................................................\n")

"""
    __str__ is a built in function called 'magic method' that contain memory 
    address but we can over-ride it as you can see
"""



"""
    another example
"""

# before over-riding
class cart1():
    def __init__(self, basket1, basket2, basket3):
        self.clothes = basket1
        self.electronics = basket2
        self.other = basket3

haider1 = cart1(['tshirt','pant','shoes'], ['laptop','5g-mobile'], ['chair','table'])
# print('len(haider1) --> ',len(haider1))


# after over-riding
class cart2():
    def __init__(self, basket1, basket2, basket3):
        self.clothes = basket1
        self.electronics = basket2
        self.other = basket3
    def __len__(self):
        print('total no. of items in cart:')
        return len(self.clothes) + len(self.electronics) + len(self.other)

haider2 = cart2(['tshirt','pant','shoes'], ['laptop','5g-mobile'], ['chair','table'])
print('len(haider2) --> ',len(haider2))

