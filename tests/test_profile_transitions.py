
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import RegistrationLocators, ConstructorLocators
from url import Url

class TestProfileNavigation:
    @staticmethod
    def _login(driver):
        wait = WebDriverWait(driver, 10)
        driver.get(Url.MAIN_URL)
        wait.until(EC.element_to_be_clickable(RegistrationLocators.BUTTON_PERSONAL_ACCOUNT)).click()
        wait.until(EC.url_contains("/login"))
        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys("kkoltsova54123@yandex.ru")
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys("Rctybz123")
        driver.find_element(*RegistrationLocators.LOGIN_BUTTON).click()
        wait.until(EC.visibility_of_element_located(RegistrationLocators.BUTTON_ORDER))

    def test_navigate_from_profile_to_constructor(self, driver):
        self._login(driver)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(RegistrationLocators.BUTTON_PERSONAL_ACCOUNT)).click()
        wait.until(EC.url_contains("/account/profile"))
      
        driver.find_element(*RegistrationLocators.BUTTON_CONSTRUCTOR).click()
        header = wait.until(EC.visibility_of_element_located(RegistrationLocators.ASSEMBLE_BURGER))
        assert header.text == "Соберите бургер", "Не перешли в конструктор или заголовок неверен"

    def test_click_logo_from_profile(self, driver):
        self._login(driver)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(RegistrationLocators.BUTTON_PERSONAL_ACCOUNT)).click()
        wait.until(EC.url_contains("/account/profile"))
        
        driver.find_element(*RegistrationLocators.LOGOTIP_STELLAR).click()
        wait.until(EC.url_contains("/"))
        header = wait.until(EC.visibility_of_element_located(RegistrationLocators.ASSEMBLE_BURGER))
        assert header.text == "Соберите бургер", "По клику на логотип не вернулись на главную с конструктором"
