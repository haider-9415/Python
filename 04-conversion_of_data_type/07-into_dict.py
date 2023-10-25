# to convert a data type into dictonary,there are some forms

# form-1 --> list of lists --> [[],[]]
dict1 = [[1,'a'],[2,'b'],[3,'c'],[4,'d']]
print("form-1")
print("    ",dict1," --> ",dict(dict1))

# form-2 --> list of sets --> [{},{}]
dict2 = [{'H','h'},{'I','i'},{'J','j'},{'K','k'}]
print("form-2")
print("    ",dict2," --> ",dict(dict2))

# form-3 --> list of tuples --> [(),()]
dict3 = [('name','hanzala'),('class','12th')]
print("form-3")
print("    ",dict3," --> ",dict(dict3))

# form-4 --> set of tuples --> {(),()}
dict4 = {('one',1),('two',2),('three',3)}
print("form-4")
print("    ",dict4," --> ",dict(dict4))

# form-5 --> tuple of lists --> ([],[])
dict5 = (['forward','w'],['down','s'],['right','d'],['left','c'])
print("form-5")
print("    ",dict5," --> ",dict(dict5))

# form-6 --> tuple of tuples --> ((),())
dict6 = (('ten',10),('hundred',100))
print("form-6")
print("    ",dict6," --> ",dict(dict6))

# form-7 --> tuple of sets --> ({},{})
dict7 = ({'a',43},{'b',98},{'c',87})
print("form-7")
print("    ",dict7," --> ",dict(dict7))

# form-8 --> mix --> [(),{},[]], ({},(),[]), etc.
dict8 = ({'a',43},('ten',10),['left','c'])
print("form-8")
print("    ",dict8," --> ",dict(dict8))
