from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationLocators
from url import Url 
from credentials import AUTH_EMAIL, AUTH_PASSWORD

class TestLoginAuthentication:
    def test_login_via_main_page(self, on_main_page):
        driver = on_main_page
        wait = WebDriverWait(driver, 10)

        button_login_account = driver.find_element(*RegistrationLocators.BUTTON_LOGIN_ACCOUNT)
        button_login_account.click()

        wait.until(EC.url_contains("/login"))

        assert wait.until(
            EC.visibility_of_element_located(RegistrationLocators.LOGIN_HEADER)
        ).is_displayed(), "После регистрации не открылась страница входа"
        

    def test_login_via_header_profile(self, on_main_page):
        driver = on_main_page
        wait = WebDriverWait(driver, 10)

        button_person_account = driver.find_element(*RegistrationLocators.BUTTON_PERSONAL_ACCOUNT)
        button_person_account.click()

        wait.until(EC.url_contains("/login"))

        assert wait.until(
            EC.visibility_of_element_located(RegistrationLocators.LOGIN_HEADER)
        ).is_displayed(), "После регистрации не открылась страница входа"


    def test_login_from_registration_form(self, on_register_page):
        driver = on_register_page
        wait = WebDriverWait(driver, 10)

        login_link = driver.find_element(*RegistrationLocators.LOGIN_LINK)
        login_link.click()

        wait.until(EC.url_contains("/login"))

        assert wait.until(
            EC.visibility_of_element_located(RegistrationLocators.LOGIN_HEADER)
        ).is_displayed(), "После регистрации не открылась страница входа"


    def test_login_from_recovery_form(self, on_reset_password):
        driver = on_reset_password
        wait = WebDriverWait(driver, 10)

        login_link = driver.find_element(*RegistrationLocators.LOGIN_LINK)
        login_link.click()
        
        wait.until(EC.url_contains("/login"))
        
        assert wait.until(
            EC.visibility_of_element_located(RegistrationLocators.LOGIN_HEADER)
        ).is_displayed(), "После регистрации не открылась страница входа"


class TestAuth:
    @staticmethod
    def _login(driver):
        wait = WebDriverWait(driver, 10)
        driver.get(Url.MAIN_URL)
        wait.until(EC.element_to_be_clickable(RegistrationLocators.BUTTON_PERSONAL_ACCOUNT)).click()
        wait.until(EC.url_contains("/login"))
        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(AUTH_EMAIL)
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(AUTH_PASSWORD)
        driver.find_element(*RegistrationLocators.LOGIN_BUTTON).click()
        wait.until(EC.visibility_of_element_located(RegistrationLocators.BUTTON_ORDER))

    def test_logout_from_profile(self, driver):
        self._login(driver)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(RegistrationLocators.BUTTON_PERSONAL_ACCOUNT)).click()
        wait.until(EC.url_contains("account/profile"))
        logout_btn = wait.until(EC.element_to_be_clickable(RegistrationLocators.BUTTON_LOGOUT))
        logout_btn.click()
        wait.until(EC.url_contains("/login"))
        assert driver.current_url.endswith("/login"), "Не выполнен редирект на страницу входа"
