import allure
from selenium.webdriver.support import expected_conditions as EC
from locators.constructor_locator import *
from locators.order_feed_locator import completed_all_time
from pages.base_page import BasePage
from pages.order_feed_page import OrderFeedPage
from tests.conftest import browser
from tests.url import URL


class ConstructorPage(BasePage):
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

    @allure.step('Нажимает на кнопку "Конструктор"')
    def click_constructor_button(self):
        self.click_element(constructor_button)

    @allure.step('Создает бургер и оформляет заказ')
    def create_burger_and_place_order(self):
        ingredient = self.get_ingredient()
        buns = self.get_buns()
        burger_constructor = self.get_constructor_burger()
        self.drag_and_drop_element(buns, burger_constructor)
        self.drag_and_drop_element(ingredient, burger_constructor)
        self.click_order_button()

    def wait_loading_visibility(self, browser):
        self.wait.until(EC.visibility_of_element_located(LOADING))

    def wait_loading_invisibility(self, browser):
        self.wait.until(EC.invisibility_of_element_located(LOADING))

    def create_order_and_check_in_feed(self, browser):
        order_feed_page = OrderFeedPage(self.browser)
        user_order_history = ConstructorPage(browser)
        with allure.step('Нажимаем "Конструктор"'):
            self.click_constructor_button()
        with allure.step('Добавляем ожидание для загрузки страницы с конструктором'):
            order_feed_page.wait_for_page_load(f'{URL}')
        with allure.step('Собираем бургер и оформляем заказ'):
            self.create_burger_and_place_order()
        with allure.step('Добавляем ожидание для появления окна с заказом'):
            user_order_history.wait_loading_visibility(browser)
            user_order_history.wait_loading_invisibility(browser)
        with allure.step('Закрываем окно с заказом'):
            self.get_close_modal_order()
        with allure.step('Открываем страницу "Лента заказов"'):
            order_feed_page.click_order_feed_button()
        with allure.step('Добавляем ожидание для загрузки страницы'):
            order_feed_page.wait(completed_all_time)

    @allure.step('Возвращает ингредиент')
    def get_ingredient(self):
        return self.find(ingredient)

    @allure.step('Возвращает булку')
    def get_buns(self):
        return self.find(buns)

    @allure.step('Возвращает конструктор бургера')
    def get_constructor_burger(self):
        return self.find(constructor_burger)

    @allure.step('Перетаскивает элемент из одного места в другое')
    def drag_and_drop_element(self, source, target):
        self.actions.drag_and_drop(source, target).perform()

    @allure.step('Нажимает "Оформить заказ')
    def click_order_button(self):
        self.click_element(arrange_order_button)

    @allure.step('Возвращает крестик для закрытия окна с заказом')
    def get_close_modal_order(self):
        self.click_element(close_modal_order)

    @allure.step('Возвращает номер заказа')
    def get_modal_order_text(self):
        return self.get_text_of_element(modal_order)
