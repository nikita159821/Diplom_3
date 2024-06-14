import allure
from locators.personal_account_locators import *
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Нажимает на кнопку "Выйти"')
    def click_button_exit(self):
        self.click_element(button_exit)

    @allure.step('Нажимает на кнопку "История заказов"')
    def click_button_history(self):
        self.click_element(order_history_link)

    @allure.step('Возвращает номер последнего заказа в ЛК')
    def get_order_history_item(self):
        return self.get_text_of_element(order_history_item)
