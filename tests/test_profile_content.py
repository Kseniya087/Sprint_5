from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import RegistrationLocators 
from url import Url        

class TestProfile:
    def test_login_and_check_profile_section(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get(Url.MAIN_URL)

        profile_btn = wait.until(
            EC.element_to_be_clickable(RegistrationLocators.BUTTON_PERSONAL_ACCOUNT))
        profile_btn.click()

        wait.until(EC.url_contains("/login"))

        email_input = wait.until(
            EC.visibility_of_element_located(RegistrationLocators.EMAIL_INPUT))
        email_input.clear()
        email_input.send_keys("kkoltsova54123@yandex.ru") 

        password_input = driver.find_element(*RegistrationLocators.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys("Rctybz123")     

        login_btn = driver.find_element(*RegistrationLocators.LOGIN_BUTTON)
        login_btn.click()

        order_btn = wait.until(
              EC.visibility_of_element_located(RegistrationLocators.BUTTON_ORDER))
        assert order_btn.is_displayed(), "Кнопка «Оформить заказ» не отобразилась — пользователь не авторизован"

        person_account_btn = wait.until(
            EC.element_to_be_clickable(RegistrationLocators.BUTTON_PERSONAL_ACCOUNT))
        person_account_btn.click()

        wait.until(EC.url_contains("/account/profile"))

        profile_section = wait.until(
            EC.visibility_of_element_located(RegistrationLocators.PROFILE_SECTION))
        assert profile_section.is_displayed(), "В личном кабинете не отображается секция «Профиль»"