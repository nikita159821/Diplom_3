from selenium.webdriver.common.by import By

button_password_recovery = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")
email_input_password_recovery = (By.CSS_SELECTOR, 'input.text')
button_recovery = (By.CSS_SELECTOR, '.button_button__33qZ0')
title_password_recovery = (By.XPATH, "//h2[text()='Восстановление пароля']")
show_hide_button = (By.CSS_SELECTOR, '.input__icon')
password_field = (By.CSS_SELECTOR, 'div.input_status_active')