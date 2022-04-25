from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager


class TestResult:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(5)
        yield
        self.driver.quit()

    def test_search(self, setup):
        self.driver.get("https://www.salesmanago.com/info/knowledgecenter.htm")