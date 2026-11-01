from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationLocators
from generators import generate_email, generate_password

class TestRegistrationPositive:
    def test_registration_header_visible(self, on_register_page):
        driver = on_register_page
        wait = WebDriverWait(driver, 10)
        reg_header = wait.until(
            EC.visibility_of_element_located(RegistrationLocators.REGISTER_HEADER)
        )
        assert reg_header.is_displayed(), "Заголовок 'Регистрация' не найден"

    def test_registration_success_flow(self, on_register_page):
        driver = on_register_page
        wait = WebDriverWait(driver, 10)
        email = generate_email()
        password = generate_password()
        name = "Ксения"

        driver.find_element(*RegistrationLocators.NAME_FIELD).clear()
        driver.find_element(*RegistrationLocators.NAME_FIELD).send_keys(name)
        driver.find_element(*RegistrationLocators.EMAIL_FIELD).clear()
        driver.find_element(*RegistrationLocators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*RegistrationLocators.PASSWORD_FIELD).clear()
        driver.find_element(*RegistrationLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*RegistrationLocators.REGISTER_BUTTON).click()

        wait.until(EC.url_contains("/login"))
        login_header = wait.until(
            EC.visibility_of_element_located(RegistrationLocators.LOGIN_HEADER)
        )
        assert login_header.is_displayed(), "После регистрации не открылась страница входа"


class TestRegistrationNegative:
    def test_password_too_short_validation(self, on_register_page):
        driver = on_register_page
        email = generate_email()
        password = generate_password(5)
        name = "Анна"

        driver.find_element(*RegistrationLocators.NAME_FIELD).send_keys(name)
        driver.find_element(*RegistrationLocators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationLocators.REGISTER_BUTTON).click()

        wait = WebDriverWait(driver, 10)
        password_wrapper = wait.until(
            EC.visibility_of_element_located(RegistrationLocators.PASSWORD_WRAPPER)
        )
        current_classes = password_wrapper.get_attribute("class")
        assert "input_status_error" in current_classes, "Ошибка: поле пароля не подсветилось красным!"

