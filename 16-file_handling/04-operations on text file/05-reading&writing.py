"""
   to perform both operations reading & writing togather, we have to use one of the following modes
   1) r+/+r  2) w+/+w  3) a+/+a

   on using 1st mode, the file offset is at starting, new file is not created and the existing file is not overwritten
   on using 2nd mode, the file offset is at starting, new file is created and the existing file is overwritten
   on using 3rd mode, the file offset is at ending, new file is created and the existing file is not overwritten

   methods to be used:
                    for readind --> read(), readline() & readlines()
                    for writing --> write() & writelines()
"""

""" using 'r+' """
ob1 = open("_file_l.txt",'r+')

content1 = ob1.read()
print("content1:");print(content1,'\n')

ob1.write("this is second line\n") 
ob1.flush()

content2 = ob1.read()
print("content2:");print(content2,'\n') # it will show nothing, because, the pointer has reached to end after execution of "content1"
# so we will use seek() to bring the pointer in starting
ob1.seek(0)# now we can see the content of file "_file_l"
content3 = ob1.read()
print("content3:");print(content3,'\n') 

# you will be observed that the content written by write() has been written in ending but the file offset is at starting in 'r+' mode
# it is because, we have applied the read() on it due to which the pointer has came to ending

# similarly
ob1.writelines(["my ",'name ','is ',' hanzala\n','i am ','a ','class ','12th ','student'])

ob1.seek(0)
content4 = ob1.readline()
print("content4:");print(content4,'\n') 

ob1.seek(0)
content5 = ob1.readline()
print("content5:");print(content5,'\n') 
content6 = ob1.readline()
print("content6:");print(content6,'\n') 
content7 = ob1.readline()
print("content7:");print(content7,'\n') 

ob1.seek(0)
content8 = ob1.readlines()
print("content8:");print(content8,'\n')

# the both of the follwing will not give any thing of the file "_file_l", to get the content of the file, we will have to use seek() 
content9 = ob1.readline()
print("content9:");print(content9,'\n')
content10 = ob1.readlines()
print("content10:");print(content10,'\n')


# if we use seek() before writing then the content will be written in starting
# remember, it will overwrite 'n' characters from starting if you write 'n' characters
ob1.seek(0)
ob1.writelines("abcd ") # it will overwrite replace "this " from "abcd " in first line of "_file_l"
ob1.flush()
content11 = ob1.read() # after writing "abcd ", the pointer has came to 6th character, therefore it will read from 6th character 
print("content11:");print(content11,'\n')
# so
ob1.seek(0)
content12 = ob1.read() # it will read whole content
print("content12:");print(content12,'\n')

# but if we bring the pointer to a specific character and write anything then that will be written in ending  
ob1.seek(0)
ob1.read(15) # here, we have brought the pointer to the 15th character
ob1.write("\nusing read()") # but it will write in ending
# similarly
ob1.seek(0)
ob1.readline() 
ob1.write("\nusing readline()")
ob1.seek(0)
ob1.readlines(15) 
ob1.write("\nusing readlines()")

ob1.seek(0)
content13 = ob1.read()
print("content13:");print(content13,'\n')




""" using 'w+' """
ob2 = open("_file_m.txt",'w+') # a new file named "_file_m.txt" will be created

ob2.write("aaaaaaaaaaaaaa\n") # after execution of it, the pointer eill go to ending of the file
# to read it we use seek()
ob2.seek(0)
content14 = ob2.read()
print("content14:");print(content14,'\n')

# on using write() second time, it will starts writing from ending
ob2.write("bbbbbbbbbbbbb\n") 
ob2.seek(0)
content15 = ob2.read()
print("content15:");print(content15,'\n')

# on trying to write from starting, it will replace 'n' characters if you write 'n' characters
ob2.seek(0)
ob2.write("ccccccccc") 
ob2.seek(0)
content16 = ob2.read()
print("content16:");print(content16,'\n')
# similarly
ob2.seek(0)
ob2.write("dddddddddddd") 
ob2.seek(0)
content17 = ob2.read()
print("content17:");print(content17,'\n')



""" using 'a+' """
ob3 = open("_file_n.txt",'a+') # a new file named "_file_n.txt" will be created
ob3.write("this a file\n")
ob3.seek(0)
content18 = ob3.read()
print("content18:");print(content18,'\n')

# in this, the content is always written in ending
ob3.seek(0)
ob3.write("eeeeeeeeeeeeeee\n") 
ob3.seek(0)
content19 = ob3.read()
print("content19:");print(content19,'\n')

ob3.seek(15)
ob3.write("fffffffffffffff\n") 
ob3.seek(0)
content20 = ob3.read()
print("content20:");print(content20,'\n')