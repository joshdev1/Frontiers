from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time

#wait = WebDriverWait(driver, 10)
#search = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "o_searchview_input")))

action = ActionChains(driver)
#action.key_down(Keys.CONTROL).send_keys('END').perform()
# for i in range(10):
#     action.key_down(Keys.SPACE).perform()
#     action.key_down(Keys.SPACE).perform()
#     driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")