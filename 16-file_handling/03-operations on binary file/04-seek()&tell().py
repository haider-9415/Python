"""
    tell() --> it is used to find the position of the pointer
               it tells us the current position of the pointer
               it does not count '\n' as a single character
               the position is the byte position from the begnning
               syntex: file-object.tell()

    seek() --> it is used to give a perticular position to the pointer 
               syntex: file_object.seek(offset, reference-point)
                       offset --> it is the integer by which the pointer is to be moved
                                  if it is +ve then pointer moves forward
                                  if it is -ve then pointer moves backward
                       reference-point --> it inddicates the starting position of the pointer, by default it is zero
                                           if it is zero then the pointer reaches at the beginning
                                           if it is one then the pointer stays on its place
                                           if it is two then the pointer reaches at the ending

    to perform this opertaion is called "setting-offset"

    we can do this in all three modes reading, writing and appending

    there is a method seekable() which tells that we can perform "setting-offset" on a file or not, it returns boolean value
"""

ob1 = open("text_file_7.txt",'wb+')
ob1.write("this is 1st line\nthis is 2nd line\nthis is 3rd line".encode())
ob1.flush()


# when we creat a file without using python then its new line character is the combination of '\r' & '\n' 
# when we creat a file with using python then its new line character is the '\n' only
# you can see in the following example, text_file_6.txt has been created without using python andtext_file_7.txt has been created with using python
ob1 = open("text_file_7.txt",'rb')
print("ob1.readlines():");print(ob1.readlines(),'\n')
ob2 = open("text_file_6.txt",'rb')
print("ob2.readlines():");print(ob2.readlines(),'\n')
print(".......................................................................\n\n")

ob3 = open("text_file_7.txt",'rb')
print("ob3.tell() --> ",ob3.tell(),'\n')
ob3.seek(0)
print("after ob3.seek(0) --> ",ob3.tell(),'\n')
ob3.seek(0,0) # it indecates that the pointer has moved 0 character forward from begnning 
print("after ob3.seek(0,0) --> ",ob3.tell(),'\n')
ob3.seek(0,1) # it indecates that the pointer has moved 0 character forward from its current position
print("after ob3.seek(0,1) --> ",ob3.tell(),'\n')
ob3.seek(0,2) # it indecates that the pointer has moved 0 character forward from ending 
print("after ob3.seek(0,2) --> ",ob3.tell(),'\n')
ob3.seek(10,0) # it indecates that the pointer has moved 10 characters forward from begnning 
print("after ob3.seek(10,0) --> ",ob3.tell(),'\n') # it will tell that the pointer is at 10th character
ob3.seek(15,1) # it indecates that the pointer has moved 15 characters forward from its current position 
print("after ob3.seek(15,1) --> ",ob3.tell(),'\n') # it will tell that the pointer is at 25th character, due to the execution of ob3.seek(10,0)
ob3.seek(4,2)# it indecates that the pointer has moved 4 characters forward from ending 
print("after ob3.seek(4,2) --> ",ob3.tell(),'\n') # it will tell that the pointer is at 54th character, because last character is 50th
print(".......................................................................\n\n")


# # if you want to move the pointer backward from beginning then it will give error
# ob3.seek(-10,0)

# in the case of current position and last position, it will not give error
ob3.seek(0)
ob3.read(15)
print("in case of current position:")
print("previous position: ",ob3.tell(),'\n')
print("current position: ",ob3.seek(-10,1),'\n') # you will se that the pointer moves 10 characters backward
print("in case of last position:")
ob3.seek(0,2)
print("previous position: ",ob3.tell(),'\n')
print("current position: ",ob3.seek(-14,2),'\n') # you will se that the pointer moves 14 characters backward
print(".......................................................................\n\n")


# if you want to move the pointer forward from last then it will not give error
ob3.seek(0,2)
print("previous position: ",ob3.tell(),'\n')
ob3.seek(0,2)
print("current position: ",ob3.seek(10,2),'\n') # you will se that the pointer moves 10 characters forawrd
print(".......................................................................\n\n")


