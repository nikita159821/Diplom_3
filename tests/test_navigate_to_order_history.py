import allure
from locators.personal_account_locators import order_history_link
from pages.base_page import BasePage
from pages.personal_account_page import PersonalAccountPage
from tests.url import URL, HISTORY


class TestToOrderHistory:

    @allure.title('Переход в раздел «История заказов»')
    def test_navigate_to_order_history(self, browser):
        base_page = BasePage(browser)
        order_history = PersonalAccountPage(browser)
        with allure.step('Открываем страницу c конструктором. Проходим авторизацию'):
            email, password, access_token = base_page.create_user()
            base_page.login(email, password, access_token)
        with allure.step('Нажимаем на кнопку "Личный кабинет"'):
            order_history.click_personal_account()
        with allure.step('Добавляем ожидание для загрузки страницы'):
            order_history.wait(order_history_link)
        with allure.step('Нажимаем на кнопку "История заказов"'):
            order_history.click_button_history()
        with allure.step('Проверяем, что открылась страница "История заказов"'):
            assert order_history.get_current_url() == f'{URL}{HISTORY}'