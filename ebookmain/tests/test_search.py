from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from ebookmain.pages.search_ebook import EbookHomePage
from ebookmain.pages.result import EbookResult


class TestResult:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(5)
        yield
        self.driver.quit()

    def test_search(self, setup):
        self.driver.get("https://www.salesmanago.com/info/knowledgecenter.htm")
        search_ebook = EbookHomePage(self.driver)
        results_ebook = EbookResult(self.driver)
        search_ebook.close_cookies()
        results_ebook.search("zero")
        search_ebook.input_name("test")
        search_ebook.input_email("jan.kowalski.benhauer+testrekrutacja@salesmanago.com")
        search_ebook.input_company("company")
        search_ebook.input_name("https://test.pl")
        search_ebook.input_phonenumber("732104858")
        # search_ebook.search_button()

        # assert len(results_ebook.get_url_links(search=)) == "https://www.salesmanago.com/info/zero-party-data-revolution.htm"

