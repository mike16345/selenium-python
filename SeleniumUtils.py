from selenium.webdriver.support import expected_conditions as EC


class SeleniumUtils:
    def __init__(self, driver, wait, action):
        self.driver = driver
        self.wait = wait
        self.action = action

    def get_element(self, el_locator):
        return self.wait.until(EC.visibility_of_element_located(el_locator))

    def get_elements(self, el_locator):
        return self.wait.until(EC.visibility_of_all_elements_located(el_locator))

    def click_element(self, el_locator):
        self.wait.until(EC.element_to_be_clickable(el_locator)).click()

    def click_element_with_js(self, el_locator):
        self.driver.execute_script('arguments[0].click()', self.get_element(el_locator))

    def validate_visibility_of_element(self, el_locator):
        self.wait.until(EC.visibility_of(self.get_element(el_locator)))

    def validate_presence_of_element(self, el_locator):
        self.wait.until(EC.presence_of_element_located(self.get_element(el_locator)))

    def validate_text_in_element(self, element_locator, text_to_find):
        self.wait.until(EC.text_to_be_present_in_element(element_locator, text_to_find))

    def validate_number_of_elements_to_be(self, elements_locator, num_of_elements):
        self.wait.until(lambda method: len(self.driver.find_elements(*elements_locator)) == num_of_elements)
