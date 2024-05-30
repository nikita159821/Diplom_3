import allure
from locators.main_functionality_locator import *
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Нажимает на ингредиент')
    def click_ingredient(self):
        self.click_element(ingredient)

    @allure.step('Возвращает счетчик с количеством ингредиента')
    def get_count_ingredient(self):
        return self.get_text_of_element(count_ingredient)

    @allure.step('Возвращает модальное окно "Детали ингредиента"')
    def get_modal_window_ingredient(self):
        return self.get_text_of_element(modal_window_ingredient)

    @allure.step('Возвращает класс модального окна')
    def get_modal_class(self):
        return self.get_attribute_of_element(close_modal, 'class')

    @allure.step('Нажимает на крестик в модальном окне "Детали ингредиента"')
    def click_close_modal_window_ingredient(self):
        self.click_element(close_modal_window_ingredient)