import requests
import argparse
from download_with_ext import download_image




def fetch_spacex_last_launch():
    parser = argparse.ArgumentParser(description="Программа скачивает картинки запуска ракет SpaceX")
    parser.parse_args()
    parser.add_argument("-l", "--launch_id", help="Start ID", default="5eb87d42ffd86e000604b384")
    namespace = parser.parse_args()

    spacex_dir = "directory/spacex/"
    spacex_url = f"https://api.spacexdata.com/v5/launches/{namespace.launch_id}"
    response = requests.get(spacex_url)
    response.raise_for_status()
    images_links = response.json()["links"]["flickr"]["original"]
    for photo_number, url in enumerate(images_links):
        filepath = f"{spacex_dir}/spacex{photo_number}.jpg"
        download_image(url, filepath)


def main():
    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()