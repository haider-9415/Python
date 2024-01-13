"""
    we will create an exception that will be raised if 
    any is ddivided by 5
"""

""" Step-1 """
# class FiveDivisionError(Exception):
#     "this is an exception class called when the divisor is 5"
#     pass

""" Step-2 & Step-3 """
# try:
#     num1 = int(input("Enter dividend: "))
#     num2 = int(input("Enter divisor: "))
#     if num2 == 5:
#         raise FiveDivisionError('divisor must not be 5 \n')
#     quotient = num1 / num2
#     print(f'\n{num1} / {num2} = {quotient}\n')
# except (FiveDivisionError, ZeroDivisionError) as err:
#     print('\nerr --> ',err)
# finally:
#     print('\n-----------I hope you understand-----------\n')



""" we can print the information of the exception in the
    class of exception 
    for example
"""
class TenDivisionError(Exception):
    "this is an exception class called when the divisor is 5"
    def __init__(self):
        print('divisor must not be 10 \n')

try:
    num1 = int(input("Enter dividend: "))
    num2 = int(input("Enter divisor: "))
    if num2 == 10:
        raise TenDivisionError
    quotient = num1 / num2
    print(f'\n{num1} / {num2} = {quotient}\n')
except (TenDivisionError, ZeroDivisionError) as err:
    print('err --> ',err)
finally:
    print('\n-----------I hope you understand-----------\n')




