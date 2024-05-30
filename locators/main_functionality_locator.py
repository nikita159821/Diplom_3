from selenium.webdriver.common.by import By

constructor_button = (By.XPATH, "//p[contains(., 'Конструктор')]")
order_feed_button = (By.XPATH, "//p[contains(., 'Лента Заказов')]")
ingredient = (By.XPATH, "//p[contains(., 'Соус Spicy-X')]")
buns = (By.XPATH, "//p[contains(., 'Флюоресцентная булка R2-D3')]")
arrange_order_button = (By.XPATH, "//button[contains(., 'Оформить заказ')]")
modal_window_ingredient = (By.CSS_SELECTOR, '.Modal_modal__title_modified__3Hjkd')
close_modal_window_ingredient = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
close_modal = (By.XPATH, "//div[@class='App_App__aOmNj']/section[@class='Modal_modal__P3_V5']")
constructor_burger = (By.CSS_SELECTOR, '.BurgerConstructor_basket__list__l9dp_')
count_ingredient = (By.XPATH, "//p[@class='counter_counter__num__3nue1'][contains(., '1')]")
modal_order = (By.CSS_SELECTOR, '.Modal_modal__title_shadow__3ikwq')
close_modal_order = (By.CSS_SELECTOR, '.Modal_modal__close_modified__3V5XS')