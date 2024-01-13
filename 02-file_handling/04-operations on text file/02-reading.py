"""
   to open a file for reading, we have to open the file in one of the given modes
   1) r 2) r+/+r 3) w+/+w 4) a+/+a

   there are three methods that helps in reading the content of a file 
   1) read(n) --> it is used to read a specified number of bytes of data from a file
                  if 'n': 
                      is None, -ve or not specified then it reads whole content of the file starting from the position of the pointer
                      is +ve then it reads 'n' bytes starting from the position of the pointer
                      is a non integer value then it will give error
                  points for read():
                      1) it returns in form of a string
                      2) it starts reading form the position where the pointer is located
                      3) if two read() are run, then the second read() starts reading from the point where the first method ended
                      4) if EOF(End Of File) is encountered before obtaining size bytes, it reads only available bytes
                      5) while reading it includes '\n' and spaces as part of the string if it is run in puthon REPL
    
    2) readline(n) --> it is used to read one complete line from a file
                       if 'n':
                           is -ve or not specified then it reads whole line starting from the position of the pointer
                           is +ve then it reads 'n' bytes of the line starting from the position of the pointer
                           is a non integer value then it will give error
                       points for readline():
                           1) it returns in form of a string
                           2) it starts reading form the position where the pointer is located
                           3) if two readline() are run, then the second readline() starts reading from the point where the first readline() ended ,i.e., from second line
                           4) if EOL(End Of Lile means) is encountered before obtaining size bytes, it reads only that line doesn't read the bytes from the second line
                           5) while reading it includes '\n' and spaces as part of the string if it is run in puthon REPL

    3) readlines(n) --> it is used to read all the lines from a file
                        if 'n':
                            is None, -ve or not specified then it reads whole content of the file starting from the position of the pointer
                            is +ve then that line which has the nth character and its previous lines will become the elements of the list
                            is a non integer value then it will give error
                        points for readlines():
                            1) it returns a list of 'x' elements if there are 'x' lines in the file, where, each line is an element along with '\n' in the form of string
                            2) it starts reading form the position where the pointer is located
                            3) if 1st readlines() reads from mid of the 1st line to the mid of the 2nd line by specified 'n' then 2nd readlines() reads from begning of the 3rd line
"""


ob1 = open("_file_4.txt") # by default it is in mode 'r'
print("ob1.read():")
print(ob1.read(),'\n')
print("type(ob1.read()) --> ",type(ob1.read()),'\n')
print("....................................................................\n\n")

print("ob1.readline():")
print(ob1.readline(),'\n') # it will give empty string, because, the pointer is in ending after executing ob1.read()
# so
ob2 = open("_file_4.txt")
print("ob2.readline():")
print(ob2.readline(),'\n')
print("type(ob2.readline()) --> ",type(ob2.readline()),'\n')
print("....................................................................\n\n")

print("ob2.readlines():")
print(ob2.readlines(),'\n') # it will not give 1st and 2nd lines, beacuse, pointer is at starting of 2nd line after 'ob2.readline()' then it is at at starting of 3rd line after 'type(ob2.readline())'
# so
ob3 = open("_file_4.txt")
print("ob3.readlines():")
print(ob3.readlines(),'\n')
print("type(ob3.readlines()) --> ",type(ob3.readlines()),'\n')
print("....................................................................\n\n")




""" for read() """
# modes
ob4 = open("_file_4.txt",'r')
print("ob4.read(): ");print(ob4.read(),'\n')

ob5 = open("_file_4.txt",'r+')
print("ob5.read(): ");print(ob5.read(),'\n')

ob6 = open("_file_4.txt",'a+') # in this, the pointer goes to the ending of the file, so, there is no thing to print  
print("ob6.read(): ");print(ob6.read(),'\n')

ob7 = open("_file_5.txt",'w+') # in this, the content will be lost. Enter anything in _file_5 and run it then the whole content will be lost
print("ob7.read(): ");print(ob7.read(),'\n')
print("....................................................................\n\n")

# pointer movement
ob8 = open("_file_4.txt")
content1 = ob8.read()
content2 = ob8.read()
print("for ob8: ")
print("content1: ")
print(content1)
# after execution of content1, the pointer goes to the end, because 'n' is not defined, so, no thing will be print in content2
print("content2: ")
print(content2,'\n')

ob9 = open("_file_4.txt")
content1 = ob9.read(None)
content2 = ob9.read()
print("for ob9: ")
print("content1: ")
print(content1)
# after execution of content1, the pointer goes to the end, because 'n' is None, so, no thing will be print in content2
print("content2: ")
print(content2,'\n')

ob10 = open("_file_4.txt")
content1 = ob10.read(-6789)
content2 = ob10.read()
print("for ob10: ")
print("content1: ")
print(content1)
# after execution of content1, the pointer goes to the end, because 'n' is -ve, so, no thing will be print in content2
print("content2: ")
print(content2,'\n')

ob11 = open("_file_4.txt")
content1 = ob11.read(10000)
content2 = ob11.read()
print("for ob11: ")
print("content1: ")
print(content1)
# after execution of content1, the pointer goes to the end, because 'n' is greatest, so, no thing will be print in content2
print("content2: ")
print(content2,'\n')

ob12 = open("_file_4.txt")
content1 = ob12.read(50)
content2 = ob12.read(100000)
print("for ob12: ")
print("content1: ")
print(content1)
# after execution of content1, the pointer goes to 50th character, then the remaining content will be print in content2
print("content2: ")
print(content2,'\n')

ob13 = open("_file_4.txt")
content1 = ob13.read(50)
content2 = ob13.read()
print("for ob13: ")
print("content1: ")
print(content1)
# after execution of content1, the pointer goes to 50th character, then the remaining content will be print in content2
print("content2: ")
print(content2,'\n')

ob14 = open("_file_4.txt")
content1 = ob14.read(20)
content2 = ob14.read(40)
print("for ob14: ")
print("content1: ")
print(content1)
# after execution of content1, the pointer goes to the 20th characters, then the content from 21th char to 60th char will be print in content2
print("content2: ")
print(content2,'\n')
print("....................................................................\n\n")




""" for readline() """
# modes
ob15 = open("_file_4.txt",'r')
print("ob15.readline(): ");print(ob15.readline(),'\n')

ob16 = open("_file_4.txt",'r+')
print("ob16.readline(): ");print(ob16.readline(),'\n')

ob17 = open("_file_4.txt",'a+') # in this, the pointer goes to the ending of the file, so, there is no thing will be printed
print("ob17.readline(): ");print(ob17.readline(),'\n')

ob18 = open("_file_5.txt",'w+') # in this, the content will be lost. Enter anything in _file_5 and run it then the whole content will be lost
print("ob18.readline(): ");print(ob18.readline(),'\n')
print("....................................................................\n\n")

# pointer movement
ob19 = open("_file_4.txt")
content1 = ob19.readline()
content2 = ob19.readline()
print("for ob19: ")
print("content1: ")
print(content1)
# after execution of content1, the pointer goes to the starting of 2nd line, then it will print 2nd line through content2
print("content2: ")
print(content2,'\n')

ob20 = open("_file_4.txt")
content1 = ob20.readline(-1872)
content2 = ob20.readline()
print("for ob20: ")
print("content1: ")
print(content1)
# after execution of content1, the pointer goes to the starting of 2nd line, then it will print 2nd line through content2
print("content2: ")
print(content2,'\n')

ob21 = open("_file_4.txt")
content1 = ob21.readline(100000)
content2 = ob21.readline()
print("for ob21: ")
print("content1: ")
print(content1)
# after execution of content1, only 1st line will be print, then it will print 2nd line through content2
print("content2: ")
print(content2,'\n')

ob22 = open("_file_4.txt")
content1 = ob22.readline()
content2 = ob22.readline(100000)
print("for ob22: ")
print("content1: ")
print(content1)
# after execution of content1, only 1st line will be print, then it will print 2nd line through content2
print("content2: ")
print(content2,'\n')

ob23 = open("_file_4.txt")
content1 = ob23.readline(1000000)
content2 = ob23.readline(100000)
print("for ob23: ")
print("content1: ")
print(content1)
# after execution of content1, only 1st line will be print, then it will print 2nd line through content2
print("content2: ")
print(content2,'\n')

ob24 = open("_file_4.txt")
content1 = ob24.readline(5)
content2 = ob24.readline()
print("for ob24: ")
print("content1: ")
print(content1)
# after execution of content1, the pointer goes to 5th character, then it will print remaining content of that line through content2 does not go to 2nd line
print("content2: ")
print(content2,'\n')

ob25 = open("_file_4.txt")
content1 = ob25.readline(5)
content2 = ob25.readline(4)
print("for ob25: ")
print("content1: ")
print(content1)
# after execution of content1, the pointer goes to 5th character, then it will print 4 characters of that line through content2
print("content2: ")
print(content2,'\n')

ob26 = open("_file_4.txt")
content1 = ob26.readline(5)
content2 = ob26.readline(20)
print("for ob26: ")
print("content1: ")
print(content1)
# after execution of content1, the pointer goes to 5th character, then it will print remaining content of that line through content2 does not go to 2nd line
print("content2: ")
print(content2,'\n')

ob27 = open("_file_4.txt")
content1 = ob27.readline(20)
content2 = ob27.readline()
print("for ob27: ")
print("content1: ")
print(content1)
# after execution of content1, only 1st line will be print, then it will print 2nd line through content2
print("content2: ")
print(content2,'\n')
print("....................................................................\n\n")




""" for readlines()"""
# modes
ob28 = open("_file_4.txt",'r')
print("ob28.readlines(): ");print(ob28.readlines(),'\n')

ob29 = open("_file_4.txt",'r+')
print("ob29.readlines(): ");print(ob29.readlines(),'\n')

ob30 = open("_file_4.txt",'a+') # in this, the pointer goes to the ending of the file, so, there is no thing will be printed
print("ob30.readlines(): ");print(ob30.readlines(),'\n')

ob31 = open("_file_5.txt",'w+') # in this, the content will be lost. Enter anything in _file_5 and run it then the whole content will be lost
print("ob31.readlines(): ");print(ob31.readlines(),'\n')
print("....................................................................\n\n")

# pointer movement
ob32 = open("_file_4.txt")
content1 = ob32.readlines()
content2 = ob32.readlines()
print("for ob32: ")
print("content1: ")
print(content1)
# after execution of content1, the pointer goes to the ending of the file, then it will give empty list through content2
print("content2: ")
print(content2,'\n')

ob33 = open("_file_4.txt")
content1 = ob33.readlines(-827)
content2 = ob33.readlines()
print("for ob33: ")
print("content1: ")
print(content1)
# after execution of content1, the pointer goes to the ending of the file, because n is -ve, then it will give empty list through content2
print("content2: ")
print(content2,'\n')

ob34 = open("_file_4.txt")
content1 = ob34.readlines(None)
content2 = ob34.readlines()
print("for ob34: ")
print("content1: ")
print(content1)
# after execution of content1, the pointer goes to the ending of the file, because n is None, then it will give empty list through content2
print("content2: ")
print(content2,'\n')

ob35 = open("_file_4.txt")
content1 = ob35.readlines()
content2 = ob35.readlines(2)
print("for ob35: ")
print("content1: ")
print(content1)
# after execution of content1, the pointer goes to the ending of the file, because n is None, then it will give empty list through content2
print("content2: ")
print(content2,'\n')


ob36 = open("_file_4.txt")
content1 = ob36.readlines(16)
content2 = ob36.readlines()
print("for ob36: ")
print("content1: ")
print(content1)
# after execution of content1, 1st and 2nd line will be the elements, because nth char is in 2nd line and remaining line will become elements through content2
print("content2: ")
print(content2,'\n')

ob37 = open("_file_4.txt")
content1 = ob37.readlines(16)
content2 = ob37.readlines(20)
print("for ob37: ")
print("content1: ")
print(content1)
# after execution of content1, 1st and 2nd line will be the elements, and 3rd line only will become element through content2 because 20th char is in 3nd line 
print("content2: ")
print(content2,'\n')

ob38 = open("_file_4.txt")
content1 = ob38.readlines(16)
content2 = ob38.readlines(2000000)
print("for ob38: ")
print("content1: ")
print(content1)
# after execution of content1, 1st and 2nd line will be the elements, and the remaining lines will become element through content2
print("content2: ")
print(content2,'\n')

ob39 = open("_file_4.txt")
content1 = ob39.readlines(1600000000)
content2 = ob39.readlines(20)
print("for ob39: ")
print("content1: ")
print(content1)
# after execution of content1, the pointer goes to the ending of the file, then it will give empty list through content2
print("content2: ")
print(content2,'\n')
print("....................................................................\n\n")



""" we can use these functions in 2nd syntex of open() """
with open("_file_4.txt",'r') as object1:
    content1 = object1.read()
    print("object1.read: ")
    print(content1,'\n')

with open("_file_4.txt",'r') as object2:
    content2 = object2.readline()
    print("object2.read: ")
    print(content2,'\n')

with open("_file_4.txt",'r') as object3:
    content3 = object3.readlines()
    print("object3.read: ")
    print(content3,'\n')
print("....................................................................\n\n")




""" we can read a file character by character, line by line, etc. using traversing """

""" 
   traversing a file 

   the file object is traversable
"""

with open('_file_4.txt','r') as object:

    j = 1
    for i in object:
        print('line',j,': ',i)
        j += 1
print('\n')
print("....................................................................\n\n")

# we can use readline()
with open('_file_4.txt','r') as object:
    content1 = object.readline()
    j = 1

    while content1:
        print('line',j,': ',content1)
        content1 = object.readline()
        j += 1
print('\n')
print("....................................................................\n\n")


""" reading character by character, we will use read() """
# E.g.
s1 = "abcdefg"
print('characters in s1: ',end=" ")
for i in s1: print(i,end=", ")
print('\n')

with open('_file_4.txt','r') as object:
    content1 = object.read()
    print('content1:' )
    for i in content1: print(i,end=",")
print('\n') 
print("....................................................................\n\n")


""" reading word by word """
# we will use split() about which we have learnt earlier
# E.g.
s2 = "hi my name is hanzala"
ob_split1 = s2.split()
print('words in s2: ',end=" ")
for i in ob_split1:
    print(i,end=', ')
print('\n')

with open('_file_4.txt','r') as object:
    content2 = (object.read()).split() # first read() will be applied and then split() will be applied
    print('content2:' )
    for i in content2: print(i,end=", ")
print('\n') 

# if you have csv file then you can use it
# E.g. 
with open('_file_6.txt','r') as object:
    content3 = (object.read()).split(',') # first read() will be applied and then split() will be applied
    print('content3:' )
    for i in content3: print(i,end=", ")
print('\n') 

# using readlines(), we can obtain words of each line separatly as elements of a list
with open('_file_4.txt','r') as object:
    content4 = object.readlines() # in this, each line will be stored in content4 as an element of a list
    print('content4:' )
    j = 1
    for i in content4:
        words = i.split()
        print("words in line",j,': ',words)
        j += 1
print('\n')
print("....................................................................\n\n")


""" reading line by line """
with open('_file_4.txt','r') as object:
    content5 = object.readlines()
    print("content5: ")
    j = 1
    for i in content5:
        print("line",j," : ",i)
        j+=1
print("\n")
# to avoid the printing of '\n'
with open('_file_4.txt','r') as object:
    content6 = object.readlines()
    print("content6: ")
    j = 1
    for i in content6:
        print("line",j," : ",i,end='')
        j+=1
print("\n")

# we can use splitlines() with read()
# splitlines() splits lines and makes them elements of a list, if we pass True then it includes \n
#E.g.
s3 = """hi my name is hanzala
and what is yuor name?"""
ob_split2 = s3.splitlines()
ob_split3 = s3.splitlines(True)
print("ob_split2 --> ",ob_split2,'\n')
print("ob_split3 --> ",ob_split3,'\n')

with open('_file_4.txt','r') as object:
    content7 = (object.read()).splitlines()
    print("content7: ")
    j = 1
    for i in content7:
        print("line",j," : ",i)
        j+=1
print('\n')
# and
with open('_file_4.txt','r') as object:
    content8 = (object.read()).splitlines(True)
    print("content8: ")
    j = 1
    for i in content8:
        print("line",j," : ",i)
        j+=1
print("\n")
print("....................................................................\n\n")

    

