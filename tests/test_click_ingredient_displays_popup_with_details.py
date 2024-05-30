import allure
from pages.main_page import MainPage
from tests.data import INGREDIENT_DETAILS


class TestClickIngredientPopup:

    @allure.title('если кликнуть на ингредиент, появится всплывающее окно с деталями,')
    def test_click_ingredient_displays_popup_with_details(self, browser):
        click_ingredient_popup = MainPage(browser)
        with allure.step('Открываем страницу c конструктором'):
            click_ingredient_popup.open()
        with allure.step('Нажимаем на ингредиент'):
            click_ingredient_popup.click_ingredient()
        with allure.step('Проверяем, что появилось модальное окно и содержит текст "INGREDIENT_DETAILS"'):
            assert click_ingredient_popup.get_modal_window_ingredient() == INGREDIENT_DETAILS
