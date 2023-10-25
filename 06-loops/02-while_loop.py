""" syntax --> while condition:
                   statement(s)    """

""" it does not know the range of data stored in the variable, so, we have to give it to this """

n1 = int(input("Enter n: "))
m1 = int(input("Enter m: "))

# if we want to print numbers from n to m
while n1 <= m1:
    print(n1,end=',')
    n1+=1
print()


# if we want to print the series 3+7+11+15+.....+n 
n2 = int(input('Enter n: '))
j = 3;i = 1
while i <=n2:
    if i < n2:
        print(j,end='+')
    else:
        print(j)
    j+=4;i+=1 # becanuse, 7-3 = 11-7 = 15-11 = 4, therefore, j+=4



# summation of all numbers from 1 to 50
i = 1
sum = 0
while i <= 50:
    sum += i
    i +=1
print("summation of all numbers from 1 to 50 = ",sum)



# summation of even numbers from 1 to 50
i = 1
sum = 0
while i <= 50:
    if i%2 == 0:
        sum += i
    i += 1
print("summation of even numbers from 1 to 50 = ",sum)



# summation of odd numbers from 1 to 50
i = 1
sum = 0
while i <= 50:
    if i%2 != 0:
        sum += i
    i += 1
print("summation of odd numbers from 1 to 50 = ",sum)



# to find factorial of n
""" method-1 """
i = 1
n3 = int(input("enter n: "))
fact = 1
print("using method-1 ")
while i <= n3:
    fact *= i
    i += 1
print("    factorial of ",n3," = ",fact)

""" method-2 """
print("using method-2 ")
fact = 1
n4 = n3 # because, n3 becomes zero after complete iteration
while n3 > 0:
    fact *= n3
    n3 -= 1
print("    factorial of ",n4," = ",fact)



""" seperate out numbers divisible by x,y,x&y and both in range n to m ,where, n<m """
n = int(input("enter n: "))
m = int(input("enter m: "))
x = int(input("enter x: "))
y = int(input("enter y: "))
div_x = []
div_y = []
div_both = []
div_noth = []

while n <= m:
    if n%x==0 and n%y==0:
        div_both.append(n)
    if n%x == 0:
        div_x.append(n)
    if n%y == 0:
        div_y.append(n)
    if n%x!=0 and n%y!=0:
        div_noth.append(n)
    n+=1
print("all n divisible by both --> ",div_both)
print("all n divisible by x --> ",div_x)
print("all n divisible by y --> ",div_y)
print("all n divisible by nothing --> ",div_noth)
