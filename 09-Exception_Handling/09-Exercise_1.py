''' Exercise-1 '''

""" write a program that will sum numbers present in 
    the list [1, 'a', 'b', 3]

    excepted output:
                    item 'a' is not a number
                    item 'b' is not a number
                    addition of numbers = 4
"""

def sum_int_ele(given_list):
    add = 0
    for i in given_list:
        try:
            add += i
        except Exception as e:
            print(f"item '{i}' is not a number")

    return f'addition of numbers = {add}\n'


result  =sum_int_ele( [1, 'a', 'b', 3] )
print(result)
