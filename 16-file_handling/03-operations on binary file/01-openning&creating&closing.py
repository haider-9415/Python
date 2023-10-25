"""
   operations performing on a binary file could be performed on a text file at binary level using encode method

   a file with the extension ".dat" is a binary file

   there are two ways to open a file
    syntex-1:
            obj1 = open(file_name, access_mode, encoding)

    syntex-2:
            with open(file_name, access_mode, encoding) as obj1:
                statement(s)

    file_name --> file_path + file_name + file_extension

    this functon returns a file object called 'file handle' which is stored in the variable 'obj1'
    we can use this variable to handle the file by calling the functions defined in the python's io module

    in syntex-1, we have to close the file explicitly using close()
    in syntex-2, operations on the file works like they are working in a function ,i.e., coming outside of the 
    body of the open() is nothing but the closing of the file

    access_mode --> mode means the operation for which the file has to be opened
                    it consists of two things:
                    1) operation, like read, write or append, but reading opration is by default
                    2) type, it will be text file or binary file, for binary file, we have to spesify 'b'
                    access modes for text file:
                    1) rb/br --> for reading only
                    2) rb+/+rb/r+b/b+r/br+/+br --> for reading and writing
                    3) wb/bw --> for writing only
                    4) wb+/+wb/w+b/b+w/bw+/+bw --> for writing and read
                    5) ab/ba --> for appending only
                    6) ab+/+ab/a+b/b+a/ba+/+ba --> for appending and reading 

    on using 1st & 2nd modes, the file offset is at starting, new file is not created and the existing file is not overwritten
    on using 3rd & 4th modes, the file offset is at starting, new file is created and the content of existing file is overwritten
    on using 3rd mode, the file offset is at ending, new file is created and the content of existing file is not overwritten

    there are four attributes for file object 'obj1'
    1) name --> it returns the given path of the file
    2) mode --> it returns the mode of the file
    3) encoding --> on using it, an error will come
    4) closed --> it returns True if the file closed else returns False
"""

"""
   to close a file:
        obj1.close() --> to close the file
"""


""" creation """
# for creation, we can use 3rd, 4th, 5th and 6th modes

# text file at binary level
ob1 = open("text_file_1.txt",'wb')
ob2 = open("text_file_2.txt",'wb+')
ob3 = open("text_file_3.txt",'ab')
ob4 = open("text_file_4.txt",'ab+')

# binary file
ob5 = open("bin_file_1.dat",'wb')
ob6 = open("bin_file_2.dat",'wb+')
ob7 = open("bin_file_3.dat",'ab')
ob8 = open("bin_file_4.dat",'ab+')

# attributes
print("ob1.name --> ",ob1.name,'\n')
print("ob2.name --> ",ob2.name,'\n')
print("ob3.name --> ",ob3.name,'\n')
print("ob4.name --> ",ob4.name,'\n')
print("ob5.name --> ",ob5.name,'\n')
print("ob6.name --> ",ob6.name,'\n')
print("ob7.name --> ",ob7.name,'\n')
print("ob8.name --> ",ob8.name,'\n')
print("....................................................\n\n")

print("ob1.mode --> ",ob1.mode,'\n')
print("ob2.mode --> ",ob2.mode,'\n')
print("ob3.mode --> ",ob3.mode,'\n')
print("ob4.mode --> ",ob4.mode,'\n')
print("ob5.mode --> ",ob5.mode,'\n')
print("ob6.mode --> ",ob6.mode,'\n')
print("ob7.mode --> ",ob7.mode,'\n')
print("ob8.mode --> ",ob8.mode,'\n')
print("....................................................\n\n")

# # the following will give error
# print("ob1.encoding --> ",ob1.encoding,'\n')
# print("ob2.encoding --> ",ob2.encoding,'\n')
# print("ob3.encoding --> ",ob3.encoding,'\n')
# print("ob4.encoding --> ",ob4.encoding,'\n')
# print("ob5.encoding --> ",ob5.encoding,'\n')
# print("ob6.encoding --> ",ob6.encoding,'\n')
# print("ob7.encoding --> ",ob7.encoding,'\n')
# print("ob8.encoding --> ",ob8.encoding,'\n')
# print("....................................................\n\n")

# on using flush(), the file doesn't close, therefore, all of the following will give false
print("ob1.closed --> ",ob1.closed,'\n')
print("ob2.closed --> ",ob2.closed,'\n')
ob3.flush()
print("ob3.closed --> ",ob3.closed,'\n')
print("ob4.closed --> ",ob4.closed,'\n')
print("ob5.closed --> ",ob5.closed,'\n')
ob6.flush()
print("ob6.closed --> ",ob6.closed,'\n')
print("ob7.closed --> ",ob7.closed,'\n')
ob8.flush()
print("ob8.closed --> ",ob8.closed,'\n')
print("....................................................\n\n")


""" we will use writable(), readable() and seekable() to know what we can do in a 
    specific mode and what we can't do 
"""

ob9 = open("text_file_1.txt",'rb')
ob10 = open("text_file_2.txt",'rb+')
ob11 = open("bin_file_1.dat",'rb')
ob12 = open("bin_file_2.dat",'rb+')

print("ob1.writable() --> ",ob1.writable(),'\n')
print("ob2.writable() --> ",ob2.writable(),'\n')
print("ob3.writable() --> ",ob3.writable(),'\n')
print("ob4.writable() --> ",ob4.writable(),'\n')
print("ob5.writable() --> ",ob5.writable(),'\n')
print("ob6.writable() --> ",ob6.writable(),'\n')
print("ob7.writable() --> ",ob7.writable(),'\n')
print("ob8.writable() --> ",ob8.writable(),'\n')
print("ob9.writable() --> ",ob9.writable(),'\n')
print("ob10.writable() --> ",ob10.writable(),'\n')
print("ob11.writable() --> ",ob11.writable(),'\n')
print("ob12.writable() --> ",ob12.writable(),'\n')
print("....................................................\n\n")

print("ob1.readable() --> ",ob1.readable(),'\n')
print("ob2.readable() --> ",ob2.readable(),'\n')
print("ob3.readable() --> ",ob3.readable(),'\n')
print("ob4.readable() --> ",ob4.readable(),'\n')
print("ob5.readable() --> ",ob5.readable(),'\n')
print("ob6.readable() --> ",ob6.readable(),'\n')
print("ob7.readable() --> ",ob7.readable(),'\n')
print("ob8.readable() --> ",ob8.readable(),'\n')
print("ob9.readable() --> ",ob9.readable(),'\n')
print("ob10.readable() --> ",ob10.readable(),'\n')
print("ob11.readable() --> ",ob11.readable(),'\n')
print("ob12.readable() --> ",ob12.readable(),'\n')
print("....................................................\n\n")

print("ob1.seekable(() --> ",ob1.seekable(),'\n')
print("ob2.seekable(() --> ",ob2.seekable(),'\n')
print("ob3.seekable(() --> ",ob3.seekable(),'\n')
print("ob4.seekable(() --> ",ob4.seekable(),'\n')
print("ob5.seekable(() --> ",ob5.seekable(),'\n')
print("ob6.seekable(() --> ",ob6.seekable(),'\n')
print("ob7.seekable(() --> ",ob7.seekable(),'\n')
print("ob8.seekable(() --> ",ob8.seekable(),'\n')
print("ob9.seekable(() --> ",ob9.seekable(),'\n')
print("ob10.seekable(() --> ",ob10.seekable(),'\n')
print("ob11.seekable(() --> ",ob11.seekable(),'\n')
print("ob12.seekable(() --> ",ob12.seekable(),'\n')
print("....................................................\n\n")