FROM python:3.11.4-slim
EXPOSE 8000

WORKDIR /app
COPY . ./
RUN python -m pip install --no-cache-dir -r requirements.txt
CMD python news_parser/manage.py runserver 0.0.0.0:8000