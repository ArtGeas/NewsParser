# NewsParser

Приложение парсит новостной сайт в БД каждые 15 мин.

Все настройки бот берет из переменных окружения. В корне проекта(NewsParser/news_parser/news_parser) рядом с файлом settings.py есть файл .env.template, туда же закинуть приложенный файл .env

После запуска проекта, чтобы получить доступ в админку переходим по http://127.0.0.1:8000/admin/

В админке есть возможность выгружать выбранные новости в json-файл в корень django-проекта.
![image](https://github.com/ArtGeas/NewsParser/assets/116754574/1f2d8885-d893-440a-b179-e5ad081a28cc)

# Шаги запуска проекта 

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
