from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ['post_id', 'post_url', 'post_title', 'date_create', 'post_text', 'post_image']
    actions = ['convert_to_JSON']

    @admin.action(description='Выгрузить в JSON')
    def convert_to_JSON(self, request, query):
        pass

admin.site.register(News, NewsAdmin)
