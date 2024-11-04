
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome("C:/Users/satis/Downloads/drivers/chromedriver-win64/chromedriver.exe")
driver.get('https://the-internet.herokuapp.com/iframe')

iframe = driver.find_element(By.ID, "mce_0_ifr")
driver.switch_to.frame(iframe)

text_editor=driver.find_element(By.ID, "tinymce")
text_editor.clear()
text_editor.send_keys('hii this is seleniumm with python')

driver.switch_to.default_content()
driver.find_element(By.XPATH, '//a[normalize-space()="Elemental Selenium"]').click()

time.sleep(2)
driver.quit()

