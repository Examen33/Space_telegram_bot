import os
import requests
from dotenv import load_dotenv
from download_with_ext import download_image
from download_with_ext import define_ext




def get_nasa_days_pictures(nasa_token, number_of_photos):
    nasa_url = "https://api.nasa.gov/planetary/apod/"
    nasa_pic_dir = "directory/daily_nasa/"
    payload = {
        "api_key": nasa_token,
        "count" : number_of_photos,
    }
    response = requests.get(nasa_url, params = payload)
    response.raise_for_status()
    response_nasa_url = response.json()
    for index, day_image in enumerate(response_nasa_url):
        ext = define_ext(day_image["url"])
        filepath = f"{nasa_pic_dir}/nasa_apod_{index}{ext}"
        download_image(day_image["url"], filepath)


def main():
    load_dotenv()
    number_of_photos = 50
    nasa_token = os.environ["NASA_TOKEN"]

    get_nasa_days_pictures(nasa_token, number_of_photos)


if __name__ == "__main__":
    main()