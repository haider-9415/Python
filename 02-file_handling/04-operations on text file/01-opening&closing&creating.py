"""
    syntex-1:
            obj1 = open(file_name, access_mode, encoding)

    syntex-2:
            with open(file_name, access_mode, encoding) as obj1:
                statement(s)

    file_name --> file_path + file_name + file_extension

    access_mode --> mode means the operation for which the file has to be opened
                    it consists of two things:
                    1) operation, like read, write or append, but reading opration is by default
                    2) type, it will be text file or binary file, but text file is by default
                    access modes for text file:
                    1) r --> for read only
                    2) r+ or +r --> for read and write
                    3) w --> for write only
                    4) w+ or +w --> for write and read
                    5) a --> for append only
                    6) a+ or +a --> for append and read 
    
    on using 1st & 2nd modes, the file offset is at starting, new file is not created and the existing file is not overwritten
    on using 3rd & 4th modes, the file offset is at starting, new file is created and the existing file is overwritten
    on using 3rd mode, the file offset is at ending, new file is created and the existing file is not overwritten

    this functon returns a file object called 'file handle' which is stored in the variable 'obj1'
    we can use this variable to handle the file by calling the functions defined in the python's io module

    in syntex-1, we have to close the file explicitly using close()
    in syntex-2, operations on the file works like they are working in a function ,i.e., coming outside of the 
    body of the open() is nothing but the closing of the file

    there are four attributes for file object 'obj1'
    1) name --> it returns the given path of the file
    2) mode --> it returns the mode of the file
    3) encoding --> it returns the encoding formate of the file
    4) closed --> it returns True if the file closed else returns False
"""
"""
   to close a file:
                obj1.close() --> to close the file
"""



""" the followign all are examples of 'relative path', because, you are going to a file or
    folder with respect to a folder """
obj1 = open("_file_2.txt") # it is called 'relative path', because, the file is in that folder if you opened in another folder then it will give error
print("obj1.read() --> ",obj1.read(),'\n') # to read a file , there is read()

# we can open '_file_3' present in folder 'for_practice' in folder 'operations on text file'
# to enter an inside folder, we use single dot '.'
obj2 = open(".\_for_practice\_file_3.txt")
print("obj2.read() --> ",obj2.read(),'\n')

# we can open '_file_1' present in folder 'file_handling' in folder 'operations on text file'
# to enter an outside folder, we use double dot '..'
obj3 = open("..\_file_1.txt")
print("obj3.read() --> ",obj3.read(),'\n')

""" 
    remember, to go to an outside folder, we don't need to enter its name, only double dots are enough,
    but, in case of inside folder, we have to enter its name
"""
print(".............................................................................\n\n")



""" the followign all are examples of 'absolute path' """

# we have to enter '\' with the present '\' in the path to avoid the error, if there is a chance to come an error
# or we can creat it a raw string using 'r'

# to open '_file_2'
obj4 = open('C:\\Users\\zaina\\OneDrive\\Desktop\\Files\\Basics of Python\\file_handling\\operations on text file\_file_2.txt')
print("obj4.read() --> ",obj4.read(),'\n')
# or
obj5 = open(r'C:\Users\zaina\OneDrive\Desktop\Files\Basics of Python\file_handling\operations on text file\_file_2.txt')
print("obj5.read() --> ",obj5.read(),'\n')
# similarly
obj6 = open(r'C:\Users\zaina\OneDrive\Desktop\Files\Basics of Python\file_handling\operations on text file\_for_practice\_file_3.txt')
print("obj6.read() --> ",obj6.read(),'\n')
obj7 = open(r'C:\Users\zaina\OneDrive\Desktop\Files\Basics of Python\file_handling\_file_1.txt')
print("obj7.read() --> ",obj7.read(),'\n')
print(".............................................................................\n\n")


""" access modes """
# remember, on opening an existing file in 'w' or 'w+' mode, the content of the file will be lost
# and on opening a non existing file in 'w' or 'w+' mode, the file will be created

ob1 = open("_file_2.txt",'r')
ob2 = open("_file_2.txt",'r+')
# ob3 = open("_file_2.txt",'w')
# ob4 = open("_file_2.txt",'w+')
ob5 = open("_file_2.txt",'a')
ob6 = open("_file_2.txt",'a+')


""" attributes """
# name
obj8 = open("_file_2.txt")
print("obj8.name --> ",obj8.name,'\n')
obj9 = open("..\_file_1.txt")
print("obj9.name --> ",obj9.name,'\n')
obj10 = open(r'C:\Users\zaina\OneDrive\Desktop\Files\Basics of Python\file_handling\operations on text file\_for_practice\_file_3.txt')
print("obj10.name --> ",obj10.name,'\n')
obj11 = open('C:\\Users\\zaina\\OneDrive\\Desktop\\Files\\Basics of Python\\file_handling\\operations on text file\_file_2.txt')
print("obj11.name --> ",obj11.name,'\n')
print(".............................................................................\n\n")

# mode
ob1 = open("_file_2.txt",'r')
print("ob1.mode --> ",ob1.mode,'\n')
ob2 = open("_file_2.txt",'r+')
print("ob2.mode --> ",ob2.mode,'\n')
# ob3 = open("_file_2.txt",'w')
# print("ob3.mode --> ",ob3.mode,'\n')
# ob4 = open("_file_2.txt",'w+')
# print("ob4.mode --> ",ob4.mode,'\n')
ob5 = open("_file_2.txt",'a')
print("ob5.mode --> ",ob5.mode,'\n') 
ob6 = open("_file_2.txt",'a+')
print("ob6.mode --> ",ob6.mode,'\n')
ob7 = open("_file_2.txt")
print("ob7.mode --> ",ob7.mode,'\n')
print(".............................................................................\n\n")

# encoding
obj12 = open("_file_2.txt")
print("obj12.encoding --> ",obj12.encoding,'\n')
obj13 = open("..\_file_1.txt")
print("obj13.encoding --> ",obj13.encoding,'\n')
obj14 = open(r'C:\Users\zaina\OneDrive\Desktop\Files\Basics of Python\file_handling\operations on text file\_for_practice\_file_3.txt')
print("obj14.encoding --> ",obj14.encoding,'\n')
obj15 = open('C:\\Users\\zaina\\OneDrive\\Desktop\\Files\\Basics of Python\\file_handling\\operations on text file\_file_2.txt')
print("obj15.encoding --> ",obj15.encoding,'\n')
print(".............................................................................\n\n")

# closed
obj16 = open("_file_2.txt")
print("obj16.closed --> ",obj16.closed,'\n')
obj17 = open("..\_file_1.txt")
print("obj17.closed --> ",obj17.closed,'\n')
obj17 = open(r'C:\Users\zaina\OneDrive\Desktop\Files\Basics of Python\file_handling\operations on text file\_for_practice\_file_3.txt')
print("obj17.closed --> ",obj17.closed,'\n')
obj18 = open('C:\\Users\\zaina\\OneDrive\\Desktop\\Files\\Basics of Python\\file_handling\\operations on text file\_file_2.txt')
print("obj18.closed --> ",obj18.closed,'\n')
print(".............................................................................\n\n")


""" methods for text file """
# close() --> to close a file
obj19 = open("_file_2.txt")
print("obj19 (before closing) --> ",obj19.closed,'\n')
obj19.close()
print("obj19 (after closing) --> ",obj19.closed,'\n')
print(".............................................................................\n\n")

# readable() --> to chack a file is in reading mode or not
ob8 = open("_file_2.txt")
print("ob8.readable() --> ",ob8.readable(),'\n')
ob9 = open("_file_2.txt",'r')
print("ob9.readable() --> ",ob9.readable(),'\n')
ob10 = open("_file_2.txt",'r+')
print("ob10.readable() --> ",ob10.readable(),'\n')
# ob11 = open("_file_2.txt",'w')
# print("ob11.readable() --> ",ob11.readable(),'\n')
# ob12 = open("_file_2.txt",'w+')
# print("ob12.readable() --> ",ob12.readable(),'\n')
ob13 = open("_file_2.txt",'a')
print("ob13.readable() --> ",ob13.readable(),'\n') 
ob14 = open("_file_2.txt",'a+')
print("ob14.readable() --> ",ob14.readable(),'\n')
print(".............................................................................\n\n")

# writable() --> to chack a file is in writing mode or not
ob15 = open("_file_2.txt")
print("ob15.writable() --> ",ob15.writable(),'\n')
ob16 = open("_file_2.txt",'r')
print("ob16.writable() --> ",ob16.writable(),'\n')
ob17 = open("_file_2.txt",'r+')
print("ob17.writable() --> ",ob17.writable(),'\n')
# ob18 = open("_file_2.txt",'w')
# print("ob18.writable() --> ",ob18.writable(),'\n')
# ob19 = open("_file_2.txt",'w+')
# print("ob19.writable() --> ",ob19.writable(),'\n')
ob20 = open("_file_2.txt",'a')
print("ob20.writable() --> ",ob20.writable(),'\n') 
ob21 = open("_file_2.txt",'a+')
print("ob21.writable() --> ",ob21.writable(),'\n')
print(".............................................................................\n\n")

# we can change encoding using encoding parameter
obj12 = open("_file_2.txt",encoding="utf-8")
print("obj12.encoding --> ",obj12.encoding,'\n')
obj13 = open("..\_file_1.txt",encoding="utf-16")
print("obj13.encoding --> ",obj13.encoding,'\n')
obj14 = open(r'C:\Users\zaina\OneDrive\Desktop\Files\Basics of Python\file_handling\operations on text file\_for_practice\_file_3.txt',encoding="utf-8")
print("obj14.encoding --> ",obj14.encoding,'\n')
obj15 = open('C:\\Users\\zaina\\OneDrive\\Desktop\\Files\\Basics of Python\\file_handling\\operations on text file\_file_2.txt',encoding="utf-32")
print("obj15.encoding --> ",obj15.encoding,'\n')
print(".............................................................................\n\n")



""" syntex-2 """
with open(r'C:\Users\zaina\OneDrive\Desktop\Files\Basics of Python\file_handling\_file_1.txt') as object:
    print("content: ",object.read(),'\n')
    print("readable: ",object.readable(),'\n')
    print("writable: ",object.writable(),'\n')
    print("encoding: ",object.encoding,'\n')
    print("mode: ",object.mode,'\n')
    print("closed: ",object.closed,'\n')
print("out of the block of open():")
print("closed: ",object.closed,'\n')
print(".............................................................................\n\n")



""" 
    using open() we can create a file 

    syntex --> variable = open(file-path,mode)
"""
# remember, a file is created only in writing an appending mode
# f1 = open("_file_a.txt",'r') # it will give run time error , also if we use 'r+'

# to create a file in present folder
f2 = open("_file_b.txt",'w')
# the file '_file_b' has been created in folder 'operations on text file' 

# to craete a file in outside folder
f3 = open("..\_file_c.txt",'w')
f4 = open("..\_file_d.txt",'w+')
# both '_file_c' and '_file_d' have been created in folder 'file handling'

# similarly
f5 = open("_file_e.txt",'a+')
f6 = open("..\_file_f.txt",'a')
print(".............................................................................\n\n")
