from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:/Users/satis/Downloads/drivers/chromedriver-win64/chromedriver.exe")
driver.maximize_window()

username="standard_user"
password1="secret_sauce"
login_url="https://www.saucedemo.com/v1/"

driver.get(login_url)
username_field=driver.find_element(By.ID, "user-name").send_keys(username)
password_field=driver.find_element(By.ID, "password").send_keys(password1)
driver.find_element(By.ID, "login-button").click()

success_element= driver.find_element(By.CLASS_NAME,"product_label")
assert success_element.text == "Products" #here we use asser method to compare the element and to sent assertion error in case of false.

driver.back()
driver.close()

#driver.find_element(By.XPATH, value=".oxd-text.oxd-text--p.orangehrm-login-forgot-header").click()


























