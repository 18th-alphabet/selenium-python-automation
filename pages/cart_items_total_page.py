from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages import path


class CartItemsTotal(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Cart items and total amount, Finish button
    def cart_items_total(self):
        sub_total_datacheck = self.find_element(By.XPATH, path.summarysubtotallabel).text
        tax_total_datacheck = self.find_element(By.XPATH, path.summarytaxlabel).text
        total_amount_datacheck = self.find_element(By.XPATH, path.totallabel).text
        self.driver.find_element(By.NAME, path.finishicon).click()
        self.assertion_check(sub_total_datacheck, path.subtotal)
        self.assertion_check(tax_total_datacheck, path.taxtotal)
        self.assertion_check(total_amount_datacheck, path.totalamount)

