import allure
from pages.password_ecovery_page import PasswordRecoveryPage
from tests.url import URL, FORGOT_PASSWORD, RESET_PASSWORD


class TestPasswordResetEmail:

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