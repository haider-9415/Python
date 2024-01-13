"""
   to open a file for writing, we have to open the file in one of the given modes
   1) w 2) r+/+r 3) w+/+w 4) a+/+a 5) a
   in w, w+ or +w modes, the content of existing file will be overwrited, i.e., its whole content will be lost

   there are two methods that helps in writing the content of a file
   1) write() --> points for write():
                    1) it accepts only string as input, but by typecasting using str(), we can give anything as input
                    2) we have to enter '\n' to mark EOL(End Of Line)
                    3) if two write() are run, then the second write() starts writing from the point where the first method ended
                    4) the content written by write() is in primery memory, so, we have to close the file to save the content in secondary memory
                    5) after using once close(), we can't enter any data in that file, so, we use flush() rather than close()
                    6) it returns the number of characters in a string, remember, \n is treated as a single character
    
    2) writelines() --> points for writelines():
                          1) it accepts an iterable object containing strings, but by typecasting using str(), we can give anything as input
                          2) we have to enter '\n' to mark EOL(End Of Line)
                          3) if two write() are run, then the second write() starts writing from the point where the first method ended
                          4) the content written by write() is in primery memory, so, we have to close the file to save the content in secondary memory
                          5) after using once close(), we can't enter any data in that file, so, we use flush() rather than close()
                          6) it returns None
"""

ob1 = open("_file_g.txt",'w') # a file named '_file_g' will be created in folder 'operations on text file'

# content1 = ob1.read() # it will give error, because, the file has been opened in write only mode
# print(content1)
# print("....................................................................\n\n")



""" write() """
content2 = ob1.write("This is a text file named '_file_g'.\n") # it will be written in 1st line
print("content2 --> ",content2,'\n') # it will give no. of characters in the string "this is a text file named '_file_g'."
print("....................................................................\n\n")

# # we have to close it to save the content permanently, so
# ob1.close()
# # now the writing operation on the file '_file_g' will not working. it will give error
# content3 = ob1.write("I welcom you all to magnet brains\n")

# therefore, we use flush()
ob1.flush()
# also now the writing operation on the file '_file_g' will working. it will not give error
content4 = ob1.write("The magnet brains is an ed-tech platform\n")

# on using multiple write()
ob1.write("Hi, i am haider, ") # it will be written in 3rd line of '_file_g'
ob1.write("i am a student of class 12th.\n") # it will also be written in 3rd line of '_file_g' after "Hi, i am haider. "
ob1.write("I am learning computer science from magnet brains ") # it will be written in 4th line of '_file_g', because, we have used '\n' in end of 3rd line
ob1.write("that provides free and quality education to all.\n") # it will also be written in 4th line of '_file_g', because, we have not used '\n' in end of its previous content
ob1.flush()


# # remember,on openning an existing file in mode 'w', its all content will be overwritten
# ob2 = open("_file_g.txt",'w') # now all previous content of "_file_g" will be lost and "abcdefg123456" will be written in "_file_g"
# ob2.write("abcdefg123456")
# ob2.close()


# # the following will give error
# ob1.write(1235)
# ob1.write(-928)
# ob1.write(0)
# ob1.write(82.9021)
# ob1.write(-29.38)
# ob1.write(82+912j)
# ob1.write((1,2,3,4,5,6))
# ob1.write([10,20,30,40])
# ob1.write({100,200,300,400,500})
# ob1.write({1:'a',2:'b',3:'c'})
# ob1.write(('1','2','3','4','5','6'))
# ob1.write(['10','20','30','40'])
# ob1.write({'100','200','300','400','500'})
# ob1.write({'1':'a','2':'b','3':'c'})

# we have to use str() or qoutes
ob1.write(str(1235)) ;ob1.write('  1235\n') # it will be written in 5th line
ob1.write(str(-928)) ;ob1.write('  -928\n') # it will be written in 6th line
ob1.write(str(0)) ;ob1.write("  0\n") # it will be written in 7th line
ob1.write(str(82.9021)) ;ob1.write("  82.9021\n") # it will be written in 8th line
ob1.write(str(-29.38)) ;ob1.write("""  -29.38\n""") # it will be written in 9th line
ob1.write(str(82+912j) );ob1.write('  82+912j\n') # it will be written in 10th line
ob1.write(str((1,2,3,4,5,6))) ;ob1.write('''  (1,2,3,4,5,6)\n''') # it will be written in 11th line
ob1.write(str([10,20,30,40])) ;ob1.write("  [10,20,30,40]\n") # it will be written in 12th line
ob1.write(str({100,200,300,400,500})) ;ob1.write('''  {100,200,300,400,500}\n''') # it will be written in 13th line
ob1.write(str({1:'a',2:'b',3:'c'})) ;ob1.write("""  {1:'a',2:'b',3:'c'}\n""") # it will be written in 14th line



""" writelines() """
ob2 = open("_file_h.txt",'w')

content5 = ob2.writelines("This is a text file named '_file_h'.\n") # it will be written in 1st line
print("content5 --> ",content5,'\n') # it will give None
print("....................................................................\n\n")

# # we have to close it to save the content permanently, so
# ob2.close()
# # now the writing operation on the file '_file_h' will not work, it will give error
# content6 = ob2.writelines("I welcom you all to magnet brains\n")

# therefore, we use flush()
ob2.flush()
# also now the writing operation on the file '_file_h' will work, it will not give error
content7 = ob2.writelines("The magnet brains is an ed-tech platform\n")

# on using multiple writelines()
ob2.writelines("Hi, i am haider, ") # it will be written in 3rd line of '_file_h'
ob2.writelines("i am a student of class 12th.\n") # it will also be written in 3rd line of '_file_h' after "Hi, i am haider. "
ob2.writelines("I am learning computer science from magnet brains ") # it will be written in 4th line of '_file_h', because, we have used '\n' in end of 3rd line
ob2.writelines("that provides free and quality education to all.\n") # it will also be written in 4th line of '_file_h', because, we have not used '\n' in end of its previous content
ob2.flush()

# # remember,on openning an existing file in mode 'w', its all content will be overwrtied
# ob3 = open("_file_h.txt",'w') # now all privious content of "_file_h" will be lost and "abcdefg123456" will be written in "_file_h"
# ob3.write("abcdefg123456")
# ob3.close()

# the following will not give error, consider them
ob2.writelines(('1','2','3','4','5','6','\n')) # it will be writen in 5th line in file "_file_h"
ob2.writelines(['10','20','30','40','\n']) # it will be writen in 6th line in file "_file_h"
ob2.writelines({'100','200','300','400','500'}) # it will be writen in 7th line in file "_file_h"
ob2.writelines({'\n1':'a','2':'b','3':'c'}) # it will be writen in 8th line in file "_file_h"
# smilarly
ob2.writelines(['\n','this ','is ','from ',' list'])
ob2.writelines(('\n','this ','is ','from ',' tuple\n'))
ob2.writelines({'this ','is ','from ',' set'})
ob2.writelines({'\nthis':1,' is':2,' from':3,' dict':4})
ob2.writelines('\n')

# the following will give error
# ob2.writelines(1235)
# ob2.writelines(-928)
# ob2.writelines(0)
# ob2.writelines(82.9021)
# ob2.writelines(-29.38)
# ob2.writelines(82+912j)
# ob2.writelines((1,2,3,4,5,6))
# ob2.writelines([10,20,30,40])
# ob2.writelines({100,200,300,400,500})

# we have to use str() or qoutes
ob2.writelines(str(1235)) ;ob2.writelines('  1235\n') # it will be written in 13th line
ob2.writelines(str(-928)) ;ob2.writelines('  -928\n') # it will be written in 14th line
ob2.writelines(str(0)) ;ob2.writelines("  0\n") # it will be written in 15th line
ob2.writelines(str(82.9021)) ;ob2.writelines("  82.9021\n") # it will be written in 16th line
ob2.writelines(str(-29.38)) ;ob2.writelines("""  -29.38\n""") # it will be written in 17th line
ob2.writelines(str(82+912j) );ob2.writelines('  82+912j\n') # it will be written in 18th line
ob2.writelines(str((1,2,3,4,5,6))) ;ob2.writelines('''  (1,2,3,4,5,6)\n''') # it will be written in 19th line
ob2.writelines(str([10,20,30,40])) ;ob2.writelines("  [10,20,30,40]\n") # it will be written in 20th line
ob2.writelines(str({100,200,300,400,500})) ;ob2.writelines('''  {100,200,300,400,500}\n''') # it will be written in 21th line
ob2.writelines(str({1:'a',2:'b',3:'c'})) ;ob2.writelines("""  {1:'a',2:'b',3:'c'}\n""") # it will be written in 22th line
