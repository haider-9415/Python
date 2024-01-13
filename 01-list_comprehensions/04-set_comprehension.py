# it is like list comprehension the difference is we use {} in this

num1 = [1,2,3,4,5,6,7,4,5,8,9,10]
print('num1 --> ',num1,'\n')


sqr = {n*n for n in num1}
print('sqr --> ',sqr,'\n')

even = {n for n in num1 if n%2 == 0}
print('even --> ',even,'\n')

mult =  {n*2 if n%2==0 else n*3 for n in num1}
print('mult --> ',mult,'\n')
