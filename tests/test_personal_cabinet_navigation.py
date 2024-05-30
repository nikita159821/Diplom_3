import allure
from pages.personal_account_page import PersonalAccountPage
from tests.url import URL, LOGIN


class TestPersonalCabinet:

    @allure.title('Переход по клику на «Личный кабинет»,"')
    def test_personal_cabinet_navigation(self, browser):
        personal_cabinet = PersonalAccountPage(browser)
        with allure.step('Открываем главную страницу'):
            personal_cabinet.open()
        with allure.step('Нажимаем на кнопку "Личный кабинет"'):
            personal_cabinet.click_personal_account()
        with allure.step('Проверяем, что открылась страница авторизации'):
            assert personal_cabinet.get_current_url() == f'{URL}{LOGIN}'