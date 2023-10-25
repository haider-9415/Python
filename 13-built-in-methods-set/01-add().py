""" to add an element --> .add() """

s1 = {1,3,2,566,"haider",90+97j,3.655,'naeem'}

s1.add('hanzala')
print("s1 -->",s1,'\n') # now,'hanzala' is in s1

s2 = s1.add('naeem')
print("s2 -->",s2,'\n')

# s4.add('haider')
# print(s4) # it gives run time error ,because, s4 is a dictionary not an empty set

""" we can add immutable entyties in a set ,so list & set can not place in a set but tuple & string can place """
s1.add((98,90,23.433,'hudbdj',9+0j))
print("s1 -->",s1,'\n') # now,'(98,90,23.433,'hudbdj',9+0j)' is in s1