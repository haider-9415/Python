""" If a string is 's' and we want from 'x' index to 'y' index
    in the string 's' then
    we use s[x:y+1] but (y+1) excludes"""
# it is called 'slicing' it give conteneous data from any string
s = "haider"
str = 'pwskills'
print("s -->",s)
print("s[0:7] -->",s[0:7]) # it gives 'haider
print("s[0:3] -->",s[0:3]) # it gives 'hai'
print("s[3:6] -->",s[3:6]) # it gives 'der'
print("s[2:4] -->",s[2:5]) # it gives 'ide'

# if we don't want conteneous data then we use this method
print("s[0:7:2]-->",s[0:7:2]) # it gives 'hie'
print("str[0:5:3]-->",str[0:5:3]) # it gives 'pk'
print("str[3:7:2]-->",str[3:7:2]) # it gives 'kl'

""" if x>y then we use -ve """
print("str[0:7:-4]-->",str[0:7:-4]) # it gives 'space' because x<y
print("str[6:0:-2]-->",str[6:0:-2]) # it gives 'lis'
print("str[5:2:-2]-->",str[5:2:-2]) # it gives 'lk'
print("s[7:0] -->",s[7:0:-1]) # it gives 'redia'
print("s[7:0] -->",s[7::-1])  # it gives 'rediah'
print("s[7:0] -->",s[::-1])   # it gives 'rediah'

