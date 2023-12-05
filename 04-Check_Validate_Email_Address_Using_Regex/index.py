# to import regex
import re

"""
    conditions:
        1st --> first character should be an alphabet
        2nd --> "." or "_" should be once before @
        3rd --> characters should be alphanumeric
        4th --> '@' should be once
        5th --> '.' should be at last 3rd or last 4th place
"""

conditions = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
"""
    '^[a-z]' tells that first character should be from 'a' to 'z'
    '?' tells '.' and '_' should be once
    '[@]\w' searches '@' should be in the given email and only once
    '[.]\w{2,3}$' tells that the '.' should be at last 3rd or last 4th place

"""
Email = input("Enter your email:")

if re.search(conditions, Email):
    print('\nValid Email\n')
else:
    print('\nWrong Email\n')
