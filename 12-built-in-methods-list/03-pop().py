""" to remove & show an element --> .pop() """

l = [1,2,53.665,'haider',34-42j,True]
l1 = [43,5,4,6.5,6,5.6,433.67,0,-445,-344,1,-1]
l2 = ['abc','wed','aaf','fd']

print(l2.pop()) # by default it will remove last element
print('l2 -->',l2,'\n') # now 'fd' is not in 'l2'
print(l.pop(3)) # it will remove 'haider'
print('l -->',l,'\n') # now 'haider' is not in 'l'

# to remove a specific element, we have to pass its index
print(l1.pop(6)) # it will remove 433.67
print('l1 -->',l1,'\n') # now 433.67 is not in 'l1' 

print(l2.pop(0)) # it will remove 'abc'
print('l2 -->',l2,'\n') # now 'abc' is not in 'l2' 