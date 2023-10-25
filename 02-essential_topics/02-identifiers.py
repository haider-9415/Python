""" An identifier is a name used to identify a variable, function
    class, module, etc. It helps to differentiate one entity from another"""

# Rules for an identifier

# rule-1
""" an identifier can be the combination of letters (a-z) or (A-Z)
    or underscore(_) and digits(0-9)"""
#E.g.
h12_ = 12
_ = 2
_21 = 3
name = "hanzala"
print(h12_);print(_);print(_21);print(name)

# rule-2
""" an identifier can not be started with a digit """
#E.g.
23_ = 32
2name = "hanzala"
# both are incorrect

# rule-3
""" an identifier can not be a keyword """
#E.g.
True = 1
False = "haider"
# both are incorrect, because, both are keywords

# rule-4
""" an identifier can not have any special symbol """
#E.g.
name$ = "hanzala"
_@23 = 1234
&name = "haider"
# these are incorrect
