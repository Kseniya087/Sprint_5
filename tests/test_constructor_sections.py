import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import RegistrationLocators, ConstructorLocators
from url import Url

class TestConstructorSections:
    @pytest.mark.parametrize("section_locator,expected_header", [
        (ConstructorLocators.TAB_BUNS, "Булки"),
        (ConstructorLocators.TAB_SAUCES, "Соусы"),
        (ConstructorLocators.TAB_FILLINGS, "Начинки"),])
    
    def test_section_transition(self, logged_in_driver, section_locator, expected_header):
        driver = logged_in_driver
        wait = WebDriverWait(driver, 10)
        
        # Переход в конструктор
        driver.find_element(*RegistrationLocators.BUTTON_CONSTRUCTOR).click()
        wait.until(EC.url_contains("/"))
        
        section_btn = wait.until(EC.element_to_be_clickable(section_locator))
        section_btn.click()
        
        ingredients_list = wait.until(
            EC.presence_of_element_located(("xpath", f"//h2[text()='{expected_header}']/following-sibling::ul")))
        assert ingredients_list.is_displayed()

