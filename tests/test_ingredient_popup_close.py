import allure
from pages.constructor_page import ConstructorPage


class TestIngredientPopupClose:

    @allure.title('если кликнуть на ингредиент, появится всплывающее окно с деталями,')
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
