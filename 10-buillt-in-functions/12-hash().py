"""
  hash(immutable object) --> it provides the object a unique value
  it returns hash value that is nothing but integer and its class is 'int'
"""
  


""" hash value of an integer is the integer itself """
print("hash(14273) --> ",hash(14273),)
print("type(hash(14273)) --> ",type(hash(14273)),'\n')
print("hash(293028273) --> ",hash(293028273),)
print("type(hash(293028273)) --> ",type(hash(293028273)),'\n')
print("hash(0) --> ",hash(0),)
print("type(hash(0)) --> ",type(hash(0)),'\n')
print("hash(-2736) --> ",hash(-2736),)
print("type(hash(-2736)) --> ",type(hash(-2736)),'\n')
print("hash(-92736219) --> ",hash(-92736219),)
print("type(hash(-92736219)) --> ",type(hash(-92736219)),'\n')

""" hash values for decimals, complex """
print("hash(142.0) --> ",hash(142.0),)
print("type(hash(142.0)) --> ",type(hash(142.0)),'\n')
print("hash(142.73) --> ",hash(142.73),)
print("type(hash(142.73)) --> ",type(hash(142.73)),'\n')
print("hash(2930.28273) --> ",hash(2930.28273),)
print("type(hash(2930.28273)) --> ",type(hash(2930.28273)),'\n')
print("hash(0.0) --> ",hash(0.0),)
print("type(hash(0.0)) --> ",type(hash(0.0)),'\n')
print("hash(-2.736) --> ",hash(-2.736),)
print("type(hash(-2.736)) --> ",type(hash(-2.736)),'\n')
print("hash(-9273621.9) --> ",hash(-9273621.9),)
print("type(hash(-9273621.9)) --> ",type(hash(-9273621.9)),'\n')
# if complex part is +ve then the hash value is also +ve
# if complex part is -ve then the hash value is also -ve
# hash value of 'a+b' & 'a-b' will be 'x' & '-x' respectively whether 'a' is +ve or -ve
print("hash(-14+73j) --> ",hash(-14+73j),)
print("type(hash(-14+73j)) --> ",type(hash(-14+73j)),'\n')
print("hash(14-73j) --> ",hash(14-73j),)
print("type(hash(14-73j)) --> ",type(hash(14-73j)),'\n')
print("hash(14+73j) --> ",hash(14+73j),)
print("type(hash(14+73j)) --> ",type(hash(14+73j)),'\n')
print("hash(-14-73j) --> ",hash(-14-73j),)
print("type(hash(-14-73j)) --> ",type(hash(-14-73j)),'\n')

""" hash values for string """
# hash value of empty string is 0
print("hash("") --> ",hash(""))
print("type(hash("")) --> ",type(hash("")),'\n')
print("hash('0') --> ",hash("0"))
print("type(hash('0')) --> ",type(hash("0")),'\n')
print("hash('a') --> ",hash('a'))
print("type(hash('a')) --> ",type(hash('a')),'\n')
print("hash('haider') --> ",hash('haider'),)
print("type(hash('haider')) --> ",type(hash('haider')),'\n')
print("hash('abc') --> ",hash('abc'))
print("type(hash('abc')) --> ",type(hash('abc')),'\n')
print("hash('@$$^&&&^') --> ",hash('@$$^&&&^'))
print("type(hash('@$$^&&&^')) --> ",type(hash('@$$^&&&^')),'\n')
print("hash('abcd3829$^%') --> ",hash('abcd3829$^%'))
print("type(hash('abcd3829$^%')) --> ",type(hash('abcd3829$^%')),'\n')
print("hash('\n') --> ",hash('\n'))
print("type(hash('\n')) --> ",type(hash('\n')),'\n')
print("hash(" ") --> ",hash(" "))
print("type(hash(" ")) --> ",type(hash(" ")),'\n')
print("hash('[1,2,3,4,5,6,7]') --> ",hash("[1,2,3,4,5,6,7]"))
print("type(hash('[1,2,3,4,5,6,7]')) --> ",type(hash("[1,2,3,4,5,6,7]")),'\n')
print("hash('(a,b,c,d,e,f,g)') --> ",hash("(a,b,c,d,e,f,g)"))
print("type(hash('(a,b,c,d,e,f,g)')) --> ",type(hash("(a,b,c,d,e,f,g)")),'\n')

""" hash value and address of a string remain change """
# if you run the following code n times then you will get n different hash vlaue and address
print("hash('haider') --> ",hash('haider'),)
print("type(hash('haider')) --> ",type(hash('haider')))
print("id(hash('haider')) --> ",id(hash('haider')),'\n')

""" hash value of an integer,decimal,complex,etc. remains same but their addresses change """
# if you run the following code n times then you will get n different address but same hash value
print("hash(162) --> ",hash(162),)
print("type(hash(162)) --> ",type(hash(162)))
print("id(hash(162)) --> ",id(hash(162)),'\n')
print("hash(162.273) --> ",hash(162.273),)
print("type(hash(162.273)) --> ",type(hash(162.273)))
print("id(hash(162.273)) --> ",id(hash(162.273)),'\n')
print("hash(636+98j) --> ",hash(636+98j),)
print("type(hash(636+98j)) --> ",type(hash(636+98j)))
print("id(hash(636+98j)) --> ",id(hash(636+98j)),'\n')



# for tuple
t1= (1,2,3,4,5,6); t2 = ('a','b','c','d','e'); t3 = (1,2,3,4,304.12,120.23,True,False,'hanzla',3+92j)
print("hash(t1) --> ",hash(t1))
print("type(hash(t1)) --> ",type(hash(t1)),'\n')

print("hash(t2) --> ",hash(t2))
print("type(hash(t2)) --> ",type(hash(t2)),'\n')

print("hash(t3) --> ",hash(t3))
print("type(hash(t3)) --> ",type(hash(t3)),'\n')