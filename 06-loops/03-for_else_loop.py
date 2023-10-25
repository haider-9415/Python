""" syntax --> for i,j,etc. in variable_name:
                   statement(s)
               else:
                   statement(s)               """

""" else-statement will be executed when for-loop is executed succesfully """


# in this, for-loop will be executed succesfully,therefore, else-statement will be executed
l = [1,2,3,4,'haider',5,6,7,8,]
for i in l:
    print(i)
else:
    print("there are seven alphabets")


# in this, for-loop will not be executed succesfully due to break-statement,therefore, else-statement will not be executed
l1 = [1,2,3,4,'haider',5,6,7,8,]
for i in l1:
    print(i)
    if i == 'haider':
        break
else:
    print("there are seven alphabets")


l2 = [2321,354438,90482,9329203,8493847,923903,940340,927332,83737,9832938,93065
      ,62535,73376,93489,3048533,84856,3874727,9328475,945858]
l3 = [1,3,2,5,6,4,8,7,5,9483,80,93,8223,232]

# summation of elements of l2 
sum1 = 0
for i in l2:
    sum1 = sum1+i
else:
    print("summation of elements of l2 = ",sum1)

# summation of elements of l2 
sum2 = 0
for i in l3:
    sum2 += i
else:
    print("summation of elements of l3 = ",sum2)