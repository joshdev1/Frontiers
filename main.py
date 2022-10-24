from bs4 import BeautifulSoup
from selenium import webdriver
import time


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


def get_journal_data(journals):
    for journal in journals:
        title = journal.find('h2', class_='JournalCard__title')
        data = journal.find_all('span', class_='JournalCard__data')
        print("Title =", title.text)
        for item in data:
            print("data =", item.text)
        print("---------------------------------")


x = get_journals(soup)
get_journal_data(x)












