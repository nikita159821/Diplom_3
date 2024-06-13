import allure
from pages.constructor_page import ConstructorPage
from tests.url import LOGIN, URL


class TestToConstructor:

    @allure.title('переход по клику на «Конструктор»')
    def test_navigate_to_constructor(self, browser):
        to_constructor = ConstructorPage(browser)
        with allure.step('Открываем страницу авторизации'):
            to_constructor.open(f'{URL}{LOGIN}')
        with allure.step('Нажимаем кнопку "Конструктор"'):
            to_constructor.click_constructor_button()
        with allure.step('Проверяем переход на страницу "Конструктор"'):
            assert to_constructor.get_current_url() == f'{URL}'
