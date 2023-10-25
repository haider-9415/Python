"""
   we have to open a file 
                        for writing in 1)rb+/+rb 2)wb 3)wb+/+wb
                        for appending in 1)ab 2)ab+/+ab

    we use those two methods to write in binary file that we use to write in text file
    1) write()    2) writelines

    remember, we need to explicitly encode it using encode()
    syntex --> string.encode()

    each character in the string is represented by a code point, so, a string is a sequence 
    of code points
    the sequence of code points is converted into bytes for efficient storage and this
    process is known  as "encoding"
    by default, python uses utf-8 encoding

"""

""" writing """
# write()
ob1 = open("bin_file_5.dat",'wb')
# ob1.write("this is first line\n") # it will give error, because, we didn't use encode()
a = "this is first line\n".encode() # it will not give error
ob1.write(a) 

print("type(a) --> ",type(a),'\n')

# it will aslo happen with text file
ob2 = open("text_file_5.txt",'wb')
# ob1.write("this is first line\n") # it will give error, because, we didn't use encode()
b = "this is first line\n".encode() # it will not give error
ob2.write(b) 

print("type(b) --> ",type(b),'\n')


# these functions work also in this as well as we saw them working in " operation on text file " 

# # we have to close it to save the content permanently, so
# ob1.close()
# # now the writing operation on the file 'bin_file_5' not working. it will give error
# ob1.write("I welcom you all to magnet brains\n".encode())

# therefore, we use flush()
ob1.flush()
# also now the writing operation on the file 'bin_file_5' will working. it will not give error
ob1.write("The magnet brains is an ed-tech platform\n".encode())

# on using multiple write()
ob1.write("Hi, i am haider, ".encode()) # it will be written in 3rd line of 'bin_file_5'
ob1.write("i am a student of class 12th.\n".encode()) # it will also be written in 3rd line of 'bin_file_5' after "Hi, i am haider. "
ob1.write("I am learning computer science from magnet brains ".encode()) # it will be written in 4th line of 'bin_file_5', because, we have used '\n' in end of 3rd line
ob1.write("that provides free and quality education to all.\n".encode()) # it will also be written in 4th line of 'bin_file_5', because, we have not used '\n' in end of its previous content
ob1.flush()

# # remember,on openning an existing file in mode 'wb', its all content will be overwritten
ob3 = open("text_file_5.txt".encode(),'wb') # now all previous content of "text_file" will be lost and "abcdefg123456" will be written in "text_file"
ob3.write("abcdefg123456".encode())
ob3.close()

# # the following will give error
# ob1.write(1235.encode())
# ob1.write(-928.encode())
# ob1.write(0.encode())
# ob1.write(82.9021.encode())
# ob1.write(-29.38.encode())
# ob1.write(82+912j.encode())
# ob1.write((1,2,3,4,5,6).encode())
# ob1.write([10,20,30,40].encode())
# ob1.write({100,200,300,400,500}.encode())
# ob1.write({1:'a',2:'b',3:'c'}.encode())
# ob1.write(('1','2','3','4','5','6').encode())
# ob1.write(['10','20','30','40'].encode())
# ob1.write({'100','200','300','400','500'}.encode())
# ob1.write({'1':'a','2':'b','3':'c'}.encode())

# we have to use str() or qoutes
ob1.write(str(1235).encode()) ;ob1.write('  1235\n'.encode()) # it will be written in 5th line
ob1.write(str(-928).encode()) ;ob1.write('  -928\n'.encode()) # it will be written in 6th line
ob1.write(str(0).encode()) ;ob1.write("  0\n".encode()) # it will be written in 7th line
ob1.write(str(82.9021).encode()) ;ob1.write("  82.9021\n".encode()) # it will be written in 8th line
ob1.write(str(-29.38).encode()) ;ob1.write("""  -29.38\n""".encode()) # it will be written in 9th line
ob1.write(str(82+912j).encode() );ob1.write('  82+912j\n'.encode()) # it will be written in 10th line
ob1.write(str((1,2,3,4,5,6)).encode()) ;ob1.write('''  (1,2,3,4,5,6)\n'''.encode()) # it will be written in 11th line
ob1.write(str([10,20,30,40]).encode()) ;ob1.write("  [10,20,30,40]\n".encode()) # it will be written in 12th line
ob1.write(str({100,200,300,400,500}).encode()) ;ob1.write('''  {100,200,300,400,500}\n'''.encode()) # it will be written in 13th line
ob1.write(str({1:'a',2:'b',3:'c'}).encode()) ;ob1.write("""  {1:'a',2:'b',3:'c'}\n""".encode()) # it will be written in 14th line


# writelines(), in this, we have to encode each character or element
ob4 = open("bin_file_6.dat",'wb')

# ob4.writelines(['a','b','c','d'].encode()) # it will give error
ob4.writelines(['a'.encode(),'b'.encode(),'c'.encode(),'d'.encode(),'\n'.encode()]) # it will not give error
# similarly
# ob4.writelines(['a','b','c','d'].encode()) # it will give error
ob4.writelines({'1'.encode(),'2'.encode(),'3'.encode(),'4'.encode()}) # it will not give error
# ob4.writelines(['a','b','c','d'].encode()) # it will give error
ob4.writelines(('\n10'.encode(),'20'.encode(),'30'.encode(),'40\n'.encode())) # it will not give error


# # we have to close it to save the content permanently, so
# ob4.close()
# # now the writing operation on the file 'bin_file_6' will not work, it will give error
# ob4.writelines("I welcom you all to magnet brains\n")

# therefore, we use flush()
ob4.flush()
# also now the writing operation on the file 'bin_file_6' will work, it will not give error
ob4.writelines(['e'.encode(),'f'.encode(),'g'.encode(),'h'.encode(),'\n'.encode()])



""" appending """
# the file "bin_file_7.dat" has been already created, but it is not overwritten on openning in appending mode
ob5 = open("bin_file_7.dat",'a')

ob5.write("this is second line\n") # it will be written in 2nd line, because, the pointer is at the end of 2nd line
# similarly
ob5.write("this is third line ")
ob5.write("1000000000 200000000000 \n")
ob5.write("this is forth line\n")

# # we have to close it to save the content permanently, so
# ob5.close()
# # now the appending operation on the file 'bin_file_7' will not working. it will give error
# ob5.write("I welcom you all to magnet brains\n")

# therefore, we use flush()
ob5.flush()
# also now the appending operation on the file '_file_i' will working. it will not give error
ob5.write("The magnet brains is an ed-tech platform\n")

# on using multiple write()
ob1.write("Hi, i am haider, ") # it will be written in 7th line of 'bin_file_7'
ob1.write("i am a student of class 12th.\n") # it will also be written in 7th line of 'bin_file_7' after "Hi, i am haider. "
ob1.write("I am learning computer science from magnet brains ") # it will be written in 8th line of 'bin_file_7', because, we have used '\n' in end of 3rd line
ob1.write("that provides free and quality education to all.\n") # it will also be written in 8th line of 'bin_file_7', because, we have not used '\n' in end of its previous content
ob1.flush()