from selenium import webdriver
from ebook.result import EbookResult
from ebook.home_page import EbookHomePage
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class TestResult:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(5)
        yield
        self.driver.quit()

    def test_search(self, setup):
        self.driver.get("https://www.salesmanago.com/info/knowledgecenter.htm")