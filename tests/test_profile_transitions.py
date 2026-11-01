from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationLocators
from url import Url
from helpers import login

class TestProfileNavigation:
    def test_navigate_from_profile_to_constructor(self, driver):
        login(driver)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(RegistrationLocators.BUTTON_PERSONAL_ACCOUNT)).click()
        wait.until(EC.url_contains("/account/profile"))
      
        driver.find_element(*RegistrationLocators.BUTTON_CONSTRUCTOR).click()
        assert wait.until(EC.visibility_of_element_located(RegistrationLocators.ASSEMBLE_BURGER)), "Не перешли в конструктор или заголовок не отображается"

    def test_click_logo_from_profile(self, driver):
        login(driver)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(RegistrationLocators.BUTTON_PERSONAL_ACCOUNT)).click()
        wait.until(EC.url_contains("/account/profile"))
        
        driver.find_element(*RegistrationLocators.LOGOTIP_STELLAR).click()
        wait.until(EC.url_contains("/"))
        assert wait.until(EC.visibility_of_element_located(RegistrationLocators.ASSEMBLE_BURGER)), "По клику на логотип не вернулись на главную с конструктором"
