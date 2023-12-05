import moviepy .editor
from tkinter.filedialog import *

# to open a folder
video = askopenfilename()
file1 = moviepy.editor.VideoFileClip(video)

# to convert into audio
file2 = file1.audio

# to save the file
name = input('Enter file name:')
path = input("Enter path to save file:")
file2.write_audiofile(f'{path}\{name}.mp3')

print("\nConverted :)\n")

