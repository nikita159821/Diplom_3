import allure
from pages.constructor_page import ConstructorPage
from tests.data import COUNT_INGREDIENT


class TestIngredientDragAndDrop:

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
