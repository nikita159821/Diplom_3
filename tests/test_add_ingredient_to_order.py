import allure
from pages.main_page import MainPage
from tests.data import COUNT_INGREDIENT


class TestIngredientDragAndDrop:

    @allure.step('при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_drag_and_drop_ingredient(self, browser):
        drag_and_drop = MainPage(browser)
        with allure.step('Открываем страницу c конструктором'):
            drag_and_drop.open()
        with allure.step('Получаем ингредиент и конструктор бургера'):
            ingredient = drag_and_drop.get_ingredient()
            burger_constructor = drag_and_drop.get_constructor_burger()
        with allure.step('Перетаскиваем ингредиент в конструктор'):
            drag_and_drop.drag_and_drop_element(ingredient, burger_constructor)
        with allure.step('Проверяем, что счетчик ингредиента увеличился'):
            assert drag_and_drop.get_count_ingredient() == COUNT_INGREDIENT
