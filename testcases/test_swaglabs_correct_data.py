import pytest
from pages.login_page import LoginPage
from pages.add_to_cart_checkout_page import AddToCartAndCheckout
from pages.checkout_details_page import CheckoutDetails
from pages.cart_items_total_page import CartItemsTotal
from pages.final_checkout_page import FinalCheckout
from pages.logout_page import Logout


@pytest.mark.swaglabs2
@pytest.mark.usefixtures("setup")
class TestSwagLabs1:
    def test_swag_labs_with_correct_input(self):
        # Input of Username, Password
        login = LoginPage(self.driver)
        login.enter_username_password("standard_user", "secret_sauce")
        login.click_login()

        # Add to cart and checkout
        add_to_cart_checkout = AddToCartAndCheckout(self.driver)
        add_to_cart_checkout.add_to_cart_and_checkout()

        # Entering checkout details
        checkout_details = CheckoutDetails(self.driver)
        checkout_details.checkout_details("Ashneer", "Grover", "530021")

        # Cart items and total amount, Finish button
        cart_items = CartItemsTotal(self.driver)
        cart_items.cart_items_total()

        # Checkout complete
        complete_checkout = FinalCheckout(self.driver)
        complete_checkout.final_checkout()

        # Hamburger icon and Logout
        logout = Logout(self.driver)
        logout.hamburger_icon_logout()
