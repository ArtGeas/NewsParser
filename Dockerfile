FROM python:3.11.4-slim
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.txt .
COPY ./news_parser/ .
RUN pip install -r requirements.txt && \ 
                    cd news_parser && \
                    python manage.py runserver 0.0.0.0:8000 && \
                    celery -A news_parser worker -l info && \
                    celery -A news_parser beat -l info