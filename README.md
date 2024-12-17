# Telegram_Space_Photos

Sends photos of space to the channel telegram from 3 sources. 

### Как установить

1. Скачайте репозиторий с проектом:
    ```sh
    git clone https://github.com/Examen33/Space_telegram_bot.git
    ```

2. Создайте файл `.env` в корневой директории проекта и добавьте следующие строки:
    ```env
    TELEGRAM_BOT_TOKEN=ваш_токен_бота_от_Telegram
    TELEGRAM_CHANNEL_ID=ваш_идентификатор_канала_Telegram
    NASA_TOKEN=ваш_токен_от_NASA_API
    ```

3. Установите зависимости:
    ```sh
    pip install -r requirements.txt
    ```

### Как использовать

1. Загрузите изображения с NASA APOD:
    ```sh
    python fetch_nasa_apod_images.py
    ```
    
2. Загрузите изображения с SpaceX:
    ```sh
    python fetch_spacex_images.py 
    ```

3. Загрузите изображения с NASA EPIC:
    ```sh
    python fetch_epic_images.py
    ```
    
2. Запустите скрипт для публикации изображений в Telegram-канал:
    ```sh
    python image_for_telegram.py images --delay 14400
    ```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
