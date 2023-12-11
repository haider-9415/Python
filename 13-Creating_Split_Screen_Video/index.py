from moviepy.editor import *

path1 = input('Enter path of video-1:')
path2 = input('Enter path of video-2:')
path3 = input('Enter path of video-3:')
path4 = input('Enter path of video-4:')

clip_1 = VideoFileClip(f'{path1}.mp4').subclip(00, 10)
clip_2 = VideoFileClip(f'{path2}.mp4').subclip(10, 20)
clip_3 = VideoFileClip(f'{path3}.mp4').subclip(00, 10)
clip_4 = VideoFileClip(f'{path4}.mp4').subclip(00, 10)

# to merge them
clips = clips_array([[clip_1, clip_2],
                     [clip_3, clip_4]])

# to create them as a single file
file_name = input('Enter file name to save:')
clips.write_videofile(f'{file_name}.mp4')

