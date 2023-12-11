# install ascii-magic-1.6
import ascii_magic as am
# using this, we can specify no. of columns and a character

imagePath = input('Enter path of the image(with name):')
col = int(input('Enter no. of columns:'))
ch = input('Enter the character:')

# to convert 
output = am.from_image_file(imagePath, columns=col, char=ch)

# to print on terminal
am.to_terminal(output)

# to save in a file
# am.to_file('demo4.txt', output)


