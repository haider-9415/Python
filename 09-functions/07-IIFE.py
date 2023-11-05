# we don't need to call such functions

result1 = (lambda x: x+10)(50)
print('result1 --> ',result1)
print('......................................................................\n')


result2 = (lambda x, y: x+y)(50, 100)
print('result2 --> ',result2)
print('......................................................................\n')


square = lambda n: n**2
modify = lambda func: lambda num: func(num)+num
result3 = modify(square) (int(input('Enter a number: ')))
print('result3: ',result3)
print('......................................................................\n')

