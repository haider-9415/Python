"""
    OS module, it has some built-in methods that help us to perform the file operations such as renaming & deleting
    but we need to import this module first

    rename() --> it is used to change the name of a file
                 syntex: os.rename(old-name, new-name)
    
    remove() --> it is used to delete a file
                 syntex: os.remove(path of the file)

    both methods return 'None'
"""

import os

# first create a file named 'bin_file_11.dat'
print(os.rename("bin_file_11.dat", "bin_file_11_1.dat"),'\n') # it will change the name of file "bin_file_11" from "bin_file_11_1" and give "None"




""" removing from current folder """
# first create a file named 'bin_file_12.dat' in folder 'operations on text file'
print(os.remove("bin_file_12.dat"),'\n') # using reference path
# first create a file named 'bin_file_13.dat' in folder 'operations on text file'
os.remove(r"C:\Users\zaina\OneDrive\Desktop\Files\Basics of Python\file_handling\operations on binary file\bin_file_13.dat") # using absolute path



""" removing from outside folder """
# first create a file named '_file_g' in folder 'file_handling'
os.remove(r"..\_file_g.dat") # using reference path
# first create a file named '_file_h' in folder 'file_handling'
os.remove(r"C:\Users\zaina\OneDrive\Desktop\Files\Basics of Python\file_handling\_file_h.dat") # using absolute path



""" removing from inside folder """
# first create a file named 'bin_file_1.dat' in folder 'for practice'
# we can use only absolute path to remove the file from inside folder
os.remove(r"C:\Users\zaina\OneDrive\Desktop\Files\Basics of Python\file_handling\operations on binary file\for practice\bin_file_1.dat")




""" we can convert .dat file in .txt file and vice-versa 
    remember the name of both file must be same        """

# first create a file named 'file1.dat'
os.rename("file1.dat","file1.txt")

# similarly
# first create a file named 'file2.txt'
os.rename("file2.txt","file2.dat")

