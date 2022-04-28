from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SearchEbook:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.search_input_name = "name"
        self.search_input_email = "email"
        self.search_input_company = "company"
        self.search_input_url = "url"
        self.search_input_phonenumber = "phoneNumber"
        self.search_submit_button = '//*[@id="uspForm"]/div[2]/div/button'
        self.closing_cookies = '//*[@id="close-cookies"]'
        self.search_download_file = '/html/body/main/div[2]/div/div[2]/div[2]/div/a[1]'

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

    def submit_button(self):
        self.driver.find_element(By.XPATH, '//*[@id="uspForm"]/div[2]/div/button').click()

    def close_cookies(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.closing_cookies))).click()

    def closing_live_chat(self):
        self.wait.until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.XPATH, '//*[@id="hubspot-messages-iframe-container"]/iframe')))
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@aria-label='Close live chat']"))).click()
        except TimeoutException as to:
            print(to)
        self.driver.switch_to.default_content()

    def download(self):
        self.driver.find_element(By.XPATH, self.search_download_file).click()




