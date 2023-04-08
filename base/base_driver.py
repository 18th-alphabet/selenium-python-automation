import datetime

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseDriver:

    def __init__(self, driver):
        self.driver = driver

    def wait_element_to_be_clickable(self, locator, locator_value):
        wait = WebDriverWait(self.driver, 3)
        elements = wait.until(EC.element_to_be_clickable((locator, locator_value)))
        return elements

    def find_element(self, locator, locator_value):
        try:
            elements = self.driver.find_element(locator, locator_value)
            return elements
        except:
            self.screenshot_with_time()

    def screenshot_with_time(self):
        time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_name = self.driver.title
        time_stamp = f"{time}"
        self.driver.get_screenshot_as_file(f"C:/Users/rahul/PycharmProjects/TestFramework/screenshots/{file_name}_{time_stamp}.png")

    def assertion_check(self, expected, actual):
        assert expected == actual


