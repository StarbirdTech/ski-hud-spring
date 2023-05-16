import os


def search_files(search=None, extension=None):
    matching_files = []
    sourcePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src")
    for filename in os.listdir(sourcePath):
        if extension is not None and not filename.endswith(extension):
            continue
        if search is not None and search not in filename:
            continue
        matching_files.append(sourcePath, filename)
    return matching_files


if __name__ == "__main__":
    print(search_files(extension="txt"))

import os
from pytube import YouTube

sourcePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src")
video = YouTube(input("Enter the video URL: "))

dlVid = video.streams.filter(
    progressive=True, file_extension="mp4"
).get_highest_resolution()
dlVid.download(output_path=sourcePath, filename=video.video_id + ".mp4")
