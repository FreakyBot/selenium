import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from ebookmain.utils.driver_factory import DriverFactory


class BaseTest:

    @pytest.fixture()
    def setup(self):
        self.driver = DriverFactory.get_driver("chrome")
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(5)
        yield
        self.driver.quit()
