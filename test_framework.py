import json
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions, wait
from selenium.webdriver.support.wait import WebDriverWait

from checkout_confirmation import Checkout
from login import LoginPage
from shop import ShopPage

test_data_path = 'Data/test_e2e.json'
with open(test_data_path) as f:
    test_data = json.load(f) #convert to json to python object
    test_list = test_data["data"]

@pytest.mark.parametrize("test_items",test_list)
def test_e2e(broswerInstance,test_items):

    driver = broswerInstance

    driver.get("https://rahulshettyacademy.com/angularpractice")

    loginpage = LoginPage(driver)
    loginpage.login(test_items["userEmail"],test_items["password"])

    shop = ShopPage(driver)
    shop.add_product_to_cart(test_items["productName"])
    shop.goto_cart()

    check = Checkout(driver)
    check.checkout_pay()
    time.sleep(5)
    check.purchase(test_items["county"])
    check.success_msg()



