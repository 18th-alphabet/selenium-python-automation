from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages import path


class AddToCartAndCheckout(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Add to cart of product and checkout
    def add_to_cart_and_checkout(self):
        try:
            self.find_element(By.NAME, path.addtocart1).click()
            self.find_element(By.NAME, path.addtocart2).click()
            self.find_element(By.XPATH, path.cartlink).click()
            self.find_element(By.ID, path.checkout).click()
        except:
            self.screenshot_with_time()
