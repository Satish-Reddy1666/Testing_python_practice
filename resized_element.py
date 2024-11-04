
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("C:/Users/satis/Downloads/drivers/chromedriver-win64/chromedriver.exe")
driver.maximize_window()

url='https://demo.automationtesting.in/Resizable.html'
driver.get(url)

res_ele_size = driver.find_element(By.XPATH,"//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
initial_ele_size = driver.find_element(By.ID,"resizable")
initial_size = initial_ele_size.size
print("initial_elementsize : ", initial_size)
time.sleep(3)

action= ActionChains(driver)
action.click_and_hold(res_ele_size).move_by_offset(xoffset=100,yoffset=100).release().perform()
time.sleep(3)

resized_size = initial_ele_size.size
print("resized_element_size : ", resized_size)

driver.quit()



