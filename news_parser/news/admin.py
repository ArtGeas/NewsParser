from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ['post_url', 'post_title', 'date_create', 'post_text', 'post_image', 'post_id']


admin.site.register(News, NewsAdmin)
