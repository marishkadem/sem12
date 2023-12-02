from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' not in cyrrent URL"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    #проверка, что есть форма регистрации на странице
    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self,email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        password_field1 = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD1)
        password_field2 = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD2)
        password_field1.send_keys(password)
        password_field2.send_keys(password)
        reg_button =  self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        reg_button.click()


    