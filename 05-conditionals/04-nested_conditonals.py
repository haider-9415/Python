""" check a no. 'n' is even or odd """

n = int(input("enter integer: "))

if n%2 == 0:
    if n == 0:
        print("n is zero")
    else:
        print("n is even")
else:
    print("n is odd")



""" check the eligibility to vote """

age = int(input("enter your age: "))
if age >= 18:

    voter_id = input("do you have a voter id card: ")
    if voter_id == 'yes':

        citizen = input("are you citizen: ")
        if citizen == 'yes':
            print("you are eligible to vote")

        else:
            print("you are not eligible to vote")

    else:
        print("you are not eligible to vote")

else:
    print("you are not eligible to vote")


