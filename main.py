import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# ChromeDriver
s = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=s)

# Destinated site
driver.get("https://www.salesmanago.com/info/knowledgecenter.htm")

wait = WebDriverWait(driver, 20)

# Accepting cookies
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="close-cookies"]'))).click()

# Closing live chat
wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="hubspot-messages-iframe-container"]/iframe')))
try:
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@aria-label='Close live chat']"))).click()
except TimeoutException as to:
    print(to)

driver.switch_to.default_content()

elems = driver.find_elements(By.CSS_SELECTOR, "div.ebook__img--container a")

search = input("Wpisz porzadana fraze e-booka lub ALL dla wylistowania linkow do e-bookow: ")

if search.lower() == 'all':
    temp = 0
    for elem in elems:
        print(temp, elem.get_attribute('href'))
        temp += 1
    else:
        wybrany = int(input("Ktory index? : "))
        print("Wybrales link :", elems[wybrany].get_attribute('href'))
        driver.get(elems[wybrany].get_attribute('href'))
elif search.lower() != 'all':
    for a in driver.find_elements(By.CSS_SELECTOR, "div.ebook__img--container a"):
        if search in a.get_attribute('href'):
            print("Link : " + a.get_attribute('href'))
            driver.get(a.get_attribute("href"))
            break

# amazing_shopping_experience_new_knowledge.htm

name = driver.find_element(By.NAME, 'name')
name.send_keys('test')

email = driver.find_element(By.NAME, 'email')
email.send_keys('kamil.kaletka+testrekrutacja@salesmanago.com')

company = driver.find_element(By.NAME, 'company')
company.send_keys('test')

url = driver.find_element(By.NAME, 'url')
url.send_keys('https://test.pl')

phone = driver.find_element(By.NAME, 'phoneNumber')
phone.send_keys('732104858')

submit = driver.find_element(By.XPATH, '//*[@id="uspForm"]/div[2]/div/button')
submit.click()

driver.close()
