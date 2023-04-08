from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages import path

class CheckoutDetails(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Entering checkout details
    def checkout_details(self, firstname, lastname, zipcode):
        self.find_element(By.ID, path.firstname).send_keys(firstname)
        self.find_element(By.ID, path.lastname).send_keys(lastname)
        self.find_element(By.ID, path.postalcode).send_keys(zipcode)
        self.find_element(By.ID, path.continueicon).click()
