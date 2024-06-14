import requests
from selenium import webdriver
import pytest
import sys
import os
from tests.helpers import generate_user_data
from tests.url import URL, CREATE_USER, DELETE_USER

# Добавляем путь к директории "pages"
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@pytest.fixture
def browser():
    driver_browser = webdriver.Chrome()
    driver_browser.maximize_window()
    yield driver_browser
    driver_browser.quit()


@pytest.fixture(scope="function")
def create_and_delete_user():
    """
    Фикстура для создания и удаления пользователя.
    """
    payload = generate_user_data()
    response = requests.post(URL + CREATE_USER, json=payload)
    yield response, payload
    access_token = response.json()['accessToken']
    requests.delete(URL + DELETE_USER, headers={'Authorization': access_token})