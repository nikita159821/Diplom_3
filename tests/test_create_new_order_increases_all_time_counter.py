import allure
from locators.order_feed_locator import completed_all_time
from pages.base_page import BasePage
from pages.order_feed_page import OrderFeedPage


class TestOrderFeedAllTimeCounterIncreases:
    @allure.title('при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_orders_module_all_time_counter_increases(self, browser):
        base_page = BasePage(browser)
        orders_module_all_time = OrderFeedPage(browser)
        with allure.step('Открываем страницу c конструктором. Проходим авторизацию'):
            email, password, access_token = base_page.create_user()
            base_page.login(email, password, access_token)
        with allure.step('Открываем страницу "Лента заказов"'):
            orders_module_all_time.click_order_feed_button()
        with allure.step('Добавляем ожидание для загрузки страницы'):
            orders_module_all_time.wait_for_element(completed_all_time)
        with allure.step('Сохраняем кол-во заказов до создания нового'):
            count_number = orders_module_all_time.get_completed_all_time()
            orders_module_all_time.create_order_and_check_in_feed()
        with allure.step('Проверяем, что новое значение не равно "count_number"'):
            assert orders_module_all_time.get_completed_all_time() != count_number
