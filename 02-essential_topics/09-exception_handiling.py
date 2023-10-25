""" when there is an error in a code then python gives error and does not execute other 
    codes after that wrong code """
""" to avoid this situation, there is a concept that is 'exception handling'  """
""" there are three keywords used for 'exception handling' """
""" 1)try 2)except 3)finally """
""" the suspicious code is written in try block if the code is wrong then the code in 
    except block and in finally block is executed """
""" remember, there are more than one try&except blocks in a try block, except block or in a finally block """

# n = int(input("enter an integer: ")) # it is wrong if input is other than integer
# d = 10/n # it is wrong if input is zero
# """ python will give error and the code 'print("d = ",d)' will not be executed """
# print("d = ",d)


try:
    n = int(input("enter an integer: ")) 
    d = 10/n 
    print("d = ",d)
except:
    print("Error") # if n is other than integer or it is zero then this code will be executed



""" if we want what is the error then """
try:
    n = int(input("enter an integer: ")) 
    d = 10/n 
    print("d = ",d)
except Exception as e: # Exception is a class that knows cause of error
    print("Error:",e) # if there is an error in try code then it will give cause of error also



""" after these blocks, all codes are executed normally """
try:
    n = int(input("enter an integer: ")) 
    d = 10/n 
    print("d = ",d)
except Exception as e:
    print("Error:",e)
# if there is any error in try block then also following code will be executed
l = [1,2,3,4,5,6,7,8,9,10]
print("l -->",l)
for i in l:
    print(i,end=',')
print()



""" there may be more than one except blocks """
try:
    n = int(input("enter an integer: ")) 
    d = 10/n 
    print("d = ",d)
except ValueError as e:
    print("Error:",e)
except ZeroDivisionError as e: 
    print("Error:",e)
except Exception as e: 
    print("Error:",e)


