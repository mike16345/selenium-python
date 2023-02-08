import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from Client.Client import Database
from Pages.BasePage import BasePage


class TestBase:
    driver = None
    wait = None
    action = None
    db = None

    @pytest.fixture(scope='function', autouse=True)
    def set_up(self):
        self.driver = webdriver.Chrome()
        self.action = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)
        self.db = Database()
        URL = "http://localhost:3001/"
        b_page = BasePage(self.driver, self.wait, self.action)
        self.driver.get(URL)
        self.driver.maximize_window()
        b_page.s_utils.click_element(b_page.show_controls)
        yield self.driver
        self.db.disconnect()
        self.driver.quit()
