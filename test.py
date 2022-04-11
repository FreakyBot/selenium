from telnetlib import EC

import null as null
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import *
from selenium.webdriver.common.by import By
import time

# driver = webdriver.Chrome('/usr/bin/google-chrome-stable')
# driver = webdriver.Chrome('/opt/google/chrome')
from selenium.webdriver.support.wait import WebDriverWait

s = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=s)

driver.get("https://www.salesmanago.com/info/knowledgecenter.htm")

#elems = driver.find_element(By.XPATH, "//div[@class='ebook__img--container']/a").get_attribute("href")
elems = driver.find_element(By.CSS_SELECTOR, "div.ebook__img--container a")
print(elems)
# elems = driver.find_element(By.XPATH, "//div[@class='ebook__img--container']/a")


# WebDriverWait(driver, 30).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,
# "//div[@class='ebook__img--container']/a"))) print([my_elem.get_attribute("href") for my_elem in WebDriverWait(
# driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='ebook__img--container']/a")))])
#


# temp = []
#
# for i in elems:
#     if i is not null:
#         temp += i
#         print(temp)
# for X in link:
#     print(X)


# elems = driver.find_elements(By.CSS_SELECTOR, ".ebook__img--container [href]")
# links = [elem.get_attribute('href') for elem in elems]


# login_form = driver.find_element_by_id('loginForm')

driver.close()
