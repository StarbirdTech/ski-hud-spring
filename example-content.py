import os
import json
from pytube import YouTube
import numpy as np
import re

cache_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")


def getId(link: str):
    return YouTube(link).video_id


def getLink(id: str):
    return f"https://youtu.be/watch?v={id}"


def download(video_link: str, path: str):
    yt = YouTube(video_link)
    yt.streams.filter(
        progressive=True, file_extension="mp4"
    ).get_highest_resolution().download(
        output_path=path,
        filename=yt.video_id + ".mp4",
    )


def cache(file_name: str, file_extension: str):
    if not os.path.exists(os.path.join(cache_path, file_name, file_extension)):
        download(file_name, cache_path)
        print(f"✅  Cached {file_name}.{file_extension}")


def search(regex: str):
    with open(f"{cache_path}/files.json") as f:
        files = np.array(json.load(f))
    return files[
        np.vectorize(lambda file_name: bool(re.match(regex, file_name)))(files)
    ]


if __name__ == "__main__":
    print(download("https://www.youtube.com/watch?v=uZsp5JxrpPg", cache_path))
