# NewsParser

Приложение парсит новостной сайт в БД каждые 15 мин.

!!! Все настройки бот берет из переменных окружения. В корне проекта(NewsParser/news_parser/news_parser) рядом с файлом settings.py есть файл .env.template, туда же закинуть приложенный файл .env

После запуска проекта, чтобы получить доступ в админку переходим по http://127.0.0.1:8000/admin/

В админке есть возможность выгружать выбранные новости в json-файл в корень django-проекта.
![image](https://github.com/ArtGeas/NewsParser/assets/116754574/1f2d8885-d893-440a-b179-e5ad081a28cc)

Далее следуют инструкция по обычному запуску и инструкция по запуску через docker

# Шаги обычного запуска проекта 

1. Устанавливаем зависимости 
```bash
pip install -r requirements.txt
```

2. Запускаем Redis
```bash
docker run -d -p 6379:6379 redis 
```

3. Переходим в корень django-проекта(cd news_parser). Применяем миграции и заводим суперюзера (для доступа в админку django)
```bash
python manage.py makemigrations && python manage.py migrate --run-syncdb && python manage.py createsuperuser 
```

4. Запускаем Django-сервер
```bash
python manage.py runserver
```

5. Открываем второе окно терминала и запускаем Celery worker
```bash
celery -A news_parser worker -l info
```

6. Открываем еще одно окно терминала и запускаем Celery beat
```bash
celery -A news_parser beat -l info
```

# Шаги запуска проекта через docker

1. Запускаем Redis
```bash
docker run -d -p 6379:6379 redis 
```

2. Собираем образ docker с проектом
```bash
docker build .
```

3. Запускаем docker-контейнер с проектом
```bash
docker run -d -p 8000:8000 -p 6379:6379 <id образа>
```

4. Заходим внутрь контейнера, преходим в директорию проекта и запускаем Celery worker в папке django-проекта
```bash
docker exec -it <id контейнера> bash
```
```bash
cd app/news_parser/
```
```bash
celery -A news_parser worker -l info
```

5. Открываем еще одно окно терминала, заходим внутрь контейнера, преходим в директорию проекта и запускаем Celery beat в папке django-проекта
```bash
docker exec -it <id контейнера> bash
```
```bash
cd app/news_parser/
```
```bash
celery -A news_parser beat -l info
```
(опционально для доступа в админку)6. Открываем еще одно окно терминала, заходим внутрь контейнера, преходим в директорию проекта и заводим суперюзера в папке django-проекта
```bash
docker exec -it <id контейнера> bash
```
```bash
cd app/news_parser/
```
```bash
python3 manage.py createsuperuser
```
