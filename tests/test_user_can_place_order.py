import allure
from locators.constructor_locator import modal_order
from pages.base_page import BasePage
from pages.constructor_page import ConstructorPage
from tests.data import DEFAULT_ORDER_NUMBER
from tests.url import URL


class TestOrderPlacementForLoggedInUser:
    @allure.step('залогиненный пользователь может оформить заказ.')
    def test_user_can_place_order(self, browser):
        base_page = BasePage(browser)
        can_place_order = ConstructorPage(browser)
        with allure.step('Открываем страницу c конструктором. Проходим авторизацию'):
            email, password, access_token = base_page.create_user()
            base_page.login(email, password, access_token)
        with allure.step('Добавляем ожидание для загрузки страницы с конструктором'):
            can_place_order.wait_for_page_load(f'{URL}')
        with allure.step('Собираем буругер и оформляем заказ'):
            can_place_order.create_burger_and_place_order()
        with allure.step('Добавляем ожидание для загрузки страницы с конструктором'):
            can_place_order.wait_for_element(modal_order)
        with allure.step('Проверяем, что номер заказа не равно 9999'):
            assert can_place_order.get_modal_order_text() != DEFAULT_ORDER_NUMBER
