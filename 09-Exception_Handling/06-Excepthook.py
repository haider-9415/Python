import sys

def format_traceback(exc_type, exc_value, exc_traceback):
    print('\n---------------------- Something went wrong ----------------------\n')
    print(f'exc_type --> {exc_type} \n')
    print(f'exc_value --> {exc_value} \n')
    print(f'exc_traceback --> {exc_traceback} \n')

# overriding the function excepthook()
sys.excepthook = format_traceback

def adder():
    print(100 + "haider")

adder()

# rest of code will not be executed
print('Rest of Code')

