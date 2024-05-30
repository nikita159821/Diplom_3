import allure
from locators.personal_account_locators import *
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Нажимает на кнопку "Выйти"')
    def click_button_exit(self):
        self.click_element(button_exit)
