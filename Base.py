from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class Page(BasePage):
    element_locator1 = (By.ID, 'locator')
    element_locator2 = (By.XPATH, 'locator')
    element_locator3 = (By.CLASS_NAME, 'locator')
    element_locator4 = (By.CSS_SELECTOR, 'locator')
    element_locator5 = (By.NAME, 'locator')

    def __init__(self, driver, wait, action):
        super().__init__(driver, wait, action)
