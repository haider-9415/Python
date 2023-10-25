# we can convert float or a astring that contains decimal, binary, octal or hexadecimal



# float --> int
fl1 = 23.5
fl2 = 345.9876
fl3 = 1.23e19 # it maens "1.23(10 raised to 4)", it is scientific form
fl4 = 2.5e-19 # it maens "2.5(10 raised to -19)"
print("float --> integer")
print("    ",fl1,"-->",int(fl1))
print("    ",fl2,"-->",int(fl2))
print("    ",fl3,"-->",int(fl3))
print("    ",fl4,"-->",int(fl4))



# string --> int
str1 = '934'  # decimal
str2 = '111100011' # binary
str3 = '0345' # octal
str4 = '3290af' #hexadecinmal
print("string --> integer")
print("    ",str1,"-->",int(str1,10)) # int(x,10) --> to convert in decimal form
print("    ",str2,"-->",int(str2,2))  # int(x,10) --> to convert in binary form
print("    ",str3,"-->",int(str3,8))  # int(x,10) --> to convert in octal form
print("    ",str4,"-->",int(str4,16)) # int(x,10) --> to convert in hexadecimal form
