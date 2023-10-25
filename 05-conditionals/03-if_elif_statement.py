""" between 'if' and 'else' statements, we can write multiple conditional statements
    using 'elif' statement 
    it is called 'cained conditionals'  """

per = int(input("enter percentage: "))

if 100 < per or per < 0:
    print("enter correct percentage")
elif 90 < per <= 100:
    print('your grade --> A')
elif 80 < per <= 90:
    print('your grade --> B')
elif 70 < per <= 80:
    print('your grade --> C')
elif 60 < per <= 70:
    print('your grade --> D')
elif 50 < per <= 60:
    print('your grade --> E')
elif 40 <= per <= 50:
    print('your grade --> F')
else:
    print("you are fail")



""" check input is +ve,-ve or 0 """
num1 = int(input("enter integer: "))

if num1 > 0:
    print("it is +ve")
elif num1 < 0:
    print("it is -ve")
else:
    print("it is zero")

