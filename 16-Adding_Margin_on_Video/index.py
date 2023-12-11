from moviepy.editor import *

video = input("Enter video path:")
file_name = input('Enter name to save new video:')
margin = int(input("Enter margin:"))

# to get a clip of the file, you can set the margin on whole video
output = VideoFileClip(f'{video}.mp4').subclip(00, 10)

# to give margin
output = output.margin(margin)

output.write_videofile(f'{file_name}.mp4')

