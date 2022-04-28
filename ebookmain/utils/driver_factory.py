from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class DriverFactory:

    @staticmethod
    def get_driver(browser):
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            options.add_experimental_option('prefs', {
                "download.prompt_for_download": False,  # To auto download the file
                "download.directory_upgrade": True,
                "plugins.always_open_pdf_externally": False  # It will not show PDF directly in chrome
            })
            return webdriver.Chrome(ChromeDriverManager().install(), options=options)
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("start-maximized")
            return webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
        raise Exception('Provide valid driver name')
