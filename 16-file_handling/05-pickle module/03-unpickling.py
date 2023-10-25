"""
    first we have to open the file in one of the following modes
    1) rb 2) rb+ 3) wb+ 5) ab+

    syntex of load() --> object = pickle.load(file-object)
                         file-object is the object of file from where we need to load the content
    
    if we use dump() 'n' times to dump 'n' objects then we will have to use load() 'n' times to get those 'n' objects
"""

import pickle as pkl

ob1 = open("bin_file_2.dat",'wb')

d1 = {"a":2,'b':3,10:'cat'}
l1 = [1,2,3,4,-5,6,-7,8.9,-9.84,10+9j]
t1 = (-1,2.959,3,-4.596,5098,6,7,-8,-9,10-93j)
st1 = {1929,92191,-1229,0912.129,111-81j}
pkl.dump(d1,ob1);pkl.dump(l1,ob1);pkl.dump(t1,ob1);pkl.dump(st1,ob1)
ob1.close()

ob2 = open("bin_file_2.dat",'rb')
content1 = pkl.load(ob2)
print('content1:');print(content1,'\n') # it will give d1 only
content2 = pkl.load(ob2)
print('content2:');print(content2,'\n') # it will give l1 only
content3 = pkl.load(ob2)
print('content3:');print(content3,'\n') # it will give t1 only
content4 = pkl.load(ob2)
print('content4:');print(content4,'\n') # it will give st1 only
# content5 = pkl.load(ob2)
# print('content5:');print(content5,'\n') # it will give error, because, after st1, there is no content
print(".....................................................\n\n")


# we can use while loop to avoid writing load() 'n' times to get 'n' objects
ob3 = open("bin_file_2.dat",'rb')
# while True:
#     print(pkl.load(ob3))
# but it will give error that we have seen in case of content5
# print(".....................................................\n\n")

# to avoid this error, we will use "exception-handiling"
print("using loop:")
try:
    while True:
        print(pkl.load(ob3))
except EOFError: # to avoid EOFError
    print()
print(".....................................................\n\n")
# you can see that there is no error