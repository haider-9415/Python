# to make a constant, first install 'pconst' library and import 'const'
from pconst import const

# we have to used const. before a variable to make it constant
const.pi = 3.14

# it will not give run time error, because, const. has not been used with same variable
pi = 1000
print(pi)

const.pi = 123
# it will give run time error, because, const. has been used with same variable
print(const.pi)
