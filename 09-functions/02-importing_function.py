# we can use a function written in a file in another file
# we have to import it from this file

from functions import sub
sub(100, 10)
print('.................................\n')

# we can import all function using *
from functions import *
add(100, 10)
print('.................................\n')

SI(10000, 3, 12.25)
print('.................................\n')
