#1. Expand metadata. For each entry in the list, try to get:
#  contact name and numbers, and address (road name, building name, area), some products they sell

import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = False


browser = webdriver.Firefox(options=options)

url = 'https://savanisbookshop.com/users/all-books'

browser.get(url)


time.sleep(10)
elems = browser.find_elements(By.CSS_SELECTOR, "div[id='book-name']")
for elem in elems:
    print(elem.text)
# next page
browser.get("https://savanisbookshop.com/users/all-books?&p=2")
time.sleep(10)
elems = browser.find_elements(By.CSS_SELECTOR, "div[id='book-name']")
for elem in elems:
    print(elem.text)
browser.quit()