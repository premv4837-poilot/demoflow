from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Checkout:

    def __init__(self, driver):
        self.driver = driver
        # Locators
        self.checkout_btn = (By.XPATH, "//button[@class='btn btn-success']")
        self.country_input = (By.ID, "country")
        self.country_option = (By.LINK_TEXT, "India")
        self.checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.purchase_btn = (By.XPATH, "//input[@type='submit']")
        self.success_msg_div = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def checkout_pay(self):
        self.driver.find_element(*self.checkout_btn).click()

    def purchase(self, country_name):
        wait = WebDriverWait(self.driver, 10)

        # Wait until input visible and type country
        country_input_element = wait.until(
            EC.visibility_of_element_located(self.country_input))

        country_input_element.clear()
        country_input_element.click()
        country_input_element.send_keys(country_name)

        # Wait until auto-suggestion appears and click
        wait.until(EC.visibility_of_element_located(self.country_option))
        self.driver.find_element(*self.country_option).click()

        # Click checkbox and purchase button
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.purchase_btn).click()

    def success_msg(self):
        wait = WebDriverWait(self.driver, 10)
        # Wait for the success alert
        wait.until(EC.visibility_of_element_located(self.success_msg_div))
        msg = self.driver.find_element(*self.success_msg_div).text
        print(msg)
        assert "Success! Thank you!" in msg
