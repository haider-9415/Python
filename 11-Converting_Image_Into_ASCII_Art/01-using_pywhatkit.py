import pywhatkit as pwk

# the following function acceepts two parameters
# 1st is path of that image and 2nd is the path of the file to save it
imagePath = input('Enter path of the image(with name):')
filePath = input('Enter path of the file(with name):')
pwk.image_to_ascii_art(imagePath, filePath)