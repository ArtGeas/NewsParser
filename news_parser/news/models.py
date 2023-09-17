from django.db import models
from unixtimestampfield.fields import UnixTimeStampField

class News(models.Model):
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    post_url = models.CharField(max_length=255, verbose_name='Ссылка на новость')
    post_title =  models.CharField(max_length=255, verbose_name='Заголовок новости')
    date_create  =  UnixTimeStampField(verbose_name='Дата публикации')  # Дата публикации новости в формате unix timestamp
    post_text = models.TextField(max_length=255, verbose_name='Текст новости')  # включая разметку и изображения
    post_image = models.ImageField(upload_to='images', verbose_name='Изображение к новости')
    post_id = models.PositiveSmallIntegerField(verbose_name='uid новости') # md5 hash от прямого ссылки на новость
