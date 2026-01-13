import time

from selenium.webdriver.common.by import By


class ShopPage:
    def __init__(self,driver):
        self.driver = driver
        self.products = (By.XPATH, "//app-card[@class='col-lg-3 col-md-6 mb-3']")
        self.cartbutton = (By.XPATH,"//a[@class='nav-link btn btn-primary']")


    def add_product_to_cart(self,productname):

        products = self.driver.find_elements(*self.products)

        for product in products:
            product_name = product.find_element(By.XPATH, ".//h4/a").text
            if product_name == productname :
                product.find_element(By.XPATH, ".//div/button").click()
        time.sleep(2)

    def goto_cart(self):
        self.driver.find_element(*self.cartbutton).click()