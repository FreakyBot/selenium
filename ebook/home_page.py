from selenium.webdriver.common.by import By


class EbookHomePage:

    def __init__(self,driver):
        self.driver = driver
        self.search_input_name = "name"
        self.search_input_email = "email"
        self.search_input_company = "company"
        self.search_input_url = "url"
        self.search_input_phonenumber = "phoneNumber"
        self.search_button = '//*[@id="uspForm"]/div[2]/div/button'

    def input_name(self, text):
        self.driver.find_element(By.NAME, self.search_input_name).send_keys(text)
    
    def input_email(self, text):
        self.driver.find_element(By.NAME, self.search_input_email).send_keys(text)

    def input_company(self, text):
        self.driver.find_element(By.NAME, self.search_input_company).send_keys(text)

    def input_url(self, text):
        self.driver.find_element(By.NAME, self.search_input_url).send_keys(text)

    def input_phonenumber(self, text):
        self.driver.find_element(By.NAME, self.search_input_phonenumber).send_keys(text)

    def search_button(self, text):
        self.driver.find_element(By.XPATH, self.search_button).click()

