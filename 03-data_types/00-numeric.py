# type-1 --> numeric data type
""" it involves integer,float and complex numbers """

# 1) integer
int1 = 12345678910
int2 = 10987654321
print(type(int1))
print(type(int2))
print(isinstance(int1,int))
print(isinstance(int2,int))

# 2) float
flt1 = 12345.6789
flt2 = 9876.54321
print(type(flt1))
print(type(flt2))
print(isinstance(flt1,float))
print(isinstance(flt2,float))

# 3) complex 
comp1 = 12+32j
comp2 = 123456789+987654321j

print(comp1.real) # it gives real part of 12+32j, .real is a in-built finc
print(comp1.imag) # it gives imaginary part of 12+32j, .imag is a in-built  func
# similarly
print(comp2.real)
print(comp2.imag)


print(type(comp1))
print(type(comp2))
print(isinstance(comp1,complex))
print(isinstance(comp2,complex))


