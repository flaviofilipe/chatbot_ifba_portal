import requests
from bs4 import BeautifulSoup

host = 'https://portal.ifba.edu.br'
url_news = '/conquista/noticias-2/noticias-campus-vitoria-da-conquista'
search_url = '/@@busca?SearchableText='


def get_last_posts() -> list:
    page_url = f'{host}{url_news}?b_start:int=0'
    page = requests.get(page_url, verify=False)
    soup = BeautifulSoup(page.text, 'html.parser').find_all(
        'article', class_='entry')
    return format_posts(soup)


def format_posts(soup) -> list:
    articles = []
    for article in soup:
        summary = article.header.find(class_='summary')
        article = {
            'title': summary.a.getText(),
            'link': summary.a['href'],
            'date': __get_dat_publish(article)
        }
        articles.append(article)
    return articles


def __get_dat_publish(articles):
    data_modification = articles.header.find(
        class_='documentByLine').getText().replace("  ", "").replace('\n', "")
    date = data_modification[data_modification.find('modificação') + 11:]
    return date


def search(text):
    page_url = f'{host}{search_url}{text}'
    page = requests.get(page_url, verify=False)
    soup = BeautifulSoup(page.text, 'html.parser').find(class_='searchResults').find_all(
        'dt')
    return format_results(soup)


def format_results(soup):
    articles = []
    for article in soup:
        article = {
            'tile': article.a.getText(),
            'link': article.a['href'],
        }
        articles.append(article)
    return articles
