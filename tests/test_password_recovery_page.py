import allure
from pages.password_ecovery_page import PasswordRecoveryPage
from tests.url import URL, LOGIN, FORGOT_PASSWORD


class TestToOrderHistory:

    @allure.title('переход на страницу восстановления пароля по кнопке «Восстановить пароль»,')
    def test_password_recovery_page(self, browser):
        recovery_page = PasswordRecoveryPage(browser)
        with allure.step('Открываем страницу авторизации'):
            recovery_page.open(f'{URL}{LOGIN}')
        with allure.step('Нажимаем на кнопку "Восстановить пароль"'):
            recovery_page.click_button_password_recovery()
        with allure.step('Проверяем, что открылась страница восстановления пароля'):
            assert recovery_page.get_current_url() == f'{URL}{FORGOT_PASSWORD}'