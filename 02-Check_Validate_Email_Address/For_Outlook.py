email = input("Enter Email:")

k = 0 
# email should not be less than 6 characters
if len(email) >= 6:
    # first character should be alphabet
    if email[0].isalpha():
        if "outlook" in email:
            # there should be only one "@"  
            if ("@" in email) and (email.count("@") == 1):
                # the "." should be placed at last 3rd or 4th place and sould be only one
                if (email[-4]=='.') ^ (email[-3]=='.'):
                    # any character should not be 'space' or in uppercase
                    for i in email:
                        if i == i.isspace():
                            k = 1
                        elif i.isalpha():
                            if i == i.upper():
                                k = 2
                        elif i.isdigit():
                            continue
                        elif i=="_" or i=="." or i=="@":
                            continue
                        else:
                            k = 3
                    if k != 0:
                        print('Error 6')
                    else:
                        print("\nValid Email :)\n")
                else:
                    print('Error 5')
            else:
                print('Error 4')
        else:
            print('Error 3')
    else:
        print('Error 2')    
else:
    print('Error 1')

