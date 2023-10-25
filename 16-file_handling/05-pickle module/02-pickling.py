"""
    first we have to open the file and the file should be opened in one of the following modes
    1) rb+ 2) wb 3) wb+ 4) ab 4) ab+

    on using 2nd mode, the offset is at starting, a new file is created and the existing file is overwritten 

    syntex of dump() --> pickle.dump(python-object, file-object)
                         python-object --> it is that object which we need to dump like list,tuple,etc.
                         file-object --> it is that object of file where we need to dump the python object
    
    note --> like write(), we have to use close() or flush() to save the content permanently
             it returns None
             it writes one object at a time

"""

import pickle as pkl

# file-object
ob1 = open("bin_file_1.dat",'wb')

# python-objects
s1 = "abcdefghi%$$^^*()!@#$%~<>?:|}\n||\\1234567899+_-+="
b1 = True
b2 = False
d1 = {"a":"apple",'b':"ball","c":'cat'}
l1 = ['1','2','3','4','5','6','7','8','9','10']
t1 = ('a','b','c','d','e','f','g')
st1 = {'hanzala','haider','naeem'}
i1 = 1234
i2 = -28373
i3 = 0
f1 = 782.032
f2 = -39.7712
f3 = 0.0
c1 = 67+42j
c2 = -98+78j
c3 = 86-12j
c4 = -98-86j
n = None

pkl.dump(s1,ob1);pkl.dump(b1,ob1);pkl.dump(b2,ob1);pkl.dump(d1,ob1);pkl.dump(l1,ob1);pkl.dump(t1,ob1);
pkl.dump(st1,ob1);pkl.dump(i1,ob1);pkl.dump(i2,ob1);pkl.dump(i3,ob1);pkl.dump(f1,ob1);pkl.dump(f2,ob1);
pkl.dump(f3,ob1);pkl.dump(c1,ob1);pkl.dump(c2,ob1);pkl.dump(c3,ob1);pkl.dump(c4,ob1);pkl.dump(n,ob1);


# similarly
d2 = {"a":2,'b':3,10:'cat'}
l2 = [1,2,3,4,-5,6,-7,8.9,-9.84,10+9j]
t2 = (-1,2.959,3,-4.596,5098,6,7,-8,-9,10-93j)
st2 = {1929,92191,-1229,0912.129,111-81j}
pkl.dump(d2,ob1);pkl.dump(l2,ob1);pkl.dump(t2,ob1);pkl.dump(st2,ob1)

d3 = {12:2,-223:3,10:-282}
l3 = [1,2,3,'abcd',-5,6,-7,8.9,-9.84,10+9j,[1,2,3,4]]
t3 = (-1,2.959,3,-4.596,5098,6,7,-8,-9,10-93j,(1,2,3),[8463,393,'hiswhu'])
st3 = {1929,92191,-1229,0912.129,111-81j,'293','jiwjdd'}
pkl.dump(d3,ob1);pkl.dump(l3,ob1);pkl.dump(t3,ob1);pkl.dump(st3,ob1)



# # the following will give error
# # file-object
# ob1 = open("bin_file_1.dat",'w')
# pkl.dump(s1,ob1);pkl.dump(b1,ob1);pkl.dump(b2,ob1);pkl.dump(d1,ob1);pkl.dump(l1,ob1);pkl.dump(t1,ob1);
# pkl.dump(st1,ob1);pkl.dump(i1,ob1);pkl.dump(i2,ob1);pkl.dump(i3,ob1);pkl.dump(f1,ob1);pkl.dump(f2,ob1);
# pkl.dump(f3,ob1);pkl.dump(c1,ob1);pkl.dump(c2,ob1);pkl.dump(c3,ob1);pkl.dump(c4,ob1);pkl.dump(n,ob1);



# we can use for loop to avoid writing dump() multiple times
# enter all different type of objects in list as its elements and then implement a loop
ob2 = open("bin_file_3.dat",'wb+')
n = [62623,'hanzala',12-93j,81.918,-19201,0,True,None,(1,2,3),[1,2,3],{1,2,3},{1:2,3:4}]
for i in n:
    pkl.dump(i,ob2)


