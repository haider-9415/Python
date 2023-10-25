""" we can write if and if-else statements in single line """

""" syntax --> if (condition):statement(s) """

""" syntax --> statement(s) if (condition) else stetement(s) 
    first statement is for if and second is for else         """


x = int(input("enter x: "))
y = int(input("enter y: "))
print("x-y = ",x-y) if(x > y) else print("y-x = ",y-x)
