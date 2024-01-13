num1 = [1,2,3,4,5,6,7,8,9,10]

# Syntex-01
# without comprehension method
print('Syntex-01')
sqr1 = []
for n in num1:
    sqr1.append(n*n)
print('without comprehension method - sqr1 --> ',sqr1)

# with comprehension method
sqr2 = [n*n for n in num1]
print('with comprehension method - sqr2 --> ',sqr2)
print("...........................................................\n")



# Syntax-02
# without comprehension method
print('Syntex-02')
even1 = []
for n in num1:
    if n%2 == 0:
        even1.append(n)
print('without comprehension method - even1 --> ',even1)

# with comprehension method
even2 = [n for n in num1 if n%2 == 0]
print('with comprehension method - even2 --> ',even2)
print(".................................................................\n")



# Syntax-03
# without comprehension method
print('Syntex-03')
divBy2and3_1 = []
for n in num1:
    if n%2==0 and n%3==0:
        divBy2and3_1.append(n)
print('without comprehension method - divBy2and3_1 --> ',divBy2and3_1)

# with comprehension method
divBy2and3_2 = [n for n in num1 if n%2==0 if n%3==0]
print('with comprehension method - divBy2and3_2 --> ',divBy2and3_2)
print(".................................................................\n")



# Syntax-04
# without comprehension method
print('Syntex-04')
arr1 = []
for n in num1:
    if n%2==0:
        arr1.append(n*2)
    else:
        arr1.append(n*3)
print('without comprehension method - arr1 --> ',arr1)

# with comprehension method
arr2 = [n*2 if n%2==0 else n*3 for n in num1]
print('with comprehension method - arr2 --> ',arr2)
print(".................................................................\n")



# Syntax-05
# without comprehension method
list1 = []
for i in range(3,7):
    for j in range(5,8):
        list1.append(i*j)
print('without comprehension method - list1 --> ',list1) 

# with comprehension method
list2 = [i*j for i in range(3,7) for j in range(5,8)]
print('with comprehension method - list2 --> ',list2) 
print(".................................................................\n")
