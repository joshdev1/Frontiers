from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re


driver = webdriver.Chrome("D:\Projetcs\Frontiers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.frontiersin.org/journals")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(5)

soup = BeautifulSoup(driver.page_source, 'html.parser')


def get_journals(soup):
    journal_info = soup.find_all('div', class_='JournalCard__info')
    journals = []
    for journal in journal_info:
        journals.append(journal)
    return journals


def split_metric(metric, keys, values):
    is_float = re.compile("^[0-9]*.[0-9]*$")
    if metric.text:
        for data in metric.text.split():
            item = data.replace(",", "")
            if item != "views":
                if item.isdigit() or is_float.match(item):
                    values.append(float(item))
                else:
                    keys.append("article views" if item == "article" else item)


def metric_to_dict(metrics):
    keys = []
    values = []
    for metric in metrics:
        split_metric(metric, keys, values)
    return dict(zip(keys, values))


def get_journal_data(journals):
    journal_data = {}
    for journal in journals:
        title = journal.find('h2', class_='JournalCard__title')
        metrics = journal.find_all('span', class_='JournalCard__data')
        journal_data[title.text] = metric_to_dict(metrics)
    return journal_data


x = get_journals(soup)
print(get_journal_data(x))












