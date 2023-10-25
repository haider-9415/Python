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

# first create a file named '_file_7.txt'
print(os.rename("_file_7.txt", "_file_7_1.txt"),'\n') # it will change the name of file "_file-7" from "_file_7_1" and gice "None"



""" removing from current folder """
# first create a file named '_file_8.txt' in folder 'operations on text file'
print(os.remove("_file_8.txt"),'\n') # using reference path
os.remove(r"C:\Users\zaina\OneDrive\Desktop\Files\Basics of Python\file_handling\operations on text file\_file_9.txt") # using absolute path


""" removing from outside folder """
# first create a file named '_file_10.txt' in folder 'file_handling'
os.remove("..\_file_10.txt") # using reference path
os.remove(r"C:\Users\zaina\OneDrive\Desktop\Files\Basics of Python\file_handling\_file_11.txt") # using absolute path


""" removing from inside folder """
# first create a file named '_file_12.txt' in folder '_for_practice'
# we can use only absolute path to remove the file from inside folder
os.remove(r"C:\Users\zaina\OneDrive\Desktop\Files\Basics of Python\file_handling\operations on text file\_for_practice\_file_12.txt")