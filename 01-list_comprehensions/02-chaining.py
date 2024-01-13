# we use chaining method when we have multiple condition

"""
if cond1:
    code1
elif cond2:
    code2
elif cond3:
    code3
else:
    code4
"""

"""
In comprehension

code1 if cond1 else code2 if cond2 else code3 if cond3 else code4
"""


num1 = int(input("enter a integer: "))
if num1 > 0:
    print(num1,"is +ve")
elif num1 < 0:
    print(num1,"is -ve")
else:
    print(num1,"is zero")
print("...........................................................\n")



num2 = int(input("enter a integer: "))
print(f"{num2} is +ve" if num2>0 else f"{num2} is -ve" if num2<0 else f"{num2} is zero")
print("...........................................................\n")




# in list comprehension

# without comprehension
list = [12,43,0,-24,12,0,-323,1]
status1 = []
for n in list:
    if n > 0:
        status1.append(f"{n} is +ve")
    elif n < 0:
        status1.append(f"{n} is -ve")
    else:
        status1.append(f"{n} is zero")
print("list --> ",list)
print("status1 --> ",status1)
print("...........................................................\n")

# with comprehension
status2 = [f"{n} is +ve" if n>0 else f"{n} is -ve" if n<0 else f"{n} is zero" for n in list]
print("status2 --> ",status2)
print("...........................................................\n")
