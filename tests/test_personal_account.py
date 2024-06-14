import allure
import pytest

from locators.personal_account_locators import order_history_link, button_exit
from pages.authorizations_page import AuthorizationsPage
from pages.personal_account_page import PersonalAccountPage
from tests.url import URL, LOGIN, HISTORY


class TestPersonalAccount:

    @allure.title('Переход по клику на «Личный кабинет»,"')
    def test_personal_cabinet_navigation(self, browser):
        personal_cabinet = PersonalAccountPage(browser)
        with allure.step('Открываем главную страницу'):
            personal_cabinet.open()
        with allure.step('Нажимаем на кнопку "Личный кабинет"'):
            personal_cabinet.click_personal_account()
        with allure.step('Проверяем, что открылась страница авторизации'):
            assert personal_cabinet.get_current_url() == f'{URL}{LOGIN}'

    @pytest.mark.usefixtures("create_and_delete_user")
    @allure.title('Переход в раздел «История заказов»')
    def test_navigate_to_order_history(self, browser, create_and_delete_user):
        response, payload = create_and_delete_user
        email = payload['email']
        password = payload['password']
        order_history = PersonalAccountPage(browser)
        auth = AuthorizationsPage(browser)
        with allure.step('Открываем страницу c конструктором. Проходим авторизацию'):
            auth.login(email, password)
        with allure.step('Нажимаем на кнопку "Личный кабинет"'):
            order_history.click_personal_account()
        with allure.step('Добавляем ожидание для загрузки страницы'):
            order_history.wait(order_history_link)
        with allure.step('Нажимаем на кнопку "История заказов"'):
            order_history.click_button_history()
        with allure.step('Проверяем, что открылась страница "История заказов"'):
            assert order_history.get_current_url() == f'{URL}{HISTORY}'

    @allure.title('Выход из аккаунта.')
    def test_logout_your_account(self, browser, create_and_delete_user):
        response, payload = create_and_delete_user
        email = payload['email']
        password = payload['password']
        logout_your = PersonalAccountPage(browser)
        auth = AuthorizationsPage(browser)
        with allure.step('Открываем страницу c конструктором. Проходим авторизацию'):
            auth.login(email, password)
        with allure.step('Нажимаем на кнопку "Личный кабинет"'):
            logout_your.click_personal_account()
        with allure.step('Добавляем ожидание для загрузки страницы'):
            logout_your.wait(button_exit)
        with allure.step('Нажимаем на кнопку "Выйти"'):
            logout_your.click_button_exit()
        with allure.step('Добавляем ожидание для загрузки страницы'):
            logout_your.wait_for_page_load(f'{URL}{LOGIN}')
        with allure.step('Проверяем, что открылась страница авторизации'):
            assert logout_your.get_current_url() == f'{URL}{LOGIN}'
