from moviepy.editor import *

video = input("Enter video path:")
file_name = input('Enter name to save screenshot:')
time = int(input('Enter time at which screenshot is taken:'))

output = VideoFileClip(f'{video}.mp4')

output.save_frame(f'{file_name}.jpg', t=time)


