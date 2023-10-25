# print function is used to give output

a = 'haider'
b = 'naeem'
c = 1000
d = ['f','g','r',4,3,2]
print("a -->",a);print("b -->",b)

""" print function has some parameters 1)sep 2)end 3)file 4)flush 
    """
# using 'sep'
print("without using 'sep'")
print(a,b,c,d)
print("using sep='' ")
print(a,b,c,d,sep='') # it will not separate a,b,c and d
print("using sep=' ' ")
print(a,b,c,d,sep=' ') # it will separate a,b,c and d by spaces
print("using sep=',' ")
print(a,b,c,d,sep=',') # it will separate a,b,c and d by commas
print("using sep='-' ")
print(a,b,c,d,sep='-') # it will separate a,b,c and d by dash
print("using sep='~' ")
print(a,b,c,d,sep='~') # it will separate a,b,c and d by ~
print("using sep=';' ")
print(a,b,c,d,sep=';') # it will separate a,b,c and d by ;


# using 'end'
print("without using 'end'")
print(a,b,sep=',')
# without using 'end', it will print in next line by default
print(c)
print("using end='~'")
print(a,b,sep=',',end="~")
# with using 'end', we can control that it will print in next line or not
print(c)
print("using end=' - '")
print(a,b,sep=',',end=" - ")
print(c,d,sep=',')


# print() gives output in none type
s1 = print()
print("type(s1) -->",type(s1),'\n')

s2 = print("hanzala")
print("type(s2) -->",type(s2),'\n')

s3 = print([1,2,3,4,'a','b','c'])
print("type(s3) -->",type(s3),'\n')

s4 = print(('hanzala','naeem'))
print("type(s4) -->",type(s4),'\n')