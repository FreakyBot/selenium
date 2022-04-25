from selenium.webdriver.common.by import By


class EbookResult:

    def __init__(self, driver):
        self.driver = driver
        self.ebook_xpath = "div.ebook__img--container a"

    def get_url_links(self):
        ebooks = self.driver.find_elements(By.CSS_SELECTOR, self.ebook_xpath)
        return [ebook.get_attribute('href') for ebook in ebooks]


