# empty, zero and None are False in boolean 
print("bool(0) --> ",bool(0));print("bool(None) --> ",bool(None))
print("bool() --> ",bool());print("bool(0.0) --> ",bool(0.0))


# any no. except 0 is True in boolean
print("bool(100) --> ",bool(100));print("bool(267) --> ",bool(267));print("bool(9283) --> ",bool(9283))
print("bool(-5) --> ",bool(-5));print("bool(-2537) --> ",bool(-2537));print("bool(-1) --> ",bool(-1))
print("bool(1+23j) --> ",bool(1+23j));print("bool(27-32j) --> ",bool(27-32j))
print("bool(34.54) --> ",bool(34.54));print("bool(0.92830) --> ",bool(0.92830))
print("bool(-23.372)) --> ",bool(-23.372))
print("bool(0x1243a) --> ",bool(0x1243a)) # hexa decimal
print("bool(0o2237) --> ",bool(0o2237)) # octal
print("bool(0b1100010101) --> ",bool(0b1100010101)) # binary


# empty string is False
s1 = "";print("bool(s1) --> ",bool(s1))


# any other string is True in boolean
s2 = '0';print("bool(s2) --> ",bool(s2))
s3 = "haider";print("bool(s3) --> ",bool(s3))
s4 = '[1,2,3,4,4]';print("bool(s4) --> ",bool(s4))
s5 = " ";print("bool(s5) --> ",bool(s5))
s6 = 'False';print("bool(s6) --> ",bool(s6))