import allure
from locators.constructor_locator import close_modal_order
from locators.order_feed_locator import completed_all_time
from pages.base_page import BasePage
from pages.constructor_page import ConstructorPage
from tests.conftest import browser


class TestNewOrderAppearsInWorkSection:

    @allure.title('после оформления заказа его номер появляется в разделе В работе.')
    def test_new_order_appears_in_work_section(self, browser):
        base_page = BasePage(browser)
        in_work = ConstructorPage(browser)
        with allure.step('Открываем страницу c конструктором. Проходим авторизацию'):
            email, password, access_token = base_page.create_user()
            base_page.login(email, password, access_token)
        with allure.step('Добавляем ожидание для загрузки страницы'):
            in_work.wait_for_element(completed_all_time)
        with allure.step('Собираем бургер и оформляем заказ'):
            in_work.create_burger_and_place_order()
        with allure.step('Добавляем ожидание для появления окна с заказом'):
            in_work.wait_for_element(close_modal_order)
        with allure.step('Получаем номер заказа'):
            number_order = in_work.get_modal_order_text()
        with allure.step('Закрываем окно с заказом'):
            in_work.get_close_modal_order()
        with allure.step('Открываем страницу "Лента заказов"'):
            in_work.click_order_feed_button()
        with allure.step('Добавляем ожидание для загрузки страницы'):
            in_work.wait_for_element(completed_all_time)
        with allure.step('Получаем номер заказа в работе'):
            count_number = in_work.get_at_work()
        with allure.step('Сравниваем, что номер заказа в работе совпадает с "number_order"'):
            assert count_number.lstrip('0') == number_order
