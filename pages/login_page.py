from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages import path


class LoginPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Correct input of Username, Password
    def enter_username_password(self, username, password):
        self.find_element(By.ID, path.username).send_keys(username)
        self.find_element(By.ID, path.password).send_keys(password)

    def click_login(self):
        self.find_element(By.CLASS_NAME, path.submitbutton).click()


