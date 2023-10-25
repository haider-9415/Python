# name = input("Enter name: ")
# print("name: ",name)

# # whatever you enter in input, input func converts oit into string
# # to add integer with 'a', we have to convert 'a' into integer
# a = input("enter an integer: ")

# b = int(a) + 4
# print("a + 4 = ",b)

# b = a + 4 # 4 can not be added with 'a' because they belong different data types
# print(b) # it will give running time error

""" we can take multiple inputs.
    for 'n' inputs, we need 'n' variables.
    if we use input().split(separator,maxsplit) then
    'separator' tells that from where the input string will be separated and
    'maxsplit' tells that how many times the string input will be separated.
    Remember 'maxsplit' should be (n-1) """
# it will separate at spaces by default
print("enter three strings separated by spaces")
c,d,e = input().split()
print('c -->',c);print('d -->',d);print('e -->',e)

# similarly
print('enter name,class_sec and subjct')
name,class_sec,subjct = input().split()
print('name -->',name);print('class&sec -->',class_sec);print('subject -->',subjct)

# it will separate at commas
print("enter two strings separated by commas")
f,g = input().split(",")
print('f -->',f);print('g -->',g)

# it will separate at commas 2 times
print("enter strings separated by commas")
h,i,j = input().split(',',2)
print('h -->',h);print('i -->',i);print('j -->',j)
