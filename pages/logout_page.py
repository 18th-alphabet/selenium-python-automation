from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages import path


class Logout(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Hamburger icon
    def hamburger_icon_logout(self):
        self.find_element(By.ID, path.hamburgericon).click()
        self.wait_element_to_be_clickable(By.XPATH, path.logout)