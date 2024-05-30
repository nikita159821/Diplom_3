import allure
from locators.order_feed_locator import *
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Нажимает на первый заказ в списке')
    def click_order_history(self):
        self.click_element(order_history)

    @allure.step('Возвращает окно с информацией по заказу')
    def get_popup_order_history(self):
        return self.find(popup_order_history)

    @allure.step('Возвращает номер последнего заказа в ЛК')
    def get_order_history_item(self):
        return self.get_text_of_element(order_history_item)

    @allure.step('Возвращает номер последнего заказа в ленте')
    def get_order(self):
        return self.find_elements(*order_number)[0].text

    @allure.step('Возвращает количество заказов за все время')
    def get_completed_all_time(self):
        return self.get_text_of_element(completed_all_time)

    @allure.step('Возвращает количество заказов за сегодня')
    def get_completed_today(self):
        return self.get_text_of_element(completed_today)

    @allure.step('Возвращает количество заказов в работе')
    def get_at_work(self):
        return self.get_text_of_element(at_work)

