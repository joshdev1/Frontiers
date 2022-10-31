from bs4 import BeautifulSoup
import pandas as pd
from matplotlib.pyplot import matplotlib
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import re

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
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
        journal_data[title.text.strip()] = metric_to_dict(metrics)
    print(journal_data)
    return journal_data


df = pd.DataFrame.from_dict(get_journal_data(get_journals(soup)), orient="index")
df2 = pd.DataFrame.from_dict(get_journal_data(get_journals(soup)))

df.to_excel("journal_data.xlsx")

print(df.tail())
print(df2.tail())





