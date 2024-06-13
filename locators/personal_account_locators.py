from selenium.webdriver.common.by import By

button_personal_account = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
order_history_link = (By.XPATH, "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']")
button_exit = (By.CSS_SELECTOR, '.Account_button__14Yp3')
title_authorizations = (By.XPATH, "//h2[text()='Вход]")
order_history_item = (By.XPATH,"//div[@class='OrderHistory_orderHistory__qy1VB']/ul/li/a/div[@class='OrderHistory_textBox__3lgbs mb-6']/p[@class='text text_type_digits-default']")
