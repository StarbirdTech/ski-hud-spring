import os
from pytube import YouTube

cache_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")


def getId(link: str):
    return YouTube(link).video_id


def getLink(id: str):
    return f"https://youtu.be/watch?v={id}"


def download(link: str, path: str):
    video = YouTube(link)
    video.streams.filter(
        progressive=True, file_extension="mp4"
    ).get_highest_resolution().download(
        output_path=path,
        filename=video.video_id + ".mp4",
    )


def getFile(file_name: str, file_extension: str):
    if not os.path.exists(os.path.join(cache_path, f"{file_name}.{file_extension}")):
        download(getLink(file_name), cache_path)
        print(f"✅  Cached {file_name}.{file_extension}")
    return os.path.join(cache_path, f"{file_name}.{file_extension}")


if __name__ == "__main__":
    download(input("YouTube Video Link: "), cache_path)
