import os
import json
from pytube import YouTube


def getId(link: str):
    return YouTube(link).video_id


def getLink(id: str):
    return f"https://youtu.be/watch?v={id}"


def download(video: str):
    YouTube(video).streams.filter(
        progressive=True, file_extension="mp4", use_oauth=True, allow_oauth_cache=True
    ).get_highest_resolution().download(
        output_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"),
        filename=getId(video) + ".mp4",
    )


def search(search=None, extension=None):
    matching_files = []
    sourcePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src")
    for filename in os.listdir(sourcePath):
        if extension is not None and not filename.endswith(extension):
            continue
        if search is not None and search not in filename:
            continue
        matching_files.append(sourcePath, filename)
    return matching_files


def get(id: str):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "src", id)


if __name__ == "__main__":
    download(input("Enter the video URL: "))
