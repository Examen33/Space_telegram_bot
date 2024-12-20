import os
import requests
import argparse
from download_with_ext import download_image
from dotenv import load_dotenv




def get_epic_image_urls(api_key, count=10):
    base_url = "https://api.nasa.gov/EPIC/api/natural"
    params = {"api_key": api_key}
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    epic_images = response.json()

    image_urls = []
    for epic_item in epic_images[:count]:
        image_date = epic_item["date"].split()[0]
        image_name = epic_item["image"]
        image_url = f"https://epic.gsfc.nasa.gov/archive/natural/{image_date.replace('-', '/')}/png/{image_name}.png"
        image_urls.append(image_url)

    return image_urls


def download_epic_images(image_urls):
    epic_dir = "directory/epics_nasa/"
    for index, url in enumerate(image_urls):
        filepath = f"{epic_dir}/epic_earth_{index}.png"
        download_image(url, filepath)


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="Загрузить фотографии NASA EPIC")
    parser.add_argument(
        "--count", type=int, default=10, help="Количество изображений для загрузки"
    )
    args = parser.parse_args()

    api_key = os.getenv("NASA_TOKEN")

    image_urls = get_epic_image_urls(api_key, args.count)
    download_epic_images(image_urls)


if __name__ == "__main__":
    main()