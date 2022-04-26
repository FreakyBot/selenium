import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class EbookHomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.search_input_name = "name"
        self.search_input_email = "email"
        self.search_input_company = "company"
        self.search_input_url = "url"
        self.search_input_phonenumber = "phoneNumber"
        self.search_button = '''//*[@id="uspForm"]/div[2]/div/button'''
        self.closing_cookies = '//*[@id="close-cookies"]'

    def input_name(self, name):
        self.driver.find_element(By.NAME, self.search_input_name).send_keys(name)

    def input_email(self, email):
        self.driver.find_element(By.NAME, self.search_input_email).send_keys(email)

    def input_company(self, company):
        self.driver.find_element(By.NAME, self.search_input_company).send_keys(company)

    def input_url(self, url):
        self.driver.find_element(By.NAME, self.search_input_url).send_keys(url)

    def input_phonenumber(self, phone):
        self.driver.find_element(By.NAME, self.search_input_phonenumber).send_keys(phone)

    def search_button(self):
        self.driver.find_element(By.XPATH, self.search_button).click()
        
    def close_cookies(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.closing_cookies))).click()




