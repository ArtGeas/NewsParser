import datetime
from datetime import timedelta

from django.db import models


class News(models.Model):
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    post_url = models.CharField(max_length=255, verbose_name='Ссылка на новость')
    post_title =  models.CharField(max_length=255, verbose_name='Заголовок новости')
    date_create  =  models.CharField(max_length=255, verbose_name='Дата публикации')  # Дата публикации новости в формате unix timestamp
    post_text = models.TextField(verbose_name='Текст новости')  # включая разметку и изображения
    post_image = models.CharField(max_length=255, verbose_name='Изображение к новости', blank=True, null=True)
    post_id = models.CharField(max_length=255, verbose_name='uid новости') # md5 hash от прямого ссылки на новость

    def save(self, *args, **kwargs):
        time_str = self.date_create
        time_str = time_str[:-1].split("T")
        time_str = " ".join(time_str)

        date_time_obj = datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S.%f') + timedelta(hours=3)  # переводим с utc на мск 
        self.date_create = str(date_time_obj.timestamp())
        super(News, self).save(*args, **kwargs)
