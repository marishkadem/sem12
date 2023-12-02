from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR,"#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR,"#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR,"#id_registration-email")
    PASSWORD_FIELD1 = (By.CSS_SELECTOR,"#id_registration-password1")
    PASSWORD_FIELD2 = (By.CSS_SELECTOR,"#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR,'button[name = "registration_submit"]')

class ProductPageLocators():
    ADD_BASKET = (By.CSS_SELECTOR,".btn-add-to-basket")
    ARRAY_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
    PROD_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1") #фактическое название товара
    PROD_PRICE = (By.CSS_SELECTOR, "p.price_color") #фактическая цена товара
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,".alert:nth-child(1)>div")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_BASKET = (By.CSS_SELECTOR, ".btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketLocators():
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner")

