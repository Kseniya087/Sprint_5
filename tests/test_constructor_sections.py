import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationLocators, ConstructorLocators


class TestConstructorSections:   
    @pytest.mark.parametrize("tab_locator,expected_text", [
        (ConstructorLocators.TAB_SAUCES, "Соусы"),
        (ConstructorLocators.TAB_FILLINGS, "Начинки"),
    ])
    def test_section_transition(self, logged_in_driver, tab_locator, expected_text):
        driver = logged_in_driver
        wait = WebDriverWait(driver, 10)

        driver.find_element(*RegistrationLocators.BUTTON_CONSTRUCTOR).click()
        wait.until(EC.url_contains("/"))

        target_tab = wait.until(EC.element_to_be_clickable(tab_locator))
        target_tab.click()

        wait.until(lambda d: "current" in target_tab.get_attribute("class"))
    
        assert "current" in target_tab.get_attribute("class"), f"Вкладка '{expected_text}' не стала активной"

    def test_buns_section_transition(self, logged_in_driver):
        driver = logged_in_driver
        wait = WebDriverWait(driver, 10)

        driver.find_element(*RegistrationLocators.BUTTON_CONSTRUCTOR).click()
        wait.until(EC.url_contains("/"))

        sauce_tab = wait.until(EC.element_to_be_clickable(ConstructorLocators.TAB_SAUCES))
        sauce_tab.click()
        wait.until(lambda d: "current" in sauce_tab.get_attribute("class"))

        buns_tab = wait.until(EC.element_to_be_clickable(ConstructorLocators.TAB_BUNS))
        buns_tab.click()
    
        wait.until(
        lambda d: "current" in d.find_element(*ConstructorLocators.TAB_BUNS).get_attribute("class"))
    
        active_buns = driver.find_element(*ConstructorLocators.TAB_BUNS)
        assert "current" in active_buns.get_attribute("class"), "Вкладка 'Булки' не стала активной"