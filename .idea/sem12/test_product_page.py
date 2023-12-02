from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.locators import ProductPageLocators
from selenium.webdriver.common.by import By
import pytest
import time

class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    #открываем страницу регистрации и регистрируем пользователя
    def setup(self,browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        self.browser=browser
        self.browser.get(link)
        login_page = LoginPage(self.browser,link)
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "Igfufn27" +str(time.time())
        print(password)
        login_page.register_new_user(email,password)
        login_page.should_be_authorized_user()

    #проверяем, что нет сообщения об успехе
    def test_user_cant_see_success_message(self,browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
        product_page = ProductPage(browser, link)
        product_page.open()
        assert product_page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.is_right_good(product_page.return_prod_name())
        product_page.is_right_price(product_page.return_prod_price())

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    assert not product_page.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE),"Success message is presented"

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    assert product_page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented and not disappeared!"
#@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    #перешли в корзину
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_message_about_empty_basket()
    basket_page.is_empty_basket() #нет сообщения одобавлении товара в корзину
    basket_page.is_not_message_about_empty_basket()


product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{index}" for index in range(0,10) if index != 7]
for_xfail = pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail)
urls.insert(7,for_xfail)

#@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    #time.sleep(100)
    product_page.is_right_good(product_page.return_prod_name())
    product_page.is_right_price(product_page.return_prod_price())
