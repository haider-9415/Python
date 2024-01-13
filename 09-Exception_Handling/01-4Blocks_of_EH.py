# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# div1 = num1 / num2
# print(f"{num1} / {num2} = {div1}")
# print("Rest of Code")

""" 
    if num2=0 then it will give "ZeroDivisionError"
    and the 2nd print function will not be executed
"""



""" 
    now we will use exception handling
"""
# num3 = int(input("Enter first number: "))
# num4 = int(input("Enter second number: "))
# try:
#     div2 = num3 / num4
#     print(f"{num3} / {num4} = {div2}")
# except:
#     print('there is any error in your code :(')

# print("Rest of Code")
""" 
    now if num2=0 then it will not give "ZeroDivisionError" but it 
    will print the code in except block and
    the 3rd print function will be executed
"""



"""
    if you want to handle multiple exceptions then do not specify
    any excepotion or use multiple exception blocks
"""
# num3 = int(input("Enter first number: "))
# num4 = int(input("Enter second number: "))
# try:
#     div2 = num3 / num4
#     print(f"{num3} / {num4} = {div2}")
# except ZeroDivisionError:
#     print('divide by zero is not possible :(')
# except NameError:
#     print('variable name is wrong :(')

# print("Rest of Code")



"""
    we can use multiple exceptions in one block
"""
# num3 = int(input("Enter first number: "))
# num4 = int(input("Enter second number: "))
# try:
#     div2 = num3 / num4
#     print(f"{num3} / {num4} = {div2}")
# except (ZeroDivisionError, NameError):
#     print('divide by zero is not possible :( \n or')
#     print('variable name is wrong :(')

# print("Rest of Code")



"""
    if you want that statement is printed which is related to 
    the exception then 
"""
# num3 = int(input("Enter first number: "))
# num4 = int(input("Enter second number: "))
# try:
#     div2 = num3 / num4
#     print(f"{num3} / {num4} = {div2}")
# except (ZeroDivisionError, NameError) as error:
#     print('error --> ',error)

# print("Rest of Code")



"""
    else block is executed when there is no exception
"""
# num3 = int(input("Enter first number: "))
# num4 = int(input("Enter second number: "))
# try:
#     div2 = num3 / num4
#     print(f"{num3} / {num4} = {div2}")
# except (ZeroDivisionError, NameError) as error:
#     print('error --> ',error)
# else:
#     print("\nthere is no exception :)\n")

# print("Rest of Code")



"""
    finally block is executed if any exception occures or not
"""
# num3 = int(input("Enter first number: "))
# num4 = int(input("Enter second number: "))
# try:
#     div2 = num3 / num4
#     print(f"{num3} / {num4} = {div2}")
# except (ZeroDivisionError, NameError) as error:
#     print('error --> ',error)
# else:
#     print("\nthere is no exception :)\n")
# finally:
#     print('\n----this is finally block----\n')

# print("Rest of Code")



"""
    we can use just "Exception" instead of name of the exception
"""
# num3 = int(input("Enter first number: "))
# num4 = int(input("Enter second number: "))
# try:
#     div2 = num3 / num4
#     print(f"{num3} / {num4} = {div2}")
# except Exception as error:
#     print('error --> ',error)
# else:
#     print("\nthere is no exception :)\n")
# finally:
#     print('\n----this is finally block----\n')

# print("Rest of Code")

