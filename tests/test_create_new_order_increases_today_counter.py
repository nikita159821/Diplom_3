import allure
from locators.order_feed_locator import completed_all_time
from pages.base_page import BasePage
from pages.order_feed_page import OrderFeedPage


class TestCreateNewOrderIncreasesTodayCounter:

    @allure.title('при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_create_new_order_increases_today_counter(self, browser):
        base_page = BasePage(browser)
        today_counter = OrderFeedPage(browser)
        with allure.step('Открываем страницу c конструктором. Проходим авторизацию'):
            email, password, access_token = base_page.create_user()
            base_page.login(email, password, access_token)
        with allure.step('Открываем страницу "Лента заказов"'):
            today_counter.click_order_feed_button()
        with allure.step('Добавляем ожидание для загрузки страницы'):
            today_counter.wait_for_element(completed_all_time)
        with allure.step('Сохраняем кол-во заказов сегодня до создания нового'):
            count_number = today_counter.get_completed_today()
            today_counter.create_order_and_check_in_feed()
        with allure.step('Проверяем, что новое значение не равно "count_number"'):
            assert today_counter.get_completed_today() != count_number
