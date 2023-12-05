from string import *
from itertools import product

# to get all small & capital letters
alphabets = ascii_letters
print('alphabets:\n',alphabets, '\n')

# to get special characters
characters = punctuation
print('characters:\n',characters, '\n')

# to get digits
numbers = digits
print('numbers:\n',numbers, '\n')


value = ascii_letters + digits + punctuation
print('value:\n',value, '\n')


for i in range(1,3):
    # product() will make combinations from 1 to 3
    for j in product(value, repeat= i):
        # it returns a tuple that contains values of 'j' so we use join()
        password = "".join(j)

        # to save in a file
        file = open("wordlist.txt", 'a')
        file.write(password)
        file.write('\n')