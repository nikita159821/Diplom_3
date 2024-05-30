import allure
from pages.password_ecovery_page import PasswordRecoveryPage
from tests.url import URL, LOGIN, RESET_PASSWORD


class TestClickShowHide:
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