import allure

from pages.constructor_page import ConstructorPage
from tests.url import LOGIN, URL, FEED


class TestOrderFeed:

    @allure.title('переход по клику на «Лента заказов»')
    def test_navigate_to_order_feed(self, browser):
        to_order_feed = ConstructorPage(browser)
        with allure.step('Открываем страницу авторизации'):
            to_order_feed.open(f'{URL}{LOGIN}')
        with allure.step('Нажимаем кнопку "Лента заказов"'):
            to_order_feed.click_order_feed_button()
        with allure.step('Проверяем переход на страницу "Лента заказов"'):
            assert to_order_feed.get_current_url() == f'{URL}{FEED}'