from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
aging_neuroscience = "https://www.frontiersin.org/journals/aging-neuroscience/articles"
synaptic_neuroscience = "https://www.frontiersin.org/journals/synaptic-neuroscience/articles"
driver.get(synaptic_neuroscience)
driver.maximize_window()  # make window bigger so more content can be loaded at once for faster scraping.

wait = WebDriverWait(driver, 10)
cookies = wait.until(expected_conditions.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
cookies.click()

while True:
    previous_height = driver.execute_script("return document.documentElement.scrollHeight")
    driver.execute_script("window.scrollTo(0, " + str(previous_height) + ");")
    time.sleep(1)
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if previous_height == new_height:
        break

soup = BeautifulSoup(driver.page_source, 'html.parser')

print(soup)


# def get_article_cards(soup):
#     scraped_article_cards = soup.find_all('article', class_='CardArticle')
#     article_cards = []
#     for article_card in scraped_article_cards:
#         article_cards.append(article_card)
#     return article_cards
#
#
# x = get_article_cards(soup)
# print(x.text)




