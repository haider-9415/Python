""" to remove an element from a set --> .remove() or .discard()
    if an element 'x' is not in a set then remove function will give error but discard functon will not give error
"""



s1 = {1,3,2,566,"haider",90+97j,3.655,'naeem'}

s1.remove(3.655)
print("s1 -->",s1,'\n') # now,3.655 is not in s1

s1.discard("naeem")
print("s1 -->",s1,'\n') # now,'naeem' is not in s1