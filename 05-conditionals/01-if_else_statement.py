""" syntax of 'if' statement --> if (condition):
                                     statement(s) """

""" syntax of 'if-else' statement --> if (condition):
                                          statement(s)
                                      else:
                                          statement(s)    """

price = int(input("enter price: ")) # because, input function converts input in string ,therefore, we have to convert it

if price <= 1000:
    print("i can buy a bat")
else:
    print("i can not buy a bat")


per = int(input("enter your percentage: "))

if per > 90:
    print("you may go to delhi")
else:
    print("no need to go to anywhere")