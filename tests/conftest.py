import pytest
from selenium import webdriver
from url import Url
from selenium.webdriver.support.ui import WebDriverWait
from locators import RegistrationLocators, ConstructorLocators
from selenium.webdriver.support import expected_conditions as EC

# Твои URL
MAIN_URL = "https://stellarburgers.education-services.ru"
REGISTRATION_URL = f"{MAIN_URL}/register"
LOGIN_URL = f"{MAIN_URL}/login"
RESET_PASSWORD = f"{MAIN_URL}/forgot-password"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def on_register_page(driver):
   driver.get(REGISTRATION_URL)
   return driver

@pytest.fixture
def on_main_page(driver):
    driver.get(MAIN_URL)
    return driver

@pytest.fixture
def on_reset_password(driver):
    driver.get(RESET_PASSWORD)
    return driver


@pytest.fixture(scope="session")
def auth_data():
    return {
        "email": "kkoltsova54123@yandex.ru",
        "password": "Rctybz123"}


@pytest.fixture(scope="function")
def logged_in_driver(driver, auth_data):
    wait = WebDriverWait(driver, 10)
    driver.get(Url.MAIN_URL)

    wait.until(EC.element_to_be_clickable(RegistrationLocators.BUTTON_PERSONAL_ACCOUNT)).click()
    wait.until(EC.url_contains("/login"))
    
    driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(auth_data["email"])
    driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(auth_data["password"])
    driver.find_element(*RegistrationLocators.LOGIN_BUTTON).click()
    
    wait.until(EC.visibility_of_element_located(RegistrationLocators.BUTTON_ORDER))
    yield driver