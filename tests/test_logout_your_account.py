import allure
from locators.personal_account_locators import button_exit
from pages.base_page import BasePage
from pages.personal_account_page import PersonalAccountPage
from tests.url import URL, LOGIN


class TestLogoutAccount:

    @allure.title('Выход из аккаунта.')
    def test_logout_your_account(self, browser):
        base_page = BasePage(browser)
        logout_your = PersonalAccountPage(browser)
        with allure.step('Открываем страницу c конструктором. Проходим авторизацию'):
            email, password, access_token = base_page.create_user()
            base_page.login(email, password, access_token)
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