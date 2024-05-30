from selenium.webdriver.common.by import By

button_personal_account = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
email_input = (By.CSS_SELECTOR, 'input[name="name"]')
password_input = (By.CSS_SELECTOR, 'input[name="Пароль"]')
button_enter = (By.CSS_SELECTOR, '.button_button__33qZ0')
order_history_link = (By.XPATH, "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']")
button_exit = (By.CSS_SELECTOR, '.Account_button__14Yp3')
title_authorizations = (By.XPATH, "//h2[text()='Вход]")