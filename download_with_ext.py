import os
import requests
from urllib.parse import urlparse




def create_dirs(*args):
    for directory in args:
        os.makedirs(directory, exist_ok=True)


def download_image(url, filepath):
    response = requests.get(url)
    response.raise_for_status()
    with open(filepath, 'wb') as file:
        file.write(response.content)


def define_ext(url):
    url_parsed = urlparse(url)
    file_ext = os.path.splitext(url_parsed.path)[1]
    return file_ext


def main():
    spacex_dir = "directory/spacex/"
    nasa_pic_dir = "directory/daily_nasa/"
    epic_dir = "directory/epics_nasa/"
    create_dirs(spacex_dir, nasa_pic_dir, epic_dir)


if __name__ == "__main__":
    main()