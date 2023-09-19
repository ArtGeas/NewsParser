from bs4 import BeautifulSoup
import requests
import json
from datetime import datetime


from news_parser.celery import app
from .models import News 


url = 'https://78.ru/news'


@app.task #регистриуем таску
def repeat_order_make():

    # распарсиваем список новостей
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

    # распарисиваем каждую новость поотдельности
    parsed_needed_news = []

    for new in needed_news:

        personal_dict = {}   
        news_page = requests.get(f'{url}/{datetime.today().strftime("%Y-%m-%d")}/{new["slug"]}')
        news_soup = BeautifulSoup(news_page.text, 'html.parser')
        news_soup = news_soup.find('script', type="application/ld+json")
        news_soup = json.loads(news_soup.text)

        personal_dict['news_id'] = new['id']
        personal_dict['url'] = f'{url}/{datetime.today().strftime("%Y-%m-%d")}/{new["slug"]}'
        personal_dict['title'] = new['title']
        personal_dict['created'] = new['availableAt'] 

        if news_soup.get('image') is not None:
            personal_dict['image'] = news_soup['image']['url']
        personal_dict['text'] = news_soup['text']


        parsed_needed_news.append(personal_dict)

        

    for news_data in parsed_needed_news:
          News.objects.get_or_create(post_id=news_data.get('news_id'),
                                     post_title=news_data.get('title'),
                                     date_create=news_data.get('created'), # время в UTC
                                     post_url =news_data.get('url'),
                                     post_text=news_data.get('text'),
                                     post_image=news_data.get('image')
                                     )     

    return "необязательная заглушка"