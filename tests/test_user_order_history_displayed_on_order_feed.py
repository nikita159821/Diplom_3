import allure
from locators.main_functionality_locator import modal_order
from locators.order_feed_locator import order_history_item, order_number
from pages.base_page import BasePage
from pages.constructor_page import ConstructorPage
from tests.url import URL, PROFILE


class TestUserOrderHistoryOnOrderFeed:

    @allure.step('заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»,')
    def test_user_order_history_displayed_on_order_feed(self, browser):
        base_page = BasePage(browser)
        user_order_history = ConstructorPage(browser)
        with allure.step('Открываем страницу c конструктором. Проходим авторизацию'):
            email, password, access_token = base_page.create_user()
            base_page.login(email, password, access_token)
        with allure.step('Добавляем ожидание для загрузки страницы с конструктором'):
            user_order_history.wait_for_page_load(f'{URL}')
        with allure.step('Собираем бургер и оформляем заказ'):
            user_order_history.create_burger_and_place_order()
        with allure.step('Добавляем ожидание для появления окна с заказом'):
            user_order_history.wait_for_element(modal_order)
        with allure.step('Закрываем модальное окно с заказом'):
            user_order_history.get_close_modal_order()
        with allure.step('Нажимаем на кнопку "Личный кабинет"'):
            user_order_history.click_personal_account()
        with allure.step('Добавляем ожидание для загрузки страницы'):
            user_order_history.wait_for_page_load(f'{URL}{PROFILE}')
        with allure.step('Нажимаем на кнопку "История заказов"'):
            user_order_history.click_button_history()
        with allure.step('Добавляем ожидание для загрузки страницы'):
            user_order_history.wait_for_element(order_history_item)
        with allure.step('Находим номер последнего заказа в ЛК'):
            last_order_number = user_order_history.get_order_history_item()
        with allure.step('Нажимаем кнопку "Лента заказов"'):
            user_order_history.click_order_feed_button()
        with allure.step('Добавляем ожидание для загрузки страницы'):
            user_order_history.wait_for_element(order_number)
        with allure.step('Находим номер заказа в ленте и сравниваем с номером из лк - "last_order_number"'):
            assert user_order_history.get_order() == last_order_number
