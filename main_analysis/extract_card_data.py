import re
import pandas as pd
from bs4 import BeautifulSoup

with open('synaptic_neuroscience.html') as f:
    content = f.read()
    soup = BeautifulSoup(content, 'html.parser')


def get_article_cards(soup):
    scraped_article_cards = soup.find_all('article', class_='CardArticle')
    article_cards = []
    for article_card in scraped_article_cards:
        article_cards.append(article_card)
    return article_cards


def get_article_metrics(article):
    article_metrics = article.find('ul', class_='CardArticle__metrics')
    split_metrics = article_metrics.text.split()
    is_float = re.compile("^[0-9]*.[0-9]*$")
    keys = []
    values = []
    for metric in split_metrics:
        metric = metric.replace(",", "")
        if metric.isdigit() or is_float.match(metric):
            values.append(float(metric))
        else:
            keys.append(metric)
    return dict(zip(keys, values))


def get_article_authors(article):
    article_authors = article.find('ul', class_='CardArticle__authors')
    authors = []
    for author in article_authors:
        if author != "\n":
            authors.append(author.text.strip())
    return authors


def get_title(article_title):
    title = article_title.text.replace("\n", "")
    title = re.sub(' +', ' ', title)
    return title.strip()


def get_article_data(article_cards):
    article_data = {}
    for article in article_cards:
        article_title = article.find('h1', class_='CardArticle__title')
        article_type = article.find('p', class_='CardArticle__type')
        article_date = article.find('p', class_='CardArticle__date')
        article_journal = article.find('div', class_='CardArticle__journal__name')

        article_data[get_title(article_title)] = {"article type": article_type.text,
                                                  "article date": article_date.text.strip(),
                                                  "article journal": article_journal.text,
                                                  "article authors": get_article_authors(article),
                                                  "article metrics": get_article_metrics(article)}
    return article_data


data = get_article_data(get_article_cards(soup))

print(data)



















