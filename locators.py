from selenium.webdriver.common.by import By

class RegistrationLocators:
    REGISTER_HEADER = (By.XPATH, "//h2[contains(text(), 'Регистрация')]")  #Заголовок "Регистрация"
    NAME_FIELD = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  #Имя
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input") #Email
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")  #Пароль
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") #Кнопка "Зарегистрироваться"
    BUTTON_LOGOUT = (By.XPATH, '//button[contains(@class, "Account_button") and text()="Выход"]') # Выход из Личного кабинета

    
    LOGIN_HEADER = (By.XPATH, "//h2[contains(text(), 'Вход')]") #Заголовок "Вход"
    LOGIN_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input") #Email
    LOGIN_PASSWORD = (By.XPATH, "//input[@type='password']") #Пароль
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']") #Кнопка "Войти"

    EMAIL_INPUT = (By.CSS_SELECTOR, "input.input__textfield[type='text']")  #поле ввода "Email"
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input.input__textfield[type='password']")  #поле ввода "Пароль"
    PASSWORD_WRAPPER = (By.CSS_SELECTOR, "div.input_type_password") #обёртка поля "Пароль"

    BUTTON_LOGIN_ACCOUNT = (By.XPATH,"//button[text()='Войти в аккаунт']") #Кнопка "Войти в аккаунт"
    BUTTON_PERSONAL_ACCOUNT = ( By.XPATH,"//a[.//p[contains(text(), 'Личный Кабинет')]]") # Кнопка "Личный кабинет"
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]") # ссылка"Войти"

    BUTTON_ORDER = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]") #кнопка "Оформить заказ"
    PROFILE_SECTION = (By.XPATH, "//button[text()='Сохранить']")
    BUTTON_CONSTRUCTOR = (By.XPATH, "//a[.//p[contains(text(), 'Конструктор')]]") #Кнопка Конструктор
    LOGOTIP_STELLAR = (By.CSS_SELECTOR, "a[href='/']") #Логотип Стеллар Бургер
    ASSEMBLE_BURGER = (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]") # Собери бургер

class ConstructorLocators:
    TAB_BUNS = (By.XPATH, '//h2[contains(@class, "text_type_main-medium") and text()="Булки"]')
    TAB_SAUCES = (By.XPATH, '//h2[contains(@class, "text_type_main-medium") and text()="Соусы"]')
    TAB_FILLINGS = (By.XPATH, '//h2[contains(@class, "text_type_main-medium") and text()="Начинки"]')
    