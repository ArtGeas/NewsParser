FROM python:3.11.4-slim
EXPOSE 8000
EXPOSE 6379
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt --no-cache-dir
RUN python3 news_parser/manage.py makemigrations && python3 news_parser/manage.py migrate 
CMD python3 news_parser/manage.py runserver 0.0.0.0:8000