import allure
from pages.authorizations_page import AuthorizationsPage
from pages.constructor_page import ConstructorPage
from pages.order_feed_page import OrderFeedPage
from tests.data import DEFAULT_ORDER_NUMBER, INGREDIENT_DETAILS, COUNT_INGREDIENT
from tests.url import LOGIN, URL, FEED


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

    @allure.title('переход по клику на «Лента заказов»')
    def test_navigate_to_order_feed(self, browser):
        to_order_feed = ConstructorPage(browser)
        click_order_feed = OrderFeedPage(browser)
        with allure.step('Открываем страницу авторизации'):
            to_order_feed.open(f'{URL}{LOGIN}')
        with allure.step('Нажимаем кнопку "Лента заказов"'):
            click_order_feed.click_order_feed_button()
        with allure.step('Проверяем переход на страницу "Лента заказов"'):
            assert to_order_feed.get_current_url() == f'{URL}{FEED}'

    @allure.title('если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_ingredient_displays_popup_with_details(self, browser):
        click_ingredient_popup = ConstructorPage(browser)
        with allure.step('Открываем страницу c конструктором'):
            click_ingredient_popup.open()
        with allure.step('Нажимаем на ингредиент'):
            click_ingredient_popup.click_ingredient()
        with allure.step('Проверяем, что появилось модальное окно и содержит текст "INGREDIENT_DETAILS"'):
            assert click_ingredient_popup.get_modal_window_ingredient() == INGREDIENT_DETAILS

    @allure.title('всплывающее окно закрывается кликом по крестику')
    def test_ingredient_popup_close(self, browser):
        ingredient_popup_close = ConstructorPage(browser)
        with allure.step('Открываем страницу c конструктором'):
            ingredient_popup_close.open()
        with allure.step('Нажимаем на ингредиент'):
            ingredient_popup_close.click_ingredient()
        with allure.step('Закрываем окно с ингредиентом'):
            ingredient_popup_close.click_close_modal_window_ingredient()
        with allure.step('Проверяем, что окно больше не отображается'):
            assert 'Modal_modal__P3_V5' in ingredient_popup_close.get_modal_class()

    @allure.step('при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_counter_increments_when_ingredient_added_to_order(self, browser):
        ingredient_added_to_order = ConstructorPage(browser)
        with allure.step('Открываем страницу c конструктором'):
            ingredient_added_to_order.open()
        with allure.step('Получаем ингредиент и конструктор бургера'):
            ingredient = ingredient_added_to_order.get_ingredient()
            burger_constructor = ingredient_added_to_order.get_constructor_burger()
        with allure.step('Перетаскиваем ингредиент в конструктор'):
            ingredient_added_to_order.drag_and_drop_element(ingredient, burger_constructor)
        with allure.step('Проверяем, что счетчик ингредиента увеличился'):
            assert ingredient_added_to_order.get_count_ingredient() == COUNT_INGREDIENT

    @allure.step('залогиненный пользователь может оформить заказ.')
    def test_user_can_place_order(self, browser, create_and_delete_user):
        response, payload = create_and_delete_user
        email = payload['email']
        password = payload['password']
        can_place_order = ConstructorPage(browser)
        auth = AuthorizationsPage(browser)
        with allure.step('Открываем страницу c конструктором. Проходим авторизацию'):
            auth.login(email, password)
        with allure.step('Добавляем ожидание для загрузки страницы с конструктором'):
            can_place_order.wait_for_page_load(f'{URL}')
        with allure.step('Собираем бургер и оформляем заказ'):
            can_place_order.create_burger_and_place_order()
        with allure.step('Добавляем ожидание'):
            can_place_order.wait_loading_visibility(browser)
            can_place_order.wait_loading_invisibility(browser)
        with allure.step('Проверяем, что номер заказа не равно 9999'):
            assert can_place_order.get_modal_order_text() != DEFAULT_ORDER_NUMBER
