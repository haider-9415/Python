from moviepy.editor import *

path = input("Enter video path:")
text = input("Enter text to add:")
file_name = input('Enter file name to save:')

video = VideoFileClip(f'{path}.mp4')
txt = TextClip(text, fontsize=60, color='red')

# to set position and duration of text
txt = txt.set_position("center").set_duration(30)

# to set the text on the video
output = CompositeVideoClip([video, txt])

output.write_videofile(f'{file_name}.mp4')

