from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import RegistrationLocators 


class TestProfile:
    def test_login_and_check_profile_section(self, logged_in_driver):
        driver = logged_in_driver
        wait = WebDriverWait(driver, 10)

        person_account_btn = wait.until(
            EC.element_to_be_clickable(RegistrationLocators.BUTTON_PERSONAL_ACCOUNT))
        person_account_btn.click()

        wait.until(EC.url_contains("/account/profile"))

        profile_section = wait.until(
            EC.visibility_of_element_located(RegistrationLocators.PROFILE_SECTION))
        assert profile_section.is_displayed(), "В личном кабинете не отображается секция «Профиль»"