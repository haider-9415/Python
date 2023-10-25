""" Escape sequence is a combination of characters having a meaning
    other than the literals """
""" backslash(\) is used as an escape sequence initiator """

# \n,\v or \f --> for new line
print("magnet\nbrains")
print('name\n    haider')
a = input("enter your\nname: ")
print(a)
print('magnet\vbarins')
print('magnet\fbarins')

# \r --> it removes a word before itself by a word after itself
print('haider\rhanzala')
print('lucknow\rdelhi')
print('abcdefg\rhij')

# \b --> it erases a letter before itself
print('magnets\b brains')
print('magnets br\bains')

# \t --> it gives a space
print('hanzalanaeem')
print('hanzala\tnaeem')
print('apple\torange\tmango\tbanana')

# \" --> to place in between " " 
# print(" ; --> it is "semi-colon" ") # it will give error
print("; --> it is \"semi-colon\"")

# \' --> to place in between ' ' 
# print('this is haider's book') # it will give error
print('this is haider\'s book')

""" to eleminate functionality of escape sequence ,there are two methods """
# method-1 --> doubling of backslash
# print('C:\U\vardan\new\videos') # it will give error,because, \U is unicode escape
# print('C:\\U\vardan\new\videos') # there is a problem, because, \v and \n ars escape sequence
print('using method-1')
print('C:\\U\\vardan\\new\\videos')


# method-2 --> create a raw string using 'r' before the string
print('using method-2')
print(r'C:\U\vardan\new\videos')
