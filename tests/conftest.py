from selenium import webdriver
import pytest
import sys
import os
from selenium.webdriver.chrome.options import Options

from pages.base_page import BasePage

# Добавляем путь к директории "pages"
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@pytest.fixture
def browser(request):
    options = Options()
    driver_browser = webdriver.Chrome(options=options)
    driver_browser.maximize_window()
    # Создаем пользователя и получаем токен доступа
    base_page = BasePage(driver_browser)
    email, password, access_token = base_page.create_user()
    yield driver_browser
    # Удаляем пользователя после теста
    base_page.delete_user(access_token)
    driver_browser.quit()