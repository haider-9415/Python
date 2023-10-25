# type-4 --> set data type
""" order of elements in a set does not matter ,therefore, indexing is not allow in a set 
    and any element can not repeat """

st1 = {1,2,3,4,6,5,6,3,4,2,1}
st2 = {'1234','hanzala',"huzaifa","""Hanzala"""}
st3 = {} # it is a dictionary
st4 = {86010,'haider',45+987j,'&^%$##@'}
print("st1  --> ",st1);print("st2  --> ",st2);print("st3  --> ",st3);print("st4  --> ",st4);
print(type(st1))
print(type(st2))
print(type(st3))
print(type(st4))
print(isinstance(st1,set))
print(isinstance(st2,set))
print(isinstance(st3,set))
print(isinstance(st4,set))
