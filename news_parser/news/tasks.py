from bs4 import BeautifulSoup
import requests
import json


from news_parser.celery import app
from .models import News 


url = 'https://78.ru/news'


@app.task #регистриуем таску
def repeat_order_make():

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    needed_news = []

    all_news = soup.findAll('script', type="application/json")
    dict_news = json.loads(all_news[0].text)
    dict_news = dict_news['props']['pageProps']['__nextRelayBridgeProps__']['initialStore']

    for key, val in dict_news.items():
            if dict_news[key]['__typename']:
                if dict_news[key]['__typename'] == 'Article':
                        needed_news.append(val)
    
    for news_data in needed_news:
          News.objects.get_or_create(post_id=news_data.get('id'),
                                     post_title=news_data.get('title'),
                                     date_create=news_data.get('availableAt'), # время в UTC
                                     )     



    """
    post_url = models.CharField(max_length=255, verbose_name='Ссылка на новость')
    post_text = models.TextField(max_length=255, verbose_name='Текст новости')  # включая разметку и изображения
    post_image = models.ImageField(upload_to='images', verbose_name='Изображение к новости', blank=True, null=True)
    """   

    return "необязательная заглушка"