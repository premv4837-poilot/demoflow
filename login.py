from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.email_input =  (By.XPATH, "//input[@name='email']")
        self.password = (By.XPATH, "//input[@id='exampleInputPassword1']")
        self.submit = (By.XPATH, "//input[@type='submit']")
        self.shop = (By.XPATH, "//a[contains(@href,'shop')]")


    def login(self,username,passsword):
        self.driver.find_element(*self.email_input).send_keys(username)
        self.driver.find_element(*self.password).send_keys(passsword)
        self.driver.find_element(*self.submit).click()
        self.driver.find_element(*self.shop).click()

