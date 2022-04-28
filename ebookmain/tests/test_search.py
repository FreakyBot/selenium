import time
import xlrd

from ebookmain.tests.base_test import BaseTest

import pytest
from selenium.webdriver.common.by import By

from ebookmain.pages.result import EbookResult
from ebookmain.pages.search_ebook import SearchEbook
from ebookmain.utils.read_excel import ExcelReader


@pytest.mark.usefixtures("setup")
class TestResult(BaseTest):

    @pytest.mark.parametrize("data", ExcelReader.get_data())
    def test_search(self, data):
        self.driver.get("https://www.salesmanago.com/info/knowledgecenter.htm")
        search_ebook = SearchEbook(self.driver)
        results_ebook = EbookResult(self.driver)
        search_ebook.close_cookies()
        search_ebook.closing_live_chat()
        results_ebook.search(data.szukana_nazwa)
        search_ebook.input_name("test")
        search_ebook.input_email("jan.kowalski.benhauer+testrekrutacja@salesmanago.com")
        search_ebook.input_company("company")
        search_ebook.input_url("https://test.pl")
        search_ebook.input_phonenumber("732104858")
        search_ebook.submit_button()
        # self.driver.find_element(By.CSS_SELECTOR, '/html/body/main/div[2]/div/div[2]/div[2]/div/div/a[1]').click()'
        time.sleep(5)


        # assert len(results_ebook.get_url_links(search=)) == "https://www.salesmanago.com/info/zero-party-data-revolution.htm"
