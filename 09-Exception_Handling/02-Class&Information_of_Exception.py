"""
    any exception has its own class and that is called 'class of exception'

    information about the exception is called 'information of exception'

"""

# num3 = int(input("Enter first number: "))
# num4 = int(input("Enter second number: "))
# div2 = num3 / num4
# print(f"{num3} / {num4} = {div2}")
# print("Rest of Code")

""" if you assign num4 as zero in the above code then it will return 
    ZeroDivisionError: division by zero, in this, 
    'ZeroDivisionError' is the class of the exception and 
    'division by zero' is the information of the class
"""



""" 
    using __class__, we can get the class of the exception 
"""
# num3 = int(input("Enter first number: "))
# num4 = int(input("Enter second number: "))
# try:
#     div2 = num3 / num4
#     print(f"{num3} / {num4} = {div2}")
# except Exception as error:
#     print('error --> ',error)
#     print('error.__class__ --> ',error.__class__)
# else:
#     print("\nthere is no exception :)\n")
# finally:
#     print('\n----this is finally block----\n')

# print("Rest of Code")




""" or we can use exc_info()[0] in 'sys' module """
# import sys
# num3 = int(input("Enter first number: "))
# num4 = int(input("Enter second number: "))
# try:
#     div2 = num3 / num4
#     print(f"{num3} / {num4} = {div2}")
# except:
#     print('sys.exc_info()[0] --> ',sys.exc_info()[0])
# else:
#     print("\nthere is no exception :)\n")
# finally:
#     print('\n----this is finally block----\n')

# print("Rest of Code")




""" 
    to get exception information, use exc_info()[1] in 'sys' module 
"""
import sys
num3 = int(input("Enter first number: "))
num4 = int(input("Enter second number: "))
try:
    div2 = num3 / num4
    print(f"{num3} / {num4} = {div2}")
except:
    print('sys.exc_info()[1] --> ',sys.exc_info()[1])
else:
    print("\nthere is no exception :)\n")
finally:
    print('\n----this is finally block----\n')

print("Rest of Code")



"""
    if there are more than one exception then it shows the exception
    which takes place first
"""

