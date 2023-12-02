from pages.base_page    import BasePage
from .locators          import BasketLocators
from .locators          import ProductPageLocators

class BasketPage(BasePage):
    def is_message_about_empty_basket(self):
        assert self.is_element_present(*BasketLocators.EMPTY_MESSAGE) , "Not found message about empty basket"

    def is_not_message_about_empty_basket(self):
        assert not self.is_not_element_present(*BasketLocators.EMPTY_MESSAGE), "Not found message about empty basket"

    def is_empty_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Basket is not empty"