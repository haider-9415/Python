""" 
    Syntex  -->  list_name[index]

    A list has indexing 0 to 'n-1' on going left to right and -1 to '-n' on going right to left
    where, 'n' is the length of the list 
    remember -->  x = length_of_list + (-y), where, 'x' is the index of element 'a' from left and '-y' is the index of element 'a' from right

"""

lt1 = [1,2,3,'haider',3+78j,83.09]

print("\nleft --> right")
print("    lt1[0] -->",lt1[0])
print("    lt1[1] -->",lt1[1])
print("    lt1[2] -->",lt1[2])
print("    lt1[3] -->",lt1[3])
print("    lt1[4] -->",lt1[4])
print("    lt1[5] -->",lt1[5])

print("\nright --> left")
print("    lt1[-1] -->",lt1[-1])
print("    lt1[-2] -->",lt1[-2])
print("    lt1[-3] -->",lt1[-3])
print("    lt1[-4] -->",lt1[-4])
print("    lt1[-5] -->",lt1[-5])
print("    lt1[-6] -->",lt1[-6])