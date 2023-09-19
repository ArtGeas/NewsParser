import os
from celery import Celery
from celery.schedules import crontab



os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'news_parser.settings')

app = Celery('news_parser')
app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()



# заносим таски в очередь
app.conf.beat_schedule = {
    'every': { 
        'task': 'news.tasks.repeat_order_make',
        'schedule': 900.0,  # 15 мин 
    },                                                              

}