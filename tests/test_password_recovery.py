import allure

from pages.password_recovery_page import PasswordRecoveryPage
from tests.url import LOGIN
from tests.url import URL, RESET_PASSWORD, FORGOT_PASSWORD


class TestPasswordRecovery:

    @allure.title('переход на страницу восстановления пароля по кнопке «Восстановить пароль»,')
    def test_password_recovery_page(self, browser):
        recovery_page = PasswordRecoveryPage(browser)
        with allure.step('Открываем страницу авторизации'):
            recovery_page.open(f'{URL}{LOGIN}')
        with allure.step('Нажимаем на кнопку "Восстановить пароль"'):
            recovery_page.click_button_password_recovery()
        with allure.step('Проверяем, что открылась страница восстановления пароля'):
            assert recovery_page.get_current_url() == f'{URL}{FORGOT_PASSWORD}'

    @allure.title('ввод почты и клик по кнопке «Восстановить»')
    def test_password_reset_email_submission(self, browser):
        reset_email = PasswordRecoveryPage(browser)
        with allure.step('Открываем страницу авторизации'):
            reset_email.open(f'{URL}{FORGOT_PASSWORD}')
        with allure.step('Вводим почту'):
            reset_email.send_keys_email_input_recovery_password()
        with allure.step('Нажимаем кнопку "Восстановить"'):
            reset_email.click_button_recovery()
        with allure.step('Добавляем ожидание для загрузки страницы'):
            reset_email.wait_for_page_load(f'{URL}{RESET_PASSWORD}')
        with allure.step('Проверяем, что открылась страница восстановления пароля'):
            assert reset_email.get_current_url() == f'{URL}{RESET_PASSWORD}'

    @allure.title('клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    def test_show_activates_password_field(self, browser):
        activates_password_field = PasswordRecoveryPage(browser)
        with allure.step('Открываем страницу авторизации'):
            activates_password_field.open(f'{URL}{LOGIN}')
        with allure.step('Нажимаем на кнопку "Восстановить пароль"'):
            activates_password_field.click_button_password_recovery()
        with allure.step('Вводим почту'):
            activates_password_field.send_keys_email_input_recovery_password()
        with allure.step('Нажимаем кнопку "Восстановить"'):
            activates_password_field.click_button_recovery()
        with allure.step('Добавляем ожидание для загрузки страницы'):
            activates_password_field.wait_for_page_load(f'{URL}{RESET_PASSWORD}')
        with allure.step('Нажимает на кнопку "Показать/Скрыть" пароль'):
            activates_password_field.show_hide_button_click()
        with allure.step('Проверяем, что поле пароля активно'):
            assert 'input_status_active' in activates_password_field.get_show_password().get_attribute('class')