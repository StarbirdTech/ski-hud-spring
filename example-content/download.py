import os
from pytube import YouTube

sourcePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src")
video = YouTube(input("Enter the video URL: "))

dlVid = video.streams.filter(
    progressive=True, file_extension="mp4"
).get_highest_resolution()
dlVid.download(output_path=sourcePath, filename=video.video_id + ".mp4")
