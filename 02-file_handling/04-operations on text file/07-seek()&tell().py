"""
    tell() --> it is used to find the position of the pointer
               it tells us the current position of the pointer
               it does not count '\n' as a single character
               the position is the byte position from the begnning
               syntex: file-object.tell()

    seek() --> it is used to give a perticular position to the pointer 
               syntex: file_object.seek(offset, reference-point)
                       offset --> it is the number by which the pointer is to be moved, it must be a +ve integer
                       reference-point --> it inddicates the starting position of the pointer, it must be zero, seek() always starts placing the pointer from 1st character

    to perform this opertaion is called "setting-offset"

    we can do this in all three modes reading, writing and appending

    there is a method seekable() which tells that we can perform "setting-offset" on a file or not, it returns boolean value
"""

ob1 = open("_file_k.txt",'r')

print("ob1.seekable() --> ",ob1.seekable(),'\n') # if it gives True then we can perform "setting-offset" operation on it
print(".......................................................................\n\n")

prev_position1 = ob1.tell()
print("previous position1: ",prev_position1)

ob1.seek(5) # it will bring the pointer to the 6th character

cur_position1 = ob1.tell()
print("current position1: ",cur_position1,'\n')

# now if we use read() on the file then it will be read from 6th character ,i.e., from second 'i' from the beginning
content1 = ob1.read()
print("content1: ")
print(content1,'\n')
print(".......................................................................\n\n")


prev_position2 = ob1.tell()
print("previous position2: ",prev_position2)

ob1.seek(26)
# we have used read() so the pointer is in ending, therefore, previous position2 = 59
# but seek() starts placing the pointer from 1st character so it will bring the pointer from 1st character to 26th character
# therefore, content2 will be printed from 2nd 's' of 2nd line

cur_position2 = ob1.tell()
print("current position2: ",cur_position2,'\n')

# now if we use read() on the file then it will be read from 27th character ,i.e., from second 's' from the beginning
content2 = ob1.read()
print("content2: ")
print(content2,'\n')
print(".......................................................................\n\n")


# the reference-piont is zero by default
prev_position3 = ob1.tell()
print("previous position3: ",prev_position3)
ob1.seek(26)
cur_position3 = ob1.tell()
print("current position3: ",cur_position3,'\n')

prev_position4 = ob1.tell()
print("previous position4: ",prev_position4)
ob1.seek(26,0)
cur_position4 = ob1.tell()
print("current position4: ",cur_position4)
content4 = ob1.read()
print("content4: ")
print(content4,'\n')
print(".......................................................................\n\n")


# the seek() always starts placing the pointer from starting
ob1.seek(5)
print("ob1.seek(5):")
print(ob1.read(),'\n')

ob1.seek(5)
print("ob1.seek(5):")
print(ob1.read(),'\n')

ob1.seek(5)
print("ob1.seek(5):")
print(ob1.read(),'\n')
ob1.close()
print(".......................................................................\n\n")




# in appending mode, the pointer will always be in ending of file
ob2 = open("_file_k.txt",'a')
prev_position5 = ob2.tell() # it will tell that the pointer is in ending, because, it is in appending mode
print("previous position5: ",prev_position5)
ob2.seek(10)
cur_position5 = ob2.tell()
print("current position5: ",cur_position5)
content5 = ob2.write(" hello") # it starts writing after last character
print("after writing: ",ob2.tell(),'\n')

prev_position6 = ob2.tell() # it will tell that the pointer is in ending, because, it is in appending mode
print("previous position6: ",prev_position6)
ob2.seek(100)
cur_position6 = ob2.tell()
print("current position6: ",cur_position6)
content6 = ob2.write("\nhello") # it starts writing after last character
print("after writing: ",ob2.tell())
ob2.close()
print(".......................................................................\n\n")




# # in writing mode, it starts writing from the character till which the seek() would bring the pointer
# ob3 = open("_file_k.txt",'w') # remember, on openning an existing file in 'w' mode, whole content of the file will be lost
# prev_position7 = ob3.tell() # it will tell that the pointer is in starting, because, it is in writing mode
# print("previous position7: ",prev_position7)
# ob3.seek(20)
# cur_position7 = ob3.tell()
# print("current position7: ",cur_position7)
# content7 = ob3.write("hello") # it starts writing from 21st character
# print("after writing: ",ob3.tell())
# ob3.close()
# print(".......................................................................\n\n")