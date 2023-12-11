from moviepy.editor import *

videoPath = input('Enter path of the video(with name):')
gifPath = input('Enter path of the gif(with name):') # to save the gif

# VideoFileClip() --> to obtain the video
# subclip(min, sec) --> to split the video
# rotate(x) --> to rotate the gif at degree of 'x'
video = VideoFileClip(f'{videoPath}.mp4').subclip(00, 20).rotate(90)

video.write_gif(f'{gifPath}.gif')

print('Converted :)')

