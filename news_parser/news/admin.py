import json

from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ['post_id', 'post_url', 'post_title', 'date_create', 'post_text', 'post_image']
    ordering = ['-date_create']
    actions = ['convert_to_JSON']

    @admin.action(description='Выгрузить в JSON')
    def convert_to_JSON(self, request, query):
        
        data_for_json = []
        for news_obj in query:
            news_data = {}
            news_data['post_id'] = news_obj.post_id
            news_data['post_url'] = news_obj.post_url
            news_data['post_title'] = news_obj.post_title
            news_data['date_create'] = news_obj.date_create
            news_data['post_text'] = news_obj.post_text
            news_data['post_image'] = news_obj.post_image
            data_for_json.append(news_data)


        with open('news_data.json', 'w') as file:
            for news in data_for_json:
                file.write(json.dumps(news, ensure_ascii=False))

admin.site.register(News, NewsAdmin)
