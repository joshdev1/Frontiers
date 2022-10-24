from selenium import webdriver
import time

driver = webdriver.Chrome("D:\Projetcs\Frontiers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.frontiersin.org/journals")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

time.sleep(5)
