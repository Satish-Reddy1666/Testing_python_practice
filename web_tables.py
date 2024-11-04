import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome("C:/Users/satis/Downloads/drivers/chromedriver-win64/chromedriver.exe")
driver.get('https://cosmocode.io/automation-practice-webtable/')
driver.maximize_window()
driver.execute_script("window.scrollTo(0, 700)")

table= driver.find_element(By.ID,"countries")
rows= table.find_elements(By.TAG_NAME,"tr")
print(len(rows))
target_value ="Bolivia"
found = False

for row in rows:
    cells = row.find_elements(By.TAG_NAME,'td')
    for cell in cells:
        if target_value in cell.text:
            print(f"found value '{target_value}")
            found = True
            break
    if found:
        break
if not found:
    print(f"Value '{target_value}' not found in the table")

time.sleep(2)
driver.quit()



