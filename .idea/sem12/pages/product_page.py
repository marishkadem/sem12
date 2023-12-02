from pages.base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait

class ProductPage(BasePage):

    def add_to_basket(self):
        button_add_basket = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        button_add_basket.click()

    def return_prod_name(self):
        return self.browser.find_element(*ProductPageLocators.PROD_NAME).text

    def return_prod_price(self):
        return self.browser.find_element(*ProductPageLocators.PROD_PRICE).text

    def is_right_good(self, prod_name):
        #print("prod_name " , prod_name)
        assert self.browser.find_elements(*ProductPageLocators.ARRAY_MESSAGE)[0].text == prod_name, "Product is not right"

    def is_right_price(self, prod_price):
        #print("prod_price " , prod_price)
        assert self.browser.find_elements(*ProductPageLocators.ARRAY_MESSAGE)[2].text == prod_price, "Price is not right"

    def should_not_be_success_message(self):
        assert self.is_not_elements_present(*ProductPageLocators.SUCCESS_MESSAGE)[0], \
            "Success message is presented, but should not be"

