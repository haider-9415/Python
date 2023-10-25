""" syntax --> while condition:
                   statement(s)
               else:
                   statement(s)               """

""" else-statement will be executed when while-loop is executed succesfully """

# in this, for-loop will be executed succesfully,therefore, else-statement will be executed
n = 10
i = 1
while i <= n:
    print(i,end=',')
    i+=1
else:
    print("\nthe loop has been executed completely")

# in this, while-loop will not be executed succesfully,therefore, else-statement will not be executed
n = 10
i = 1
while i <= n:
    print(i,end=',')
    if i == 9:
        break
    i+=1
else:
    print("\nthe loop has been executed completely") 
print()

# summation of all numbers from 1 to 50
i = 1
sum = 0
while i <= 50:
    sum += i
    i +=1
else:
    print("summation from 1 to 50 = ",sum)

# summation of even numbers from 1 to 50
i = 1
sum = 0
while i <= 50:
    if i%2 == 0:
        sum += i
    i += 1
else:
    print("summation of even numbers from 1 to 50 = ",sum)


# summation of odd numbers from 1 to 50
i = 1
sum = 0
while i <= 50:
    if i%2 != 0:
        sum += i
    i += 1
else:
    print("summation of odd numbers from 1 to 50 = ",sum)