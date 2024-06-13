import allure
from locators.password_ecovery_locator import *
from pages.base_page import BasePage
from tests.data import LOGIN


class PasswordRecoveryPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Нажимает на кнопку "Восстановить пароль"')
    def click_button_password_recovery(self):
        self.click_element(button_password_recovery)

    @allure.step('Вводит почту в поле на восстановления пароля')
    def send_keys_email_input_recovery_password(self):
        self.send_keys(email_input_password_recovery, LOGIN)

    @allure.step('Нажимает на кнопку "Восстановить"')
    def click_button_recovery(self):
        self.click_element(button_recovery)

    @allure.step('Нажимает на кнопку "Показать/Скрыть" пароль')
    def show_hide_button_click(self):
        self.click_element(show_hide_button)

    @allure.step('Возвращает кнопку "Показать/Скрыть" пароль')
    def get_show_password(self):
        return self.browser.find_element(*password_field)