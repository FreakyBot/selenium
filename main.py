import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = 'K://pythonProject/venv/chromedriver-Windows'
driver = webdriver.Chrome(s)

# path = 'K://pythonProject/venv/chromedriver-Windows'
# driver = webdriver.Chrome(path)

# navigating to
driver.get('https://www.salesmanago.pl/info/knowledgecenter.htm')

elems = driver.find_elements(By.XPATH, "//a[@href]")


for elem in elems:
    print(elem.get_attribute('href'))

# elems = driver.find_elements(By.CSS_SELECTOR, ".ebook__img--container [href]")
# links = {elem.get_attribute('href') for elem in elems}

# printing length of total i.e total number of links
# print(len(total))
# print("Following are the link present in the webpage")
# for totals in total:
#     total.get_attribute("href")
#     print(totals.text)

driver.close()
