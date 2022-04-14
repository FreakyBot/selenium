from selenium import webdriver
from selenium.webdriver.chrome.service import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

s = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=s)

driver.get("https://www.salesmanago.com/info/knowledgecenter.htm")

wait = WebDriverWait(driver, 10)

element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="close-cookies"]'))).click()
# element1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'VizExNotificationBadge__Wrapper-b3snvh-0 kanpaf'))).click()
driver.switchTo().frame(driver.find_element(By.XPATH, '//*[@id="hubspot-messages-iframe-container'))
driver.find_element(By.CLASS_NAME("VizExNotificationBadge__Wrapper-b3snvh-0 kanpaf")).click()
driver.switchTo().defaultContent()

elems = driver.find_elements(By.CSS_SELECTOR, "div.ebook__img--container a")


driver.get(elems[4].get_attribute('href'))

driver.find_element(By.NAME, 'name').send_keys('test')
driver.find_element(By.NAME, 'email').send_keys('test@o2.pl')
driver.find_element(By.NAME, 'company').send_keys('test')
driver.find_element(By.NAME, 'url').send_keys('https://test.pl')
driver.find_element(By.NAME, 'phoneNumber').send_keys('666666666')




# driver.close()
