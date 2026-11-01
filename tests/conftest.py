import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from locators import RegistrationLocators, ConstructorLocators
from selenium.webdriver.support import expected_conditions as EC
from url import Url
from credentials import AUTH_EMAIL, AUTH_PASSWORD


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()

@pytest.fixture(scope="function")
def logged_in_driver(driver):
    wait = WebDriverWait(driver, 10)
    driver.get(Url.MAIN_URL)

    wait.until(EC.element_to_be_clickable(RegistrationLocators.BUTTON_PERSONAL_ACCOUNT)).click()
    wait.until(EC.url_contains("/login"))
    
    driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(AUTH_EMAIL)
    driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(AUTH_PASSWORD)
    driver.find_element(*RegistrationLocators.LOGIN_BUTTON).click()
    
    wait.until(EC.visibility_of_element_located(RegistrationLocators.BUTTON_ORDER))
    yield driver

@pytest.fixture(scope="function")
def on_register_page(driver):
    driver.get(Url.REGISTRATION_URL)
    yield driver

@pytest.fixture(scope="function")
def on_main_page(driver):
    driver.get(Url.MAIN_URL)
    yield driver

@pytest.fixture(scope="function")
def on_reset_password(driver):
    driver.get(Url.RESET_PASSWORD)
    yield driver
