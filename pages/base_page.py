import allure
import requests
import random
import string
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_functionality_locator import order_feed_button, ingredient, buns, constructor_burger, \
    arrange_order_button, close_modal_order, constructor_button, modal_order
from locators.order_feed_locator import completed_all_time
from locators.personal_account_locators import button_personal_account, email_input, password_input, button_enter, \
    order_history_link
from tests.url import URL
from selenium.webdriver.support import expected_conditions as EC, expected_conditions


# Класс для кастомного условия ожидания
class element_to_be:
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        driver.find_element(*self.locator)


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.actions = ActionChains(self.browser)

    @allure.step('Генерация случайных данных для пользователя')
    def generate_user_data(self):
        email = f"test-data-{random.randint(1, 10000)}@yandex.ru"
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        name = f"TestUser{random.randint(1, 100)}"
        return email, password, name

    @allure.step('Создание пользователя')
    def create_user(self):
        email, password, name = self.generate_user_data()
        url = "https://stellarburgers.nomoreparties.site/api/auth/register"
        data = {
            "email": email,
            "password": password,
            "name": name
        }
        response = requests.post(url, json=data)
        response.raise_for_status()

        access_token = response.json()['accessToken'].split(' ')[1]

        return email, password, access_token

    @allure.step('Удаление пользователя')
    def delete_user(self, access_token):
        url = "https://stellarburgers.nomoreparties.site/api/auth/user"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        response = requests.delete(url, headers=headers)
        response.raise_for_status()

    @allure.step('Открывает страницу с конструктором + выполняет авторизацию пользователя')
    def login(self, email, password, access_token):
        self.open()
        self.click_personal_account()
        self.send_keys_email_input(email)
        self.send_keys_password_input(password)
        self.click_button_enter()
        return email, password, access_token

    @allure.step('Общий метод для получения атрибута элемента')
    def get_attribute_of_element(self, locator, attribute):
        element = self.find(locator)
        return element.get_attribute(attribute)

    @allure.step('Кастомные условия ожидания')
    def wait_for_element(self, locator):
        try:
            WebDriverWait(self.browser, 3).until(element_to_be(locator))
        except TimeoutException:
            return False
        return True

    @allure.step('Явное ожидание. Пока элемент не будет кликабелен')
    def wait(self, locator):
        WebDriverWait(self.browser, 10).until(expected_conditions.element_to_be_clickable(locator))
        return self.browser.find_element(*locator)

    @allure.step('Ждет загрузки страницы с указанным URL.')
    def wait_for_page_load(self, url):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.url_to_be(url))

    @allure.step('Поиск элемента')
    def find_element(self, *args):
        return self.browser.find_element(*args)

    @allure.step('Общий метод для поиска элемента')
    def find(self, locator):
        return self.find_element(*locator)

    @allure.step('Поиск элементов')
    def find_elements(self, *args):
        return self.browser.find_elements(*args)

    @allure.step('Общий метод для клика по элементу')
    def click_element(self, locator):
        element = self.find(locator)
        element.click()

    @allure.step('Общий метод для ввода данных')
    def send_keys(self, locator, text):
        element = self.find(locator)
        element.send_keys(text)

    @allure.step('Открывает главную страницу')
    def open(self, url=None):
        if url is not None:
            self.browser.get(url)
        else:
            self.browser.get(URL)

    @allure.step('Возвращаем текущую страницу')
    def get_current_url(self):
        return self.browser.current_url

    @allure.step('Общий метод для получения текста элемента')
    def get_text_of_element(self, locator):
        element = self.find(locator)
        return element.text

    @allure.step('Нажимает на кнопку "Конструктор"')
    def click_constructor_button(self):
        self.click_element(constructor_button)

    @allure.step('Создает бургер и оформляет заказ')
    def create_burger_and_place_order(self):
        ingredient = self.get_ingredient()
        buns = self.get_buns()
        burger_constructor = self.get_constructor_burger()
        self.drag_and_drop_element(buns, burger_constructor)
        self.drag_and_drop_element(ingredient, burger_constructor)
        self.click_order_button()

    def create_order_and_check_in_feed(self):
        with allure.step('Нажимаем "Конструктор"'):
            self.click_constructor_button()
        with allure.step('Добавляем ожидание для загрузки страницы'):
            self.wait_for_element(ingredient)
        with allure.step('Собираем бургер и оформляем заказ'):
            self.create_burger_and_place_order()
        with allure.step('Добавляем ожидание для появления окна с заказом'):
            self.wait_for_element(close_modal_order)
        with allure.step('Закрываем окно с заказом'):
            self.get_close_modal_order()
        with allure.step('Открываем страницу "Лента заказов"'):
            self.click_order_feed_button()
        with allure.step('Добавляем ожидание для загрузки страницы'):
            self.wait_for_element(completed_all_time)

    @allure.step('Нажимает на кнопку "Личный кабинет')
    def click_personal_account(self):
        self.click_element(button_personal_account)

    @allure.step('Вводит почту в поле на странице авторизации')
    def send_keys_email_input(self, email):
        self.browser.find_element(*email_input).send_keys(email)

    @allure.step('Вводит пароль в поле на странице авторизации')
    def send_keys_password_input(self, password):
        self.browser.find_element(*password_input).send_keys(password)

    @allure.step('Нажатие на кнопку "Войти"')
    def click_button_enter(self):
        self.browser.find_element(*button_enter).click()

    @allure.step('Нажимает на кнопку "Лента заказов"')
    def click_order_feed_button(self):
        self.click_element(order_feed_button)

    @allure.step('Возвращает ингредиент')
    def get_ingredient(self):
        return self.find(ingredient)

    @allure.step('Возвращает булку')
    def get_buns(self):
        return self.find(buns)

    @allure.step('Возвращает конструктор бургера')
    def get_constructor_burger(self):
        return self.find(constructor_burger)

    @allure.step('Перетаскивает элемент из одного места в другое')
    def drag_and_drop_element(self, source, target):
        self.actions.drag_and_drop(source, target).perform()

    @allure.step('Нажимает "Оформить заказ')
    def click_order_button(self):
        self.click_element(arrange_order_button)

    @allure.step('Возвращает крестик для закрытия окна с заказом')
    def get_close_modal_order(self):
        self.click_element(close_modal_order)

    @allure.step('Нажимает на кнопку "История заказов"')
    def click_button_history(self):
        self.click_element(order_history_link)

    @allure.step('Возвращает номер заказа')
    def get_modal_order_text(self):
        return self.get_text_of_element(modal_order)
