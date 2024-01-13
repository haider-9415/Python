"""
    we can use recursion if user enter wrong input
"""

def get_square():
    try:
        num = int(input('Enter the number: '))
        print(f'\nsquare of {num} = {num**2}\n')
    except Exception as e:
        print(f'\n{e}\n')
        
        # for recursion
        get_square()

get_square()

print('Rest of Code')

