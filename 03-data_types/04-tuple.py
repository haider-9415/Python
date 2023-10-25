# type-7 --> tuple
tp1 = ("delhi","1234",'lucknow',4321,4321)
tp2 = (12345) # it isb int type
tp3 = ('Hanzala',"Haider","""naeem""","Haider")
tp4 = 1,2,3,4,5
tp5 = "hanzala","haider",'naeem','naeem','#$%^&*()'

print("tp1 --> ",tp1)
print(tp1[0]);print(tp1[1]);print(tp1[2]);print(tp1[3]);print(tp1[4])
print(tp1[2][0]);print(tp1[2][1]);print(tp1[2][2]);print(tp1[2][3]);print(tp1[2][4]);print(tp1[2][5]);print(tp1[2][6])

print("tp2 --> ",tp2)

print("tp3 --> ",tp3)
print(tp3[0]);print(tp3[1]);print(tp3[2]);print(tp3[3])

print("tp4 --> ",tp4)
print(tp4[0]);print(tp4[1]);print(tp4[2]);print(tp4[3]);print(tp4[4])

print("tp5 --> ",tp5)
print(tp5[0]);print(tp5[1]);print(tp5[2]);print(tp5[3]);print(tp5[4])
print(tp5[4][0]);print(tp5[4][1]);print(tp5[4][2]);print(tp5[4][3]);print(tp5[4][4]);print(tp5[4][5]);print(tp5[4][6]);print(tp5[4][7])

print(type(tp1))
print(type(tp2))
print(type(tp3))
print(type(tp4))
print(type(tp5))
print(isinstance(tp1,tuple))
print(isinstance(tp2,tuple))
print(isinstance(tp3,tuple))
print(isinstance(tp4,tuple))
print(isinstance(tp5,tuple))

""" tuple is immutable ,i.e., any value in tuple can not changed """
# tp1[2] = 'haider' # it gives run time error
