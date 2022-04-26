from selenium.webdriver.common.by import By


class EbookResult:

    def __init__(self, driver):
        self.driver = driver
        self.ebook_xpath = "div.ebook__img--container a"

    def search(self, search):
        ebooks = self.driver.find_elements(By.CSS_SELECTOR, self.ebook_xpath)
        ebooks_links = [ebook.get_attribute('href') for ebook in ebooks]
        for ebook in ebooks_links:
            if search in ebook:
                print("Link " + ebook)
                return self.driver.get(ebook)









