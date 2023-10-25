"""
   to open a file for appending, we have to open the file in one of the given modes
   1) a+/+a 2) a

   in appending --> the writing starts from end of the file 
                    the existing file is not overwritten
                    if we run programm 'n' times then it will append 'n' times

   we use write() and writelines() for appending

"""

# the file "_file_i" has been already created, but it is not overwritten on openning in appending mode
ob1 = open("_file_i.txt",'a')

ob1.write("this is second line\n") # it will be written in 2nd line, because, the pointer is at the end of 2nd line
# similarly
ob1.write("this is third line ")
ob1.write("1000000000 200000000000 \n")
ob1.write("this is forth line\n")

# # we have to close it to save the content permanently, so
# ob1.close()
# # now the appending operation on the file '_file_i' will not working. it will give error
# ob1.write("I welcom you all to magnet brains\n")

# therefore, we use flush()
ob1.flush()
# also now the appending operation on the file '_file_i' will working. it will not give error
ob1.write("The magnet brains is an ed-tech platform\n")

# on using multiple write()
ob1.write("Hi, i am haider, ") # it will be written in 7th line of '_file_i'
ob1.write("i am a student of class 12th.\n") # it will also be written in 7th line of '_file_i' after "Hi, i am haider. "
ob1.write("I am learning computer science from magnet brains ") # it will be written in 8th line of '_file_i', because, we have used '\n' in end of 3rd line
ob1.write("that provides free and quality education to all.\n") # it will also be written in 8th line of '_file_i', because, we have not used '\n' in end of its previous content
ob1.flush()

# the following will give error
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
ob1.write(str(1235)) ;ob1.write('  1235\n') # it will be written in 9th line
ob1.write(str(-928)) ;ob1.write('  -928\n') # it will be written in 10th line
ob1.write(str(0)) ;ob1.write("  0\n") # it will be written in 11th line
ob1.write(str(82.9021)) ;ob1.write("  82.9021\n") # it will be written in 12th line
ob1.write(str(-29.38)) ;ob1.write("""  -29.38\n""") # it will be written in 13th line
ob1.write(str(82+912j) );ob1.write('  82+912j\n') # it will be written in 14th line
ob1.write(str((1,2,3,4,5,6))) ;ob1.write('''  (1,2,3,4,5,6)\n''') # it will be written in 15th line
ob1.write(str([10,20,30,40])) ;ob1.write("  [10,20,30,40]\n") # it will be written in 16th line
ob1.write(str({100,200,300,400,500})) ;ob1.write('''  {100,200,300,400,500}\n''') # it will be written in 17th line
ob1.write(str({1:'a',2:'b',3:'c'})) ;ob1.write("""  {1:'a',2:'b',3:'c'}\n""") # it will be written in 18th line



""" writelines() """
ob2 = open("_file_j.txt",'a')

ob2.writelines("\nThis is a text file named '_file_j'.\n") # it will be written in 3rd line

# # we have to close it to save the content permanently, so
# ob2.close()
# # now the writing operation on the file '_file_j' will not work, it will give error
# ob2.writelines("I welcom you all to magnet brains\n")

# therefore, we use flush()
ob2.flush()
# also now the writing operation on the file '_file_j' will work, it will not give error
ob2.writelines("The magnet brains is an ed-tech platform\n")

# on using multiple writelines()
ob2.writelines("Hi, i am haider, ") # it will be written in 5th line of '_file_j'
ob2.writelines("i am a student of class 12th.\n") # it will also be written in 5th line of '_file_j' after "Hi, i am haider. "
ob2.writelines("I am learning computer science from magnet brains ") # it will be written in 6th line of '_file_j', because, we have used '\n' in end of 3rd line
ob2.writelines("that provides free and quality education to all.\n") # it will also be written in 6th line of '_file_j', because, we have not used '\n' in end of its previous content
ob2.flush()

# the following will not give error, consider them
ob2.writelines(('1','2','3','4','5','6','\n')) # it will be writen in 7th line in file "_file_h"
ob2.writelines(['10','20','30','40','\n']) # it will be writen in 8th line in file "_file_h"
ob2.writelines({'100','200','300','400','500'}) # it will be writen in 9th line in file "_file_h"
ob2.writelines({'\n1':'a','2':'b','3':'c'}) # it will be writen in 10th line in file "_file_h"
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
ob2.writelines(str(1235)) ;ob2.writelines('  1235\n') # it will be written in 15th line
ob2.writelines(str(-928)) ;ob2.writelines('  -928\n') # it will be written in 16th line
ob2.writelines(str(0)) ;ob2.writelines("  0\n") # it will be written in 17th line
ob2.writelines(str(82.9021)) ;ob2.writelines("  82.9021\n") # it will be written in 18th line
ob2.writelines(str(-29.38)) ;ob2.writelines("""  -29.38\n""") # it will be written in 19th line
ob2.writelines(str(82+912j) );ob2.writelines('  82+912j\n') # it will be written in 20th line
ob2.writelines(str((1,2,3,4,5,6))) ;ob2.writelines('''  (1,2,3,4,5,6)\n''') # it will be written in 21th line
ob2.writelines(str([10,20,30,40])) ;ob2.writelines("  [10,20,30,40]\n") # it will be written in 22th line
ob2.writelines(str({100,200,300,400,500})) ;ob2.writelines('''  {100,200,300,400,500}\n''') # it will be written in 23th line
ob2.writelines(str({1:'a',2:'b',3:'c'})) ;ob2.writelines("""  {1:'a',2:'b',3:'c'}\n""") # it will be written in 24th line
