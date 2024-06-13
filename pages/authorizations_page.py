import allure
from locators.authorizations_locator import *
from pages.base_page import BasePage


class AuthorizationsPage(BasePage):

    @allure.step('Вводит почту в поле на странице авторизации')
    def send_keys_email_input(self, email):
        self.find(email_input).send_keys(email)

    @allure.step('Вводит пароль в поле на странице авторизации')
    def send_keys_password_input(self, password):
        self.find(password_input).send_keys(password)

    @allure.step('Нажатие на кнопку "Войти"')
    def click_button_enter(self):
        self.find(button_enter).click()

    @allure.step('Открывает страницу с конструктором + выполняет авторизацию пользователя')
    def login(self, email, password):
        self.open()
        self.click_personal_account()
        self.send_keys_email_input(email)
        self.send_keys_password_input(password)
        self.click_button_enter()
