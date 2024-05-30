import allure
from locators.order_feed_locator import order_history
from pages.order_feed_page import OrderFeedPage


class TestOrderDetailsPopup:

    @allure.title('Переход в раздел «История заказов»')
    def test_open_order_details_popup(self, browser):
        order_details = OrderFeedPage(browser)
        with allure.step('Открываем главную страницу'):
            order_details.open()
        with allure.step('Нажимаем кнопку "Лента заказов"'):
            order_details.click_order_feed_button()
        with allure.step('Ожидание элемента перед кликом'):
            order_details.wait(order_history)
        with allure.step('Нажимаем на первый заказ в ленте'):
            order_details.click_order_history()
        with allure.step('Проверяем, что открылась окно с заказом'):
            assert order_details.get_popup_order_history().is_displayed()
