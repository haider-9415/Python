"""
    we will write a code that raise the exception if 
    input number is less than or equal to zero
"""

# age = int(input("Enter your age: "))
# try:
#     if age <= 0:
#         raise ValueError
# except:
#     print(f"\nage {age} is not possible. Enter valid age\n")
# else:
#     print(f'\nyour age is {age}\n')



""" or """
age = int(input("Enter your age: "))
try:
    if age <= 0:
        raise ValueError(f"age {age} is not possible. Enter valid age\n")
except ValueError as err:
    print('\nerr --> ', err)
else:
    print(f'\nyour age is {age}\n')

