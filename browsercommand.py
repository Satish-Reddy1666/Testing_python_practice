from datetime import time
import time
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path="C:/Users/satis/Downloads/drivers/chromedriver-win64/chromedriver.exe")
#code for ultimate qa .com
driver.maximize_window()
driver.get("https://ultimateqa.com/complicated-page")
driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/div[1]/div[7]/div[2]/div[2]/div[2]/form[1]/p[3]/a[1]").click()


#code for orange hrm
'''driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.CSS_SELECTOR, "a[href='http://www.orangehrm.com']").click()'''

#code for para bank
'''driver.maximize_window()
driver.get("https://parabank.parasoft.com/parabank/lookup.htm;jsessionid=5E2373012F2CE58E5C642CCB4B0DA5EF")
driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()'''

time.sleep(2)
driver.back()   
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.quit() 

