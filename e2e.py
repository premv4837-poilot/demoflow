import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/shop")

products = driver.find_elements(By.XPATH,"//app-card[@class='col-lg-3 col-md-6 mb-3']")

for product in products:
    productname = product.find_element(By.XPATH,".//h4/a").text
    if productname == "Blackberry":
        product.find_element(By.XPATH,".//div/button").click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()

driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()

driver.find_element(By.ID,"country").send_keys("ind")

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))

driver.find_element(By.LINK_TEXT,"India").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()

driver.find_element(By.XPATH,"//input[@type='submit']").click()
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='alert alert-success alert-dismissible']")))
alert = driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text

assert "Success! Thank you!" in alert




