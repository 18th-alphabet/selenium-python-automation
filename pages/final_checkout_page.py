from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages import path


class FinalCheckout(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Checkout complete
    def final_checkout(self):
        order_placed_datacheck = self.find_element(By.CLASS_NAME, path.completeheader).text
        order_dispatch_datacheck = self.find_element(By.CLASS_NAME, path.completetext).text
        self.find_element(By.CLASS_NAME, path.button).click()
        self.assertion_check(order_placed_datacheck, path.orderplaced)
        self.assertion_check(order_dispatch_datacheck, path.orderdispatched)

