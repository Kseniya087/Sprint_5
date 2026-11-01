from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationLocators
from url import Url
from credentials import AUTH_EMAIL, AUTH_PASSWORD

def login(driver):
    wait = WebDriverWait(driver, 10)
    driver.get(Url.MAIN_URL)
    wait.until(EC.element_to_be_clickable(RegistrationLocators.BUTTON_PERSONAL_ACCOUNT)).click()
    wait.until(EC.url_contains("/login"))
    
    driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(AUTH_EMAIL)
    driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(AUTH_PASSWORD)
    
    driver.find_element(*RegistrationLocators.LOGIN_BUTTON).click()
    wait.until(EC.visibility_of_element_located(RegistrationLocators.BUTTON_ORDER))
