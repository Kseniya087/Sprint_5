from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationLocators
from generators import generate_email, generate_password
import time

class TestRegistration:
    def test_registration_success(self, on_register_page):
        driver = on_register_page
        wait = WebDriverWait(driver, 10)

        # Проверяем заголовок «Регистрация»
        reg_header = wait.until(
            EC.visibility_of_element_located(RegistrationLocators.REGISTER_HEADER)
        )
        assert reg_header.is_displayed(), "Заголовок 'Регистрация' не найден"

        # Генерируем данные
        email = generate_email()
        password = generate_password()
        name = "Ксения"  

        print(f"Данные для регистрации: email={email}, name={name}, password={password}")

        # Заполняем поля
        name_field = driver.find_element(*RegistrationLocators.NAME_FIELD)
        name_field.clear()
        name_field.send_keys(name)

        email_field = driver.find_element(*RegistrationLocators.EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(email)

        password_field = driver.find_element(*RegistrationLocators.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(password)

        # Нажимаем кнопку
        register_btn = driver.find_element(*RegistrationLocators.REGISTER_BUTTON)
        register_btn.click()

        # Ждём перехода на /login
        wait.until(EC.url_contains("/login"))

        # Проверяем, что открылся экран «Вход»
        login_header = wait.until(
            EC.visibility_of_element_located(RegistrationLocators.LOGIN_HEADER)
        )
        assert login_header.is_displayed(), "После регистрации не открылась страница входа"


class TestRegistrationNegative:
    def test_password_too_short(self, on_register_page):
        driver = on_register_page
        
        # Готовим данные 
        email = generate_email()
        password = generate_password(5)
        name = "Анна"

        # Заполняем поля 
        driver.find_element(*RegistrationLocators.NAME_FIELD).send_keys(name)
        driver.find_element(*RegistrationLocators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)

        # Нажимаем кнопку регистрации
        driver.find_element(*RegistrationLocators.REGISTER_BUTTON).click()

        time.sleep(3)

        # Находим тот самый блок, который должен стать красным
        password_wrapper = driver.find_element(*RegistrationLocators.PASSWORD_WRAPPER)
        
        current_classes = password_wrapper.get_attribute("class")

        assert "input_status_error" in current_classes, "Ошибка: поле пароля не подсветилось красным!"
