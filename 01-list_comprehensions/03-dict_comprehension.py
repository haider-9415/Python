# without comprehension
print('without comprehension')
nums = [1,2,3,4,5,6,7,8,9]
my_dict1 = {}
for n in nums:
    my_dict1[n] = n**2
print('my_dict1 --> ',my_dict1)
print()

# with comprehension
print('with comprehension')
my_dict2 = {n:n**2 for n in nums}
print('my_dict2 --> ',my_dict2)
print("...........................................................\n")


# with if statement
print('without comprehension')
nums = [1,2,3,4,5,6,7,8,9]
my_dict3 = {}
for n in nums:
    if n%2 != 0:
        my_dict3[n] = n**2
print('my_dict3 --> ',my_dict3)
print()

print('with comprehension')
my_dict4 = {n:n**2 for n in nums if n%2!=0}
print('my_dict4 --> ',my_dict4)
print("...........................................................\n")



print('without comprehension')
str1 = 'haider'
my_dict5 = {}
for char in str1:
    my_dict5[char.upper()] = (ord(char), ord(char.upper()))
print('my_dict5 --> ',my_dict5)
print()

print('with comprehension')
my_dict6 = {char.upper():(ord(char), ord(char.upper())) for char in str1}
print('my_dict6 --> ',my_dict6)
print("...........................................................\n")
